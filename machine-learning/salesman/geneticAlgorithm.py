import matplotlib.pyplot as plt
import numpy as np
from area import Area
import math
import random

class GeneticAlgorithm():

	def __init__(self, area: Area, populationSize: int, mutationPercent: float,
						successionRate: int, diversityRate: float, time: int, solution: int, 
						secondStage: bool, progress: int):
		self.area = area
		self.populationSize	= populationSize
		self.mutationPercent = mutationPercent
		self.successionRate	= successionRate
		self.diversityRate = diversityRate
		self.time = time
		self.solution = solution
		self.progress = progress
		
		self.numberOfBlocks	= area.numberOfBlocks
		self.secondStage = False
		self.populationPool	:np.array   = np.arange(0, populationSize)
		self.blocksPool		:np.array   = np.arange(0, self.numberOfBlocks)
		if time is not 0: self.solution = 1000
					
	def start(self):
		basePopulation = self.createBasePopulation()
		fitness = self.fitnessCalculation(basePopulation)
		Population = basePopulation[np.argsort(fitness)]
		elite = Population[0,:]
	
		history = []
		for generation in range(0,500):
			if generation == 20:
				self.secondStage = True
				self.successionRate = 4
				self.mutationPercent = 0.5
			Parents = self.succession(Population, elite)
			Mutated = self.mutation(Parents)
			NeighborMutation = self.neighborMutation(Parents)
			Reversed = self.reversalMutation(Parents, )
	
			newPopulation = np.concatenate((Mutated,NeighborMutation,Reversed))
			fitness = self.fitnessCalculation(newPopulation)
			Population = newPopulation[np.argsort(fitness)]
	
			if(len(history) is 0 or max(fitness) > history[-1]): 
				history.append(max(fitness))
				elite = Population[0,:]
			else: history.append(history[-1])
	
			print('Generation: {}, Solution: {}'.format(generation, history[-1]))
			if(len(history) > self.progress and history[-1] == history[-self.progress]):
				self.area.plotPath(Population[0,:])
				self.plotConvCurve(history)
				break

	def createBasePopulation(self):
		Population = np.empty((self.populationSize, self.numberOfBlocks+1), dtype=np.uint8)
		for p in range(0, self.populationSize):
			Population[p,0:self.numberOfBlocks] = np.random.choice(self.blocksPool, self.blocksPool.size, replace=False)
		Population[:,-1] = Population[:,0]
		return Population
		
	def fitnessCalculation(self, Population):
		sum=0;
		distance = np.empty([Population.shape[0]])
		for i in range(0,Population.shape[0]):
			for j in range(0, self.numberOfBlocks-1):
				sum = sum + self.area.distances[Population[i,j], Population[i,j+1]];
			distance[i]=sum;
			sum=0;
		return distance
		
	def succession(self, Population, elite):
		Population[self.successionRate, :] = elite
		idx = np.random.randint(self.successionRate, size=self.populationSize)
		Population = Population[0:self.populationSize,:][idx,:]
		# Diversity
		diversedIndividuals = np.random.choice(self.populationPool, math.ceil(self.populationSize * self.diversityRate), replace=False)
		for i in diversedIndividuals:
			Population[i,0:self.numberOfBlocks] = np.random.choice(self.blocksPool, self.blocksPool.size, replace=False)
		Population[:,-1] = Population[:,0]
		return Population
		
	def mutation(self, Parents):
		toMutate = np.random.choice(self.populationPool, math.ceil(self.populationSize * self.mutationPercent), replace=False)
		for j in toMutate:
			k = random.randint(2, self.numberOfBlocks-2)
			if random.random() > 0.5: 
				Parents[j,k], Parents[j,k+1]  = Parents[j,k+1], Parents[j,k]
			else:  
				Parents[j,k-1], Parents[j,k]  = Parents[j,k], Parents[j,k-1]  
		return Parents
	
	def neighborMutation(self, Parents):
		toMutate = np.random.choice(self.populationPool, math.ceil(self.populationSize * self.mutationPercent), replace=False)
		for j in toMutate:
				k = random.randint(1, self.numberOfBlocks-2)
				sortedNeigbours = np.argsort(self.area.distances[Parents[j,k],:])
				if (int(sortedNeigbours[1]) == int(Parents[j,0])): neigh = sortedNeigbours[2]
				else: neigh = sortedNeigbours[1]
				neighIndex = np.argwhere(Parents[j,:] == neigh)
				Parents[j,k], Parents[j, neighIndex] = Parents[j, neighIndex], Parents[j,k]
		return Parents
		
	def reversalMutation(self, Parents):
		toMutate = np.random.choice(self.populationPool, math.ceil(self.populationSize * self.mutationPercent), replace=False)
		for j in toMutate:
			reverseStart = random.randint(1, self.numberOfBlocks-1)
			reverseStop = random.randint(reverseStart, self.numberOfBlocks-1)
			if self.secondStage and reverseStop - reverseStart > 7:
				reverseStop = random.randint(reverseStart, reverseStart + random.randint(1,5))
			Parents[j, reverseStart:reverseStop]=np.flip(Parents[j, reverseStart:reverseStop],0)
		return Parents	
		
	def plotConvCurve(self, history):
		plt.plot(history)
		plt.show()
		#plt.savefig('Area/curve.png')
		
	def printParameters(self):
		items = self.__dict__.items()
		[print(f"Parameter: {k}     \tValue: {v}") for k, v in items]
		
		return items