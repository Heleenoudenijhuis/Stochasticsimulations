import glob
import matplotlib.pyplot as plt

files = glob.glob('results_heleen/*.txt')

data = []

for file in files:
	henk = {}
	with open(file, 'r') as f:
		for line in f:
			line = line.strip().split(',')
			henk['pixels'] = float(line[0])
			henk['mandelbrot_iterations'] = float(line[1])
			henk['iterations'] = float(line[2])
			henk['factor'] = float(line[2]) / float(line[0])
			henk['area'] = float(line[3])
			henk['area_true'] = float(line[4])
			henk['fraction_true'] = float(line[5])
			henk['pixel_scale'] = float(line[0]) / 9
			if len(line) > 5:
				henk['duration'] = float(line[6])
			data.append(henk)


pixel_scale = list(set([i['pixel_scale'] for i in data]))

print(pixel_scale)

