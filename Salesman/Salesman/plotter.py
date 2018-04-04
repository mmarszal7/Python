import matplotlib.pyplot as plt
import seaborn
from numpy import genfromtxt
import numpy as np

def plotArea(solutionToPlot = None):

	area = readCSV()
	if area is None or solutionToPlot is None: return None

	fig, ax = plt.subplots()
	fig.canvas.set_window_title('Salesman Area')

	ax.scatter(area[:,0], area[:,1], area[:,2]*10, 'pink')
	for i, txt in enumerate(area[:,2]):
		ax.annotate(i+1, (area[:,0][i],area[:,1][i]), horizontalalignment='r', fontsize=16, fontweight='bold') # str = str(area[:,2][i])
	for path in range(0,area[:,1].shape[0]):
		ax.plot([area[solutionToPlot[path],0], area[solutionToPlot[path+1],0]], [area[solutionToPlot[path],1], area[solutionToPlot[path+1],1]], 'k-')

	plt.axis([0,1000,0,1000])
	plt.title('Salesman Area')
	#plt.xlabel('')
	#plt.ylabel('')
	#plt.legend(loc='lower left')
	plt.tight_layout()
	plt.show()
	#plt.savefig('Area/plot.png')
	plt.close()

def readCSV():
	try:
		sizes = genfromtxt('Area/Sizes.csv', delimiter=',')
		cords = genfromtxt('Area/Cords.csv', delimiter=',')

		area = np.empty([cords.shape[0],cords.shape[1]+1])
		area[:,0:2] = cords
		area[:,2] = sizes
		return area
	except OSError as e:
		print(e)
	return None

def plotConvCurve(history):
	plt.plot(history)
	plt.show()
	#plt.savefig('Area/curve.png')
	plt.close()
