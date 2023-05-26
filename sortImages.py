import os
imagesFolder = r"C:\Users\1499106\CompSciRes\nullpomino-master\nullpomino-run\target\install\ss"
framePath = r"C:\Users\1499106\CompSciRes\2021_12_07_08_57_06.txt"
#put each line of the frame.txt file into a list
frames = []
with open(framePath,"r") as f:
    frames = f.read().split("\n")
    frames = [int(i) for i in frames if len(i) > 0]

for image in os.listdir(imagesFolder):
    print(image)
    frame = image.split("F")[1].split(".")[0]
    inputs = frames[int(frame)]
    print(inputs)
    #if a folder with the name of the inputs doesn't exist, create it
    if not os.path.exists(os.path.join(imagesFolder,str(inputs))):
        os.mkdir(os.path.join(imagesFolder,str(inputs)))
    #move the image to the folder without renaming it
    os.rename(os.path.join(imagesFolder,image),os.path.join(imagesFolder,str(inputs),image))

    
