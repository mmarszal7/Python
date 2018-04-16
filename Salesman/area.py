import numpy as np
import csv
from scipy.spatial.distance import euclidean

sizeX = 1000
sizeY = 1000

class Area():
	   
	def __init__(self, numberOfBlocks):
		self.numberOfBlocks = numberOfBlocks
		self.cords = self.drawCords()
		self.sizes = self.drawSizes()
		self.distances = self.calculateDistances()
		self.saveArea()
		
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
		with open('Area/Distances.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(self.distances)
		with open('Area/Sizes.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(self.sizes)
		with open('Area/Cords.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(self.cords)

	def toString(self):
		print("{} \n\n {} \n\n {}".format(self.sizes, self.cords, self.distances))