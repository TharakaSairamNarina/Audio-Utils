import wave
import os
import contextlib
from pydub import AudioSegment

def findlength(filename):
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return int(duration)

c=1
for filename in os.listdir('Path_Directory'):
    if(filename.endswith(".wav")):  
        # print(filename)
        filename='Path_Directory'+filename
        t1,t2= 300,320
        length=findlength(filename) 
        # print(i)
        while(t2<length):
            newAudio = AudioSegment.from_wav(filename)
            newAudio = newAudio[t1*1000:t2*1000]
            newAudio.export('Language'+str(c)+'.wav', format="wav")
            c+=1
            t1=t2
            t2+=20
