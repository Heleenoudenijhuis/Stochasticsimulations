#HOOOI


#Mandelbrot generator
import numpy as np
from PIL import Image
import random


PIXEL_SCALE = 200
WIDTH = 3
HEIGHT = 3
XSTART = -2
YSTART = -1.5

image_width = int(PIXEL_SCALE*WIDTH)
image_height = int(PIXEL_SCALE*HEIGHT)
count2 = 0

def calc(c1, c2):
    x = y = 0
    for i in range(50):
        x, y = x*x - y*y + c1, 2*x*y + c2
        if x*x + y*y > 4:
            return i+1
    return 0

array = np.zeros((image_height,
                  image_width,
                  3),
                 dtype=np.uint8)

for i in range(image_width):
    c1 = XSTART + i/PIXEL_SCALE
    for j in range(image_height):
        c2 = YSTART + j/PIXEL_SCALE
        v = calc(c1, c2)
        if v:
            array[j, i,] = (255, 255, 255)
            count2 += 1

img = Image.fromarray(array)
img.show()



#Hit and miss algorithm
def hitandmiss(iterations):
    count = 0
    for k in range(iterations):
        randomh = random.randrange(0, image_height)
        randomw = random.randrange(0, image_width)

        if np.all(array[randomh, randomw,] == 0):
            count += 1
        array[randomh, randomw,] = (255,69,0)

    img2 = Image.fromarray(array)
    img2.show()
    return count



#Statistical analysis
area = hitandmiss(1000000)

#Calculating values
area_image = image_height * image_width
fraction_hitmiss = area / area_image
area_true = area_image - count2
fraction_true = area_true / area_image

print(fraction_hitmiss, fraction_true)

