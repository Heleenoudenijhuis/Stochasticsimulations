#Mandelbrot generator
import numpy as np
from PIL import Image
import random
import os
import copy
import time



file = 'results/double_random.txt'
WIDTH = 3
HEIGHT = 3
XSTART = -2
YSTART = -1.5
intervals_grid = 10


square_width = WIDTH / intervals_grid
square_height = HEIGHT / intervals_grid
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


for mand_iters in range(10,201,10):
    for darts in range(10**4, 2*10**5+1, 10**4):
        for run in range(20):
            area_count = 0
            start = time.time()
            for i in range(darts):
                if not i % int(darts/10):
                    print('mand_iters', mand_iters, 'darts', darts, 'run', run, str(int(i/darts * 100)) + '%')
                i = random.randint(0, intervals_grid-1) * square_width
                j = random.randint(0, intervals_grid-1) * square_height
                x = XSTART + random.uniform(i, i + square_width)
                y = YSTART + random.uniform(j, j + square_height)
                if not calc(x,y, mand_iters):
                    area_count+=1

            duration = time.time() - start
            area_true = (area_count / darts) * area

            with open(file, 'a') as f:
                f.write(str(darts) + ',' + str(mand_iters) + ',' + str(area_true) + ',' + str(duration) + '\n')