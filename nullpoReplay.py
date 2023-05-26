rep = "2022_01_09_18_15_24"
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


    
