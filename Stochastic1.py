#Mandelbrot generator
import numpy as np
from PIL import Image
import random
import os
import copy


PIXEL_SCALE = 200
WIDTH = 3
HEIGHT = 3
XSTART = -2
YSTART = -1.5

image_width = int(PIXEL_SCALE*WIDTH)
image_height = int(PIXEL_SCALE*HEIGHT)
count2 = 0
pixels = image_height * image_width
mandelbrot_iterations = 50
iterations = 1 * pixels

print('Vergeet de file niet aan te passen naar heleen ipv alwan')
file = 'results/alwan.txt'

def calc(c1, c2, iterations):
    x = y = 0
    for i in range(iterations):
        x, y = x*x - y*y + c1, 2*x*y + c2
        if x*x + y*y > 4:
            return i+1
    return 0



#Hit and miss algorithm
def hitandmiss(iterations):
    count = 0
    for k in range(iterations):
        randomh = random.randrange(0, image_height)
        randomw = random.randrange(0, image_width)

        if np.all(array[randomh, randomw,] == 0):
            count += 1
        array[randomh, randomw,] = (255,69,0)

    # img2 = Image.fromarray(array)
    # img2.show()
    return count




if not os.path.exists('results'):
    os.mkdir('results')

if not os.path.exists(file):
    with open(file, 'w') as f:
        f.write('')

array = np.zeros((image_height,
                  image_width,
                  3),
                 dtype=np.uint8)
for i in range(image_width):
    c1 = XSTART + i/PIXEL_SCALE
    for j in range(image_height):
        c2 = YSTART + j/PIXEL_SCALE
        v = calc(c1, c2, mandelbrot_iterations)
        if v:
            array[j, i,] = (255, 255, 255)
            count2 += 1
# img = Image.fromarray(array)
# img.show()

mandelbrot_array = copy.deepcopy(array)

for run in range(6):
    array = copy.deepcopy(mandelbrot_array)




    #Statistical analysis
    area = hitandmiss(iterations)

    #Calculating values
    fraction_hitmiss = area / pixels
    area_true = pixels - count2
    fraction_true = area_true / pixels
    with open(file, 'a') as save_file:
        save_file.write(str(pixels) + ',' + str(mandelbrot_iterations) + ',' + str(iterations) 
             + ',' + str(area) + ',' + str(area_true) + ',' + str(fraction_true) + '\n')

