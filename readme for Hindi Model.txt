XTTSv2 Hindi FineTuning



Indic TTS Hindi Dataset

https://www.iitm.ac.in/donlab/indictts/database

Common Voice Dataset

https://commonvoice.mozilla.org/en/datasets


(ALL SCRIPTS AND BAT FILES ARE INCLUDED IN THE MAIN DIRECTORY)

Convert Mozilla Common Voice .TSV to VCTK format dataset metadata using
script included named conv_cv_vctk.py


Download and install ffmpeg, and add it to your windows system path environment variable. Using convert_cv_mp3_to_flac.bat.


Convert Indic TTS format dataset metadata file to LJspeech format metadata file:
Using script named conv_indic_to_ljs.py


Convert wavs to single channel, 22050hz.
Using con_wav_to_singchan.bat


Remove missing file entries from LJSpeech format dataset:
Using rm_missing.py

Batch inference test a directory of samples with a list of sentences.
Using hindi_xttx_finetuned.ipynb
