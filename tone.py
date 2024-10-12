import numpy as np
import wavio, os, random
import utilFunctions as utf
import inspect


rate = 44100 #sample rate

def sine(freq, fileLen):
    """generate a sine wave of `fileLen` length and `freq` frequency"""
    
    t = np.linspace(0, fileLen, int(fileLen*rate), endpoint=False) #generate ascenting list of values from 0 to 3, one value for each sample
    audio = np.sin(2*np.pi * freq * t) #use t to generate a sine
    
    return audio

def sineBlip(freq, decayLen, fileLen):
    """Generate a sine wave of `freq` frequency that immediately decays for `decayLen`` seconds, in an audio of length `fileLen` seconds."""

    t = np.linspace(0, fileLen, int(fileLen*rate), endpoint=False) #generate ascenting list of values from 0 to 3, one value for each sample
    audio = np.sin(2*np.pi * freq * t) #use t to generate a sine
    envelope = utf.scaleList(0, 1, 1, 0, utf.clampList(0, 1, np.linspace(0, 1, int(fileLen*rate), endpoint=False) * (fileLen/decayLen))) #generate a list of values in equal length to audio, consisting of cv 

    audio = audio * envelope #functionally a vca
    return audio 

def noise(fileLen):
    """generate a file of `fileLen` length containing mono white noise"""
    audio = [random.uniform(-1.0, 1.0) for x in range(int(fileLen*rate))] #generate list of random values from 0 to 1, one value for each audio sample
    
    return audio

def noiseBlip(decayLen, fileLen):
    """Generate a sine wave of `freq` frequency that immediately decays for `decayLen`` seconds, in an audio of length `fileLen` seconds."""

    audio = [random.uniform(-1.0, 1.0) for x in range(int(fileLen*rate))] #use t to generate a sine
    envelope = utf.scaleList(0, 1, 1, 0, utf.clampList(0, 1, np.linspace(0, 1, int(fileLen*rate), endpoint=False) * (fileLen/decayLen))) #generate a list of values in equal length to audio, consisting of cv 

    audio = audio * envelope #functionally a vca
    return audio 

def impulseTrain(count, period, fileLen):
    
    audio = [1 if (x % period == 0) and (x < period * count) else (-1) for x in range(int(rate * fileLen))] #generate silence of length (fileLen * rate)

    return audio




generate = {
    "sine": sine,
    "sineBlip": sineBlip,
    "noise": noise,
    "noiseBlip": noiseBlip,
    "impulseTrain": impulseTrain
}


print(utf.dictToStr(generate))
choice = str(input("choose a generator from the list:"))
num = int(input("number of files to create: ")) #number of files to generate
fileName = str(input("name for each file: "))


paramNames = inspect.getfullargspec(generate[choice])[0]
paramStart = []
paramEnd = []
params = []
for i in range(len(paramNames)):
    paramStart.append(float(input(paramNames[i]+" start value: ")))
    paramEnd.append(float(input(paramNames[i]+" end value: ")))

# print(paramNames, paramStart, paramEnd, params)

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
        print(i, params)
        audio = generate[choice](*params)
        # audio = [sineBlip()]
        wavio.write(newDir+"/"+fileName+str(i)+".wav", audio, rate, sampwidth=3)

    print("created", num, "files in", newDir)


