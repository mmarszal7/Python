import unittest
import geneticAlgorithm as ga
import numpy as np
import area
import time as timeasure

# Arrange-Act-Assert
population = ga.createBasePopulation()
for i in range(0,ga.populationSize):
	population[i,:-1] = ga.blocksPool
	population[i,-1] = 0

class TestGA(unittest.TestCase):

	def test_generateBasePopulation(self):
		start = timeasure.time()
		basePopulation = ga.createBasePopulation()
		end = timeasure.time()
		print('gaConstructor: {}s'.format(end - start))

		self.assertEqual(basePopulation.shape[1], ga.numberOfBlocks + 1 )
		self.assertEqual(basePopulation.shape[0], ga.populationSize)
		self.assertEqual(sum(basePopulation[:,-1]), sum(basePopulation[:,0]))
		self.assertEqual(sum(sum(basePopulation[:,:-1])), sum(list(range(0,ga.numberOfBlocks))) * ga.populationSize)

	def test_fitnessCalculation(self):
		start = timeasure.time()
		Population = ga.fitnessCalculation(population)
		end = timeasure.time()
		print('fitnessCalculation: {}s'.format(end - start))

		self.assertEqual(2, 2)

	#def test_succession(self):
	#	pass
	#
	#def test_mutation(self):
	#	pass

	def test_area_arraySizes(self):
		newArea = area.Area(ga.numberOfBlocks)
		
		self.assertEqual(newArea.cords.shape[1], 2)
		self.assertEqual(newArea.cords.shape, (ga.numberOfBlocks,2))
		self.assertEqual(newArea.sizes.shape, (ga.numberOfBlocks,))

	def test_area_calculateDistances(self):
		newArea = area.Area(ga.numberOfBlocks)
		newArea.cords = np.array([[1, 1],[1, 5]])

		start = timeasure.time()
		newArea.distances = area.calculateDistances(ga.numberOfBlocks, newArea.cords)
		end = timeasure.time()
		print('calculateDistances: {}s'.format(end - start))

		self.assertEqual(newArea.distances[0,1], 4.0 )

if __name__ == '__main__':
	try:
		unittest.main()
		wait = input()
	except:
		wait = input()
