from geneticAlgorithm import GeneticAlgorithm
from area import Area
import numpy as np

numberOfBlocks	:int    = 30
populationSize	:int    = 150
mutationPercent :float  = 0.5
successionRate	:int    = 10
diversityRate	:float  = 0.5
time			:int    = 0
solution		:int    = 0
secondStage		:bool   = False
progress 		:int = 100

if __name__ == '__main__':
	area = Area('file')
	area = Area('draw', 25)
	ga = GeneticAlgorithm(area, populationSize, mutationPercent,
							successionRate, diversityRate, time, solution, 
							secondStage, progress)
	#ga.printParameters()
	ga.start();
							
	