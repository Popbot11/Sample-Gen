# import random

# newlist = [random.uniform(-1.0, 1.0) for x in range(5)]
# print(newlist)

# generate = {
#     "sineBlip": "yes",
#     "noise": "no"
# }

# def dictToStr(dict):
#     output = ""
#     for i in dict:
#         output +=( str(i) + ", ")

#     return output




# print(dictToStr(generate))
# audio = [0 for x in range(40)]
# audio = [1 if y % 5 == 0 and y <= 20 else 0 for y in range(40)] 
period = 3
count = 6
rate = 1
fileLen = 40

audio = [1 if (x % period == 0) and (x < period * count) else (0) for x in range(int(rate * fileLen))]
print(audio)