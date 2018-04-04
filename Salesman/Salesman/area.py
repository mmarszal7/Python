import numpy as np
import csv
from scipy.spatial.distance import euclidean

sizeX = 1000
sizeY = 1000

class Area():
	   
	distances:	np.empty
	sizes:		np.empty
	cords:		np.empty

	def __init__(self, numberOfBlocks):
		self.cords = drawCords(numberOfBlocks)
		self.sizes = drawSizes(numberOfBlocks)
		self.distances = calculateDistances(numberOfBlocks, self.cords)
		saveEstate(self.cords, self.sizes, self.distances)
		
def drawCords(numberOfBlocks):
	cords = np.empty([numberOfBlocks,2])
	cords = np.column_stack((np.random.choice(range(1,1001), numberOfBlocks,  replace=False), np.random.choice(range(1,1001), numberOfBlocks, replace=False)))
	return cords

def drawSizes(numberOfBlocks):
	sizes = np.empty([1,numberOfBlocks])
	sizes = np.random.choice(range(1,101),numberOfBlocks)
	return sizes

def calculateDistances(numberOfBlocks, cords):
	distances = np.empty([numberOfBlocks, numberOfBlocks])
	for x in range(0,cords.shape[0]):
		for y in range(0,cords.shape[0]):
			distances[x,y] = euclidean(cords[x,:],cords[y,:])
	return distances
		
def saveEstate(cords, sizes, distances):
	with open('Area/Distances.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(distances)
	with open('Area/Sizes.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(sizes)
	with open('Area/Cords.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(cords)
	#pass

def toString():
	print("{} \n\n {} \n\n {}".format(sizes, cords, distances))