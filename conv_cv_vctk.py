import csv
import os
import subprocess

from pandas import read_csv
ds_name="vctk-cv-hi-22k"
 cv_in_path = 'c:\\tts\\datasets\\hi\\'
df = read_csv(cv_in_path+'validated.tsv', delimiter='\t', encoding='utf-8')
out_path_root = 'c:\\tts\\datasets\\'
print(df)

for i in range(0, len(df)):
    file_name = df.iloc[i]['path']
    file_name = os.path.basename(file_name)
    dir_name= os.path.dirname(file_name)
    subprocess.run(["mkdir", "-p", out_path_root+ds_name+'/txt/'+str(dir_name)])
    mp3_file = file_name
    file_name = file_name[:-4]
    subprocess.run(["mkdir", "-p", out_path_root+ds_name+'/txt/'+str(df.iloc[i]['client_id'])])
    subprocess.run(["mkdir", "-p", out_path_root+ds_name+'/wav48_silence_trimmed/'+str(df.iloc[i]['client_id'])])
    subprocess.run(["cp", cv_in_path+"/clips/"+mp3_file, out_path_root+ds_name+'/wav48_silence_trimmed/'+str(df.iloc[i]['client_id'])])
    outfilepath = out_path_root+ds_name+'/txt/'+df.iloc[i]['client_id']+'/'+file_name+'.txt'
    with open(outfilepath, 'w', encoding='utf-8') as vctk_txt_out:
        vctk_txt_out.write(df.iloc[i]['sentence'])
df2 = df.groupby(['client_id'])['client_id'].count()

df2.to_csv("hi-ids.csv", sep='\t', encoding='utf-8')