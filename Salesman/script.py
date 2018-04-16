from geneticAlgorithm import GeneticAlgorithm
from area import Area
import numpy as np

numberOfBlocks	:int    = 30
populationSize	:int    = 50
mutationPercent :float  = 0.2
successionRate	:int    = 10
diversityRate	:float  = 0.3
time			:int    = 0
solution		:int    = 0
secondStage		:bool   = False
progress 		:int = 50

if __name__ == '__main__':
	area = Area('file')
	ga = GeneticAlgorithm(area, populationSize, mutationPercent,
							successionRate, diversityRate, time, solution, 
							secondStage, progress)
	#ga.printParameters()
	ga.start();
							
	