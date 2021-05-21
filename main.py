from PIL import Image
import numpy as np

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

for block in blocks:
    print(np.dot(blocks.get(block),blocks.get(block)))

#print(pixels)
#print(pixels.shape)



#im.show()