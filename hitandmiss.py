#Mandelbrot generator
import numpy as np
from PIL import Image
import random
import os
import copy
import time



file = 'results/hitandmiss.txt'
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


for mand_iters in range(10,201,10):
    for darts in range(10**5, 2*10**6+1, 10**5):
        for run in range(20):
            start = time.time()
            area_count = 0
            for i in range(darts):
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





