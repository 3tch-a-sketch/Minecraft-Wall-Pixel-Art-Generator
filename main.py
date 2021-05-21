from PIL import Image
import numpy as np
import math

blocks = {
    "black_concrete": [8, 10, 15], #080a0f
    "blue_concrete": [45, 47, 143], #2d2f8f
    "brown_concrete": [96, 60, 32], #603c20
    "cyan_concrete": [21, 119, 136], #157788
    "gravel": [132, 127, 127], #847f7f
    "gray_concrete": [55, 58, 62], #373a3e
    "green_concrete": [73, 91, 36], #495b24
    "light_blue_concrete": [36, 137, 199], #2489c7
    "light_gray_concrete": [125, 125, 115], #7d7d73
    "lime_concrete": [94, 169, 24], #5ea918
    "magenta_concrete": [169, 48, 159], #a9309f
    "orange_concrete": [224, 97, 1], #e06101
    "pink_concrete": [214, 101, 143], #d6658f
    "purple_concrete": [100, 32, 156], #64209c
    "red_concrete": [142, 33, 33], #8e2121
    "red_sand": [191, 103, 33], #bf6721
    "sand": [219, 207, 163], #dbcfa3
    "white_concrete": [207, 213, 214], #cfd5d6
    "yellow_concrete": [241, 175, 21] #f1af15
}

im = Image.open(r"albo.png")

pixels = np.asarray(im)

square = np.empty([pixels.shape[0],pixels.shape[1]])

def RGBtoInt(rgb = [0,0,0]):
    return math.sqrt(math.pow(rgb[0],2)+math.pow(rgb[1],2)+math.pow(rgb[2],2))

def search(term):
    for name, search in blocks.items():
        if search == term:
            return name

def min(term = [0,0,0]):
    min = 999999999
    for block in blocks:
        if RGBtoInt(term) - RGBtoInt(blocks.get(block)) < min:
            min = RGBtoInt(term) - RGBtoInt(blocks.get(block))
    return min

for y in range(pixels.shape[0]):
    for x in range(pixels.shape[1]):
        square[y][x] = RGBtoInt(pixels[y][x])

build = np.empty([pixels.shape[0],pixels.shape[1]])

for y in range(pixels.shape[0]):
    for x in range(pixels.shape[1]):
            min(square[y][x])
            print(max)
            build[y][x] = search(max)

print(square[10][20])
print(build[10][20])

#print(pixels)
#im.show()