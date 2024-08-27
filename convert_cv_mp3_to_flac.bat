@ECHO OFF

rem Define the sample path (replace with your actual path)
set "sample_path=C:\tts\datasets\vctk-cv-hi-22k\wav48_silence_trimmed"

cd /D "%sample_path%"

for /d %%ytid in (*) do (
  echo %%ytid
  cd /D "%%ytid"
  
  for %%mp3 in (*.mp3) do (
    echo %%mp3
    set "trim_ytid=%%~nytid"
    ffmpeg -i "%%mp3" -ar 22050 -acodec flac -af aresample=osf=s16:dither_method=triangular_hp -ac 1 "%%~n%%mp3_mic1.flac"
    del "%%mp3"
  )
  cd ..
)