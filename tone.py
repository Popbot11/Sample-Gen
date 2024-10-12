import numpy as np
import wavio, os
import utilFunctions as utf
import inspect


rate = 44100 #sample rate


def sineBlip(freq, decayLen, fileLen):
    """Generate a sine wave of 'freq' frequency that immediately decays for 'decayLen' seconds, in an audio of length 'fileLen' seconds."""

    t = np.linspace(0, fileLen, int(fileLen*rate), endpoint=False) #generate ascenting list of values from 0 to 3, one value for each sample
    
    audio = np.sin(2*np.pi * freq * t) #use t to generate a sine
    envelope = utf.scaleList(0, 1, 1, 0, utf.clampList(0, 1, np.linspace(0, 1, int(fileLen*rate), endpoint=False) * (fileLen/decayLen))) #generate a list of values in equal length to audio, consisting of cv 

    audio = audio * envelope #functionally a vca
    return audio #output


#this whole thing here is current pretty broken, fix later
num = int(input("number of files to create: ")) #number of files to generate
#later once I have multiple functions, implement a system to choose which one
paramNames = inspect.getfullargspec(sineBlip)[0]
paramStart = []
paramEnd = []
params = []
for i in range(len(paramNames)):
    paramStart.append(float(input(paramNames[i]+" start value: ")))
    paramEnd.append(float(input(paramNames[i]+" end value: ")))

print(paramNames, paramStart, paramEnd, params)
#comment 
if (str(input("generate files? y/n ")).upper()=="y".upper()):

    newDir = "toneGen/render"+str(int(os.listdir("toneGen")[-1][-1])+1)
    print("Created new directory", newDir)
    os.makedirs(newDir)

    # gradient = np.linspace(0, 1, num)
    for i in range(num):
        interpVal = i / num
        params = []
        for j in range(len(paramNames)):
            params.append(utf.interp(paramStart[j], paramEnd[j], interpVal))
        print(params)
        audio = sineBlip(*params)
        # audio = [sineBlip()]
        wavio.write(newDir+"/sine"+str(i)+".wav", audio, rate, sampwidth=3)

    print("created", num, "files in", newDir)
