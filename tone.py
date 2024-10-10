import numpy as np
import wavio, os, shutil

#number of files to generate
num = 15

rate = 44100
T = 0.1
f1 = 50.0
f2 = 100.0

def scale(inMin, inMax, outMin, outMax, input):
    return(((input-inMin)*((outMax-outMin)/(inMax-inMin)))+outMin)

def scaleList(inMin, inMax, outMin, outMax, input):
    output = []
    for i in input:
        output.append(scale(inMin, inMax, outMin, outMax, i))
    return output

def interp(min, max, interp):
    return((interp*(max-min))+min)

def clamp(v_min, v_max, input):
    return min(v_max, max(v_min, input))

def clampList(v_min, v_max, input):
    output = []
    for i in input:
        output.append(clamp(v_min, v_max, i))
    return output

#compute waveform samples
t = np.linspace(0, T, int(T*rate), endpoint=False)

print(t)
#write to file
# wavio.write("sine.wav", x, rate, sampwidth=3)

newDir = "toneGen/render"+str(int(os.listdir("toneGen")[-1][-1])+1)
print("Created new directory", newDir)
os.makedirs(newDir)

for i in range(num):
    audio = np.sin(2*np.pi * interp(f1, f2, scale(0, num, 0, 1, i)) * t)
    envelope = scaleList(0, 1, 1, 0, clampList(0, 1, np.linspace(0, 1, int(T*rate), endpoint=False) * 1.2))

    audio = audio * envelope
    wavio.write(newDir+"/sine"+str(i)+".wav", audio, rate, sampwidth=3)
