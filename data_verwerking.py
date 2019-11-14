import glob
import matplotlib.pyplot as plt
import copy
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time


def plot(files):
	data = []
	mandel_iters = []
	darts = []
	area = []
	duration = []
	plot_data = []


	for file in files:
		print(file)
		with open(file, 'r') as f:
			for line in f:
				line = line.strip().split(',')
				# if float(line[2]) < 1:
					# continue
				data.append([float(i) for i in line])
				if line[0] not in darts:
					darts.append(line[0])
				if line[1] not in mandel_iters:
					mandel_iters.append(line[1])


	mandel_iters = sorted([int(i) for i in mandel_iters])
	darts = sorted([int(i) for i in darts])

	for i in darts:
		for j in mandel_iters:
			wanted_data = list(filter(lambda x: x[0] == i and x[1] == j, data))
			average = np.average([i[2] for i in wanted_data])
			plot_data.append([i / 1000, j, average])


	fig = plt.figure()
	ax = fig.gca(projection='3d')


	for mandel_iter in mandel_iters:
		wanted_data = list(filter(lambda x: x[1] == mandel_iter, plot_data))
		wanted_data = sorted(wanted_data, key=lambda x: x[0])  
		x,y,z = zip(*wanted_data)
		print(np.average(z))
		ax.plot(x, y, z, 'ko-')

	for dart in darts:
		wanted_data = list(filter(lambda x: x[0] == dart / 1000, plot_data))
		wanted_data = sorted(wanted_data, key=lambda x: x[1])  
		x,y,z = zip(*wanted_data)
		ax.plot(x, y, z, 'ko-')



	plt.ylabel('Mandelbrot iterations')
	plt.xlabel('Darts (x1000)')
	ax.set_zlabel('Area')
	plt.show()

hitandmiss_files = glob.glob('results/*miss.txt')
random_files = glob.glob('results/*strat.txt')
random_latin = glob.glob('results/*m_l*.txt')
median_latin = glob.glob('results/*n_l*.txt')



# plot(random_latin)
# plot(median_latin)

plot(random_files)
plot(hitandmiss_files)