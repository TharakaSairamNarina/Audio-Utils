"""
    This code will convert all the stereo audio files in source path to mono audios and store them in destination path
    ffmpeg is a tool need to be installed and set path in system environment variables
"""
import os
import glob
import time
num=1
t1=time.time()
for filename in os.listdir('Directory_Path'):  
    file_path='Directory_Path'+filename
    destination='Destination_Path'+str(num)+'.wav'
    if (filename.endswith(".wav")): 
        os.system("ffmpeg -i "+file_path+" -ac 1 -ar 8000 "+destination)
        num+=1
print(time.time()-t1)
