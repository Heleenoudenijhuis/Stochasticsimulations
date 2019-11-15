import glob
import matplotlib.pyplot as plt
import copy
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
import random


def make_sketch():
	x = list(range(5))
	y = list(range(5))

	for el in range(5):
		i = random.choice(x)
		j = random.choice(y)
		x.remove(i)
		y.remove(j)
		plt.plot(i+random.random(),j+random.random(), 'ro')

	for i in range(6):
		plt.plot([0,5], [i,i], 'k')
		plt.plot([i,i], [0,5], 'k')
	plt.xticks([])
	plt.yticks([])
	plt.xlim(0,5)
	plt.ylim(0,5)
	plt.show()



def read_files(files):
	data = []
	darts = []
	mandel_iters = []
	for file in files:
		with open(file, 'r') as f:
			for line in f:
				line = line.strip().split(',')
				if float(line[3]) > 200:
					continue
				data.append([float(i) for i in line])
				if line[0] not in darts:
					darts.append(line[0])
				if line[1] not in mandel_iters:
					mandel_iters.append(line[1])
	darts = sorted([int(i) for i in darts])
	mandel_iters = sorted([int(i) for i in mandel_iters])
	return data, darts, mandel_iters

def plot3d(files):
	area = []
	duration = []
	plot_data = []

	data, darts, mandel_iters = read_files(files)




	for i in darts:
		for j in mandel_iters:
			wanted_data = list(filter(lambda x: x[0] == i and x[1] == j, data))
			average = np.average([i[2] for i in wanted_data])
			plot_data.append([i / 10000, j, average])


	fig = plt.figure()
	ax = fig.gca(projection='3d')


	for mandel_iter in mandel_iters:
		wanted_data = list(filter(lambda x: x[1] == mandel_iter, plot_data))
		wanted_data = sorted(wanted_data, key=lambda x: x[0])  
		x,y,z = zip(*wanted_data)
		ax.plot(x, y, z, 'ko-')

	for dart in darts:
		wanted_data = list(filter(lambda x: x[0] == dart / 10000, plot_data))
		wanted_data = sorted(wanted_data, key=lambda x: x[1])  
		x,y,z = zip(*wanted_data)
		ax.plot(x, y, z, 'ko-')



	plt.ylabel('Mandelbrot iterations', fontsize=15)
	plt.xlabel('Samples (x1000)', fontsize=15)
	ax.set_zlabel('Area', fontsize=15)
	plt.show()


def plot2d(files):
	exp = 4
	count = 0
	for file in files:
		data, darts, mandel_iters = read_files(file)
		mandel_iter = 200
		data = list(filter(lambda x: x[1] ==  mandel_iter, data))
		plot_data = []
		for i in darts:
			wanted_data = list(filter(lambda x: x[0] == i, data))
			values = [j[2] - 1.5065918849 for j in wanted_data]
			std = np.std(values) / (len(wanted_data) -1)**0.5
			average = np.average(values)
			plot_data.append([i/(10**exp), average ,std])
		x, y, error = zip(*plot_data)
		
		if count == 0:
			exp-=1
			# plt.errorbar(x,y, yerr=error, label='PRS')
		# if count == 1:
			# plt.errorbar(x,y, yerr=error, label='DRS')
		if count == 2:
			plt.errorbar(x,y, yerr=error, label='RLHC')
		if count == 3:
			plt.errorbar(x,y, yerr=error, label='MLHC')
		count+=1

	plt.legend()
	plt.xlabel('Samples (x1000)', fontsize=20)
	plt.ylabel(r'Difference in area ($\Delta$A)', fontsize=20)
	plt.xticks(fontsize=15)
	plt.yticks(fontsize=15)
	plt.grid()
	plt.show()


def area2d(files):
	exp = 4
	count = 0
	for file in files:
		data, darts, mandel_iters = read_files(file)
		# mandel_iter = [int(len(darts)/2+1)]
		# mandel_iter = 200
		dart = max(darts)
		data = list(filter(lambda x: x[0] ==  dart, data))
		max_area = list(filter(lambda x: x[1] == 200, data))
		area = np.average([i[2] for i in max_area])
		plot_data = []
		for i in mandel_iters:
			wanted_data = list(filter(lambda x: x[1] == i, data))
			values = [j[2] - area for j in wanted_data]
			std = np.std(values) / (len(wanted_data) -1)**0.5
			average = np.average(values)
			plot_data.append([i, average ,std])

		# for i in plot_data:
			# print(i)
		x, y, error = zip(*plot_data)
		if count == 0:
			exp-=1
			# plt.errorbar(x,y, yerr=error, label='PRS')
		# if count == 1:
			# plt.errorbar(x,y, yerr=error, label='DRS')
		if count == 2:
			plt.errorbar(x,y, yerr=error, label='RLHC')
		if count == 3:
			plt.errorbar(x,y, yerr=error, label='MLHC')
		count+=1



	plt.legend()
	plt.xlabel('Mandelbrot iterations', fontsize=20)
	plt.ylabel(r'Difference in area ($\Delta$A)', fontsize=20)
	plt.xticks(fontsize=15)
	plt.yticks(fontsize=15)
	plt.grid()
	plt.show()



hitandmiss_files = glob.glob('results/a*miss.txt')
random_files = glob.glob('results/*strat.txt')
random_latin = glob.glob('results/*m_l*0.txt')
median_latin = glob.glob('results/*n_l*0.txt')





# plot3d(random_latin)
# plot3d(median_latin)
# plot3d(hitandmiss_files)
# plot3d(random_files)

# area2d([hitandmiss_files, random_files, random_latin, median_latin])
plot2d([hitandmiss_files, random_files, random_latin, median_latin])
# plot2d([random_files])
# plot2d([random_latin])
# plot2d([median_latin])
# plot2d([hitandmiss_files])