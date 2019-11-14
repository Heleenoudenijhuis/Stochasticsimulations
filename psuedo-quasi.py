import random
import sobol_seq
import matplotlib.pyplot as plt
import numpy as np

fig1, ax1 = plt.subplots(figsize=(15,10))
#ax1.set_title("Station: "+StaName+','+' Component: '+comp)
ax1.grid(True)


number = 200
#xp = []
#yp = []

q = sobol_seq.i4_sobol_generate(2, number)

for i in range(number):
    xp = np.random.rand(0,1)
    yp = np.random.rand(0,1)
    #plt.scatter(xp, yp)
    ax1.scatter(xp, yp, c='b')

plt.show()
print(xp)

