import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import numpy as np
from numpy import genfromtxt
import csv
import os

sizeX = 1000
sizeY = 1000

class Area():
	
	def __init__(self, source = '', numberOfBlocks = 5):
		self.numberOfBlocks = numberOfBlocks;
		if (source == 'file'):
			self.recoverAreaFromFile()
		else:
			self.drawArea();
		self.saveArea()
		
	def recoverAreaFromFile(self):
		try:
			self.cords = genfromtxt('Area/Cords.csv', delimiter=',')
			self.sizes = genfromtxt('Area/Sizes.csv', delimiter=',')
			self.distances = genfromtxt('Area/Distances.csv', delimiter=',')
			self.numberOfBlocks = len(self.sizes);
		except OSError as e:
			print("Could not find csv file, drawing area...")
			self.drawArea()
		
	def drawArea(self):
		self.cords = self.drawCords()
		self.sizes = self.drawSizes()
		self.distances = self.calculateDistances()

	def drawCords(self):
		cords = np.empty([self.numberOfBlocks,2])
		cords = np.column_stack((np.random.choice(range(1,1001), self.numberOfBlocks,  replace=False), np.random.choice(range(1,1001), self.numberOfBlocks, replace=False)))
		return cords
	
	def drawSizes(self):
		sizes = np.empty([1, self.numberOfBlocks])
		sizes = np.random.choice(range(1,101), self.numberOfBlocks)
		return sizes
	
	def calculateDistances(self):
		distances = np.empty([self.numberOfBlocks, self.numberOfBlocks])
		for x in range(0, self.cords.shape[0]):
			for y in range(0, self.cords.shape[0]):
				distances[x,y] = euclidean(self.cords[x,:], self.cords[y,:])
		return distances
			
	def saveArea(self):
		if not os.path.exists('Area'):
			os.makedirs('Area')
		with open('Area/Distances.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(self.distances)
		with open('Area/Sizes.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(self.sizes)
		with open('Area/Cords.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(self.cords)
			
	def plotPath(self, solutionToPlot):
		area = np.empty([self.cords.shape[0], self.cords.shape[1]+1])
		area[:,0:2] = self.cords
		area[:,2] = self.sizes
		
		fig, ax = plt.subplots()
		fig.canvas.set_window_title('Salesman Area')
	
		ax.scatter(area[:,0], area[:,1], area[:,2]*10, 'pink')
		for i, txt in enumerate(area[:,2]):
			ax.annotate(i+1, (area[:,0][i],area[:,1][i]), horizontalalignment='r', fontsize=16, fontweight='bold') # str = str(area[:,2][i])
		for path in range(0, area[:,1].shape[0]):
			ax.plot([area[solutionToPlot[path],0], area[solutionToPlot[path+1],0]], [area[solutionToPlot[path],1], area[solutionToPlot[path+1],1]], 'k-')
	
		plt.axis([0, 1000, 0, 1000])
		plt.title('Salesman Area')
		plt.tight_layout()
		plt.show()

	def toString(self):
		print("{} \n\n {} \n\n {}".format(self.sizes, self.cords, self.distances))
		
