from PIL import Image
from collections import defaultdict
import numpy as np

image_to_replicate = "SCAR.png" # must be png

blocks = {
    "black_concrete": [8, 10, 15, 255], #080a0f
    "blue_concrete": [45, 47, 143, 255], #2d2f8f
    "brown_concrete": [96, 60, 32, 255], #603c20
    "cyan_concrete": [21, 119, 136, 255], #157788
    "gravel": [132, 127, 127, 255], #847f7f
    "gray_concrete": [55, 58, 62, 255], #373a3e
    "green_concrete": [73, 91, 36, 255], #495b24
    "light_blue_concrete": [36, 137, 199, 255], #2489c7
    "light_gray_concrete": [125, 125, 115, 255], #7d7d73
    "lime_concrete": [94, 169, 24, 255], #5ea918
    "magenta_concrete": [169, 48, 159, 255], #a9309f
    "orange_concrete": [224, 97, 1, 255], #e06101
    "pink_concrete": [214, 101, 143, 255], #d6658f
    "purple_concrete": [100, 32, 156, 255], #64209c
    "red_concrete": [142, 33, 33, 255], #8e2121
    "red_sand": [191, 103, 33, 255], #bf6721
    "sand": [219, 207, 163, 255], #dbcfa3
    "white_concrete": [207, 213, 214, 255], #cfd5d6
    "yellow_concrete": [241, 175, 21, 255] #f1af15
}


img = Image.open(image_to_replicate)
imgArr = np.array(img)
print(imgArr.shape)
w, h, _ = imgArr.shape

def findClosest(r, g, b):
    bestBlock = ""
    bestDistance = 9999999999999999.0

    for block, colour in blocks.items():
        distance = (r-colour[0])**2+(g-colour[1])**2+(b-colour[2])**2



        if distance < bestDistance:
            bestBlock = block
            bestDistance = distance
    
    return blocks[bestBlock], bestBlock

outputImage = np.zeros(shape = (w, h, 4))
outputBlocks = np.empty((w, h), dtype=str)
#print(output)

for x in range(w):
    for y in range(h):
        outputImage[x, y], outputBlocks = findClosest(*imgArr[x, y])

outputImage = outputImage.astype("uint8")
#print(outputImage)

invimg = Image.fromarray(outputImage)
#invimg.show()
invimg.save(image_to_replicate[:-4]+'-minecrafted.png')