import numpy as np
import wavio, os, shutil
import utilFunctions as utf

num = 10 #number of files to generate

rate = 44100 #sample rate
T = 0.1 #length of each file in seconds
f1 = 50.0 #starting frequency
f2 = 100.0 #ending frequency

# def sineBlip(freq, ):
#compute waveform samples


# print(t)
#write to file
# wavio.write("sine.wav", x, rate, sampwidth=3)



if (input("generate files? y/n ").upper()=="y".upper()):

    t = np.linspace(0, T, int(T*rate), endpoint=False)
    newDir = "toneGen/render"+str(int(os.listdir("toneGen")[-1][-1])+1)
    print("Created new directory", newDir)
    os.makedirs(newDir)     

    for i in range(num):
        audio = np.sin(2*np.pi * utf.interp(f1, f2, utf.scale(0, num, 0, 1, i)) * t)
        envelope = utf.scaleList(0, 1, 1, 0, utf.clampList(0, 1, np.linspace(0, 1, int(T*rate), endpoint=False) * 1.2))

        audio = audio * envelope
        wavio.write(newDir+"/sine"+str(i)+".wav", audio, rate, sampwidth=3)

    print("created", num, "files in", newDir)
