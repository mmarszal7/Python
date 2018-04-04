import numpy as np
from area import Area
import math
import random

numberOfBlocks	:int    = 30
populationSize	:int    = 50
mutationPercent :float  = 0.2
successionRate	:int    = 10
diversityRate	:float  = 0.3
time			:int    = 0
solution		:int    = 0
secondStage		:bool   = False
area			:Area   = Area(numberOfBlocks)
populationPool	:np.array   = np.arange(0,populationSize)
blocksPool		:np.array   = np.arange(0,numberOfBlocks)

if time is not 0: solution = 1000

# Population - best individuals are on top
# ............................................................ #

def mutation(Parents):
	toMutate = np.random.choice(populationPool, math.ceil(populationSize * mutationPercent), replace=False)
	for j in toMutate:
		k = random.randint(2,numberOfBlocks-2)
		if random.random() > 0.5: 
			Parents[j,k], Parents[j,k+1]  = Parents[j,k+1], Parents[j,k]
		else:  
			Parents[j,k-1], Parents[j,k]  = Parents[j,k], Parents[j,k-1]  
	return Parents

def reversalMutation(Parents):
	toMutate = np.random.choice(populationPool, math.ceil(populationSize * mutationPercent), replace=False)
	for j in toMutate:
		reverseStart = random.randint(1,numberOfBlocks-1)
		reverseStop = random.randint(reverseStart,numberOfBlocks-1)
		if secondStage and reverseStop - reverseStart > 7:
			reverseStop = random.randint(reverseStart,reverseStart + random.randint(1,5))
		Parents[j,reverseStart:reverseStop]=np.flip(Parents[j,reverseStart:reverseStop],0)
	return Parents

def neighborMutation(Parents):
	toMutate = np.random.choice(populationPool, math.ceil(populationSize * mutationPercent), replace=False)
	for j in toMutate:
			k = random.randint(1,numberOfBlocks-2)
			sortedNeigbours = np.argsort(area.distances[Parents[j,k],:])
			if (int(sortedNeigbours[1]) == int(Parents[j,0])): neigh = sortedNeigbours[2]
			else: neigh = sortedNeigbours[1]
			neighIndex = np.argwhere(Parents[j,:]==neigh)
			Parents[j,k], Parents[j,neighIndex] = Parents[j,neighIndex], Parents[j,k]
	return Parents
		
def succession(Population, elite):
	Population[successionRate, :] = elite
	idx = np.random.randint(successionRate, size=populationSize)
	Population = Population[0:populationSize,:][idx,:]
	# Diversity
	diversedIndividuals = np.random.choice(populationPool, math.ceil(populationSize * diversityRate), replace=False)
	for i in diversedIndividuals:
		Population[i,0:numberOfBlocks] = np.random.choice(blocksPool, blocksPool.size, replace=False)
	Population[:,-1] = Population[:,0]
	return Population
		
def fitnessCalculation(Population):
	sum=0;
	distance = np.empty([Population.shape[0]])
	for i in range(0,Population.shape[0]):
		for j in range(0,numberOfBlocks-1):
			sum = sum + area.distances[Population[i,j],Population[i,j+1]];
		distance[i]=sum;
		sum=0;
	return distance

def createBasePopulation():
	Population = np.empty((populationSize,numberOfBlocks+1), dtype=np.uint8)
	for p in range(0, populationSize):
		Population[p,0:numberOfBlocks] = np.random.choice(blocksPool, blocksPool.size, replace=False)
	Population[:,-1] = Population[:,0]
	return Population

def recoverAreaFromCSV():
	from numpy import genfromtxt
	global area
	try:
		area = Area(numberOfBlocks)
		area.distances = genfromtxt('Area/Distances.csv', delimiter=',')
		area.sizes = genfromtxt('Area/Sizes.csv', delimiter=',')
		area.cords = genfromtxt('Area/Cords.csv', delimiter=',')
	except OSError as e:
		print(e)
	return None