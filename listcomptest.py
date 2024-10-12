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
audio = [1 if y % 5 == 0 and y < 20 else 0 for y in range(40)] 
print(audio)