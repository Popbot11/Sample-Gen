import numpy as np

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

def dictToStr(dict):
    output = ""
    for i in dict:
        output +=( str(i) + ", ")

    return output