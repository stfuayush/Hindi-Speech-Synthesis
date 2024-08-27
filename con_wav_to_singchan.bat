mkdir out
for %%a in (*.wav) do ffmpeg -i "%%a" -ar 22050 -ac 1 out/"%%a"