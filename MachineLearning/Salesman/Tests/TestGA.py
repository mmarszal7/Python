import sys 
sys.path.append('..')
import unittest
from geneticAlgorithm import GeneticAlgorithm
from area import Area
import numpy as np

numberOfBlocks	:int    = 10
populationSize	:int    = 50
mutationPercent :float  = 0.2
successionRate	:int    = 10
diversityRate	:float  = 0.3
time			:int    = 0
solution		:int    = 0
secondStage		:bool   = False
progress 		:int = 50

class TestGA(unittest.TestCase):

	def test_generateBasePopulation(self):
		area = Area('draw', numberOfBlocks)
		ga = GeneticAlgorithm(area, populationSize, mutationPercent,
								successionRate, diversityRate, time, solution, 
								secondStage, progress)
								
		basePopulation = ga.createBasePopulation()

		self.assertEqual(basePopulation.shape, (ga.populationSize, ga.area.numberOfBlocks + 1))
		self.assertEqual(sum(basePopulation[-1,:-1]), sum(basePopulation[0,:-1]))
		self.assertEqual(sum(basePopulation[0,:-1]), sum(range(0, ga.area.numberOfBlocks)))
		self.assertEqual(sum(np.sum(basePopulation[:,:-1], axis=1)), sum(range(0, ga.area.numberOfBlocks)) * ga.populationSize)

if __name__ == '__main__':
	try:
		unittest.main()
		wait = input()
	except:
		wait = input()
