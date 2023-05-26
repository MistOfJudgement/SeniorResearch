#Take the replay filename, creates the frame data file, then sorts the images in one python script.
rep = "2021_12_07_08_57_06"
imagesFolder = r"C:\Users\1499106\CompSciRes\nullpomino-master\nullpomino-run\target\install\ss"
image_prefix = "replay_2021-12-07-13-57-06"

replay = open(f"{rep}.rep", "r")
replayObject = {}
def processLine(line):
    print(line)
    if len(line.strip()) == 0 or line.strip()[0] == "#":
        return
    temp = line.split("=")
    temp2 = temp[0].split(".")
    nester = replayObject
    for value in temp2[:-1]:
        if value not in nester:                
            nester[value] = {}
        nester = nester[value]

    if type(nester) == dict:
        nester[temp2[-1]] = temp[1]

for line in replay.read().split("\n"):
    processLine(line)

import json
with open(f"{rep}.json","w") as f:
    json.dump(replayObject,f)

replay.close()

### in bit order (up, down, left, right, A, B, C, D, E, F)

frames = [0 for i in range(int(replayObject["0"]["r"]["max"]))]
lastInput = 0

#copy the inputs to a new dictionary
import copy
inputs = copy.deepcopy(replayObject["0"]["r"])
del inputs["max"]
keys = list(inputs.keys())
keys.sort(key = lambda x: int(x))
lastKey = int(keys[0])
for key in keys[1:]:
    print(key)
    frames[lastKey:int(key)] = [int(replayObject["0"]["r"][key]) for i in range(int(key) - lastKey)]
    lastKey = int(key)

#print to a file
with open(f"{rep}.txt","w") as f:
    for frame in frames:
        f.write(str(frame) + "\n")
# print(frames)

framePath = f"{rep}.txt"
import os
imagesFolder = r"C:\Users\1499106\CompSciRes\nullpomino-master\nullpomino-run\target\install\ss"
#put each line of the frame.txt file into a list
frames = []
with open(framePath,"r") as f:
    frames = f.read().split("\n")
    frames = [int(i) for i in frames if len(i) > 0]

for image in os.listdir(imagesFolder):
    print(image)
    if image.startswith(image_prefix):
        frame = image.split("F")[1].split(".")[0]
        inputs = frames[int(frame)]
        print(inputs)
        #if a folder with the name of the inputs doesn't exist, create it
        if not os.path.exists(os.path.join(imagesFolder,str(inputs))):
            os.mkdir(os.path.join(imagesFolder,str(inputs)))
        #move the image to the folder without renaming it
        os.rename(os.path.join(imagesFolder,image),os.path.join(imagesFolder,str(inputs),image))

    

