import os
import torch
import torchaudio
from datetime import datetime
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import logging
import time
logger = logging.getLogger(__name__)
print("Loading model...")
config = XttsConfig()
config.load_json("./xtts/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="./xtts/", use_deepspeed=False)
#config.enable_readaction=True
model.cuda()
speakerpath = "./speakers-hi/"
phrases = ["जलवायु परिवर्तन से निपटने के लिए वैश्विक प्रयास तेज़ी से बढ़ रहे हैं, क्योंकि दुनिया भर के देश कार्बन उत्सर्जन को कम करने का संकल्प ले रहे हैं। संयुक्त राष्ट्र ने औद्योगिक क्रांति से पहले के स्तरों की तुलना में वैश्विक तापमान वृद्धि को 1.5 डिग्री सेल्सियस तक सीमित करने के लिए त्वरित कार्रवाई की अपील की है, और सरकारें इस दिशा में महत्वाकांक्षी योजनाएं बना रही हैं। तकनीकी क्षेत्र में, कृत्रिम बुद्धिमत्ता (A.I) के क्षेत्र में महत्वपूर्ण प्रगति हो रही है, जो विभिन्न उद्योगों के भविष्य को आकार दे रही है। स्वास्थ्य सेवा से लेकर वित्त तक, A.I व्यवसायों के संचालन के तरीके को बदल रहा है, जिससे नए अवसर और नवाचार की संभावनाएं सामने आ रही हैं। खेल जगत में, आगामी ओलंपिक खेलों का आयोजन दर्शकों के लिए बेहद रोमांचक होने वाला है। खिलाड़ी वैश्विक मंच पर प्रतिस्पर्धा के लिए तैयार हैं, अपनी क्षमताओं और दृढ़ संकल्प को प्रदर्शित करते हुए। यह आयोजन एक रोमांचक नज़ारा होगा, जिसमें नए रिकॉर्ड बनने की उम्मीद है। अंत में, मनोरंजन की दुनिया में, एक बहुप्रतीक्षित फिल्म ने बॉक्स ऑफिस पर रिकॉर्ड तोड़ दिया है। इस फिल्म में अत्याधुनिक विशेष प्रभाव और एक सितारों से सजी कास्ट है, जिसने समीक्षकों और दर्शकों दोनों से प्रशंसा प्राप्त की है।"]

print(len(phrases))
for filename in os.listdir(speakerpath):
    if filename.endswith(".wav"):
        for phrase in phrases:
            start_time = time.time()

            print("Computing speaker latents...")
            gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=[speakerpath+filename])

            print("Inference...")
            out = model.inference(
            phrase,
            "hi",
            gpt_cond_latent, 
            speaker_embedding,
            temperature=0.7, # Add custom parameters here
        )
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # compute stats
            process_time = time.time() - start_time
            audio_time = len(torch.tensor(out["wav"]).unsqueeze(0) / 24000)
            logger.warning("Processing time: %.3f", process_time)
            logger.warning("Real-time factor: %.3f", process_time / audio_time)
            torchaudio.save(f"{now}-xtts.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)