import os
# print(os.getcwd())

# os.makedirs("render"+int(str((os.listdir("testDir"))[-1])[-1])+1)
newDir = "testDir/render"+str(int(os.listdir("testDir")[-1][-1])+1)
print("Created new directory", newDir)
os.makedirs(newDir)
