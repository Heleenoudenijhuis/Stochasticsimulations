#Mandelbrot generator
import numpy as np
from PIL import Image
import random
import os
import copy
import time



file = 'results/alwan_hitandmiss.txt'
WIDTH = 3
HEIGHT = 3
XSTART = -2
YSTART = -1.5

area = WIDTH * HEIGHT

def calc(c1, c2, iterations):
    x = y = 0
    for i in range(iterations):
        x, y = x*x - y*y + c1, 2*x*y + c2
        if x*x + y*y > 4:
            return i+1
    return 0


if not os.path.exists('results'):
    os.mkdir('results')

if not os.path.exists(file):
    with open(file, 'w') as f:
        f.write('')




for mand_iters in range(10,210,10):
    for darts in range(10**5, 2*10**6+1, 10**5):
        for run in range(20):
            for i in range(darts):
                area_count = 0
                start = time.time()
                if not i % int(darts/10):
                    print('mand_iters', mand_iters, 'darts', darts, 'run', run, str(int(i/darts * 100)) + '%')
                x = XSTART + random.uniform(0,WIDTH)
                y = YSTART + random.uniform(0,HEIGHT)
                if not calc(x,y, mand_iters):
                    area_count+=1

            duration = time.time() - start
            area_true = (area_count / darts) * area

            with open(file, 'a') as f:
                f.write(str(darts) + ',' + str(mand_iters) + ',' + str(area_true) + ',' + str(duration) + '\n')







#Hit and miss algorithm
# def hitandmiss(iterations):
#     count = 0
#     for k in range(iterations):
#         randomh = random.randrange(0, image_height)
#         randomw = random.randrange(0, image_width)

#         if np.all(array[randomh, randomw,] == 0):
#             count += 1
#         array[randomh, randomw,] = (255,69,0)

#     # img2 = Image.fromarray(array)
#     # img2.show()
#     return count




# for PIXEL_SCALE in range(1800, 2000, 100):


#     image_width = int(PIXEL_SCALE*WIDTH)
#     image_height = int(PIXEL_SCALE*HEIGHT)
#     pixels = image_height * image_width
#     for c in np.arange(2,3):
#         iterations = int(c * pixels)
#         for mandelbrot_iterations in range(50, 51, 1): 
#             count2 = 0



#             array = np.zeros((image_height,
#                               image_width,
#                               3),
#                              dtype=np.uint8)
#             for i in range(image_width):
#                 c1 = XSTART + i/PIXEL_SCALE
#                 for j in range(image_height):
#                     c2 = YSTART + j/PIXEL_SCALE
#                     v = calc(c1, c2, mandelbrot_iterations)
#                     if v:
#                         array[j, i,] = (255, 255, 255)
#                         count2 += 1
#             # img = Image.fromarray(array)
#             # img.show()

#             mandelbrot_array = copy.deepcopy(array)

#             for run in range(20):
#                 start = time.time()
#                 array = copy.deepcopy(mandelbrot_array)




#             #Statistical analysis
#                 area = hitandmiss(iterations)

#                 #Calculating values
#                 fraction_hitmiss = area / pixels
#                 area_true = pixels - count2
#                 fraction_true = area_true / pixels
#                 duration = time.time() - start
#                 with open(file, 'a') as save_file:
#                     save_file.write(str(pixels) + ',' + str(mandelbrot_iterations) + ',' + str(iterations) 
#                          + ',' + str(area) + ',' + str(area_true) + ',' + str(fraction_true) + ',' + str(round(duration,2)) + '\n')

#                 print('pixel: ', PIXEL_SCALE, 'mandel iter: ', mandelbrot_iterations, 'run: ', run, duration)
