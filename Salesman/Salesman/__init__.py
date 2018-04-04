''' 
TODO: 
- Tests
'''
import geneticAlgorithm as ga
import plotter
from threading import Thread
import numpy as np

progress :int = 50

if __name__ == '__main__':  
	basePopulation = ga.createBasePopulation()
	ga.recoverAreaFromCSV() # working only when desired area size equals saved area size
	fitness = ga.fitnessCalculation(basePopulation)
	Population = basePopulation[np.argsort(fitness)]
	elite = Population[0,:]

	history = []
	for generation in range(0,500):
		if generation == 20:
			ga.secondStage = True
			ga.successionRate = 4
			ga.mutationPercent = 0.5
		Parents = ga.succession(Population, elite)
		Mutated = ga.mutation(Parents)
		NeighborMutation = ga.neighborMutation(Parents)
		Reversed = ga.reversalMutation(Parents, )

		newPopulation = np.concatenate((Mutated,NeighborMutation,Reversed))
		fitness = ga.fitnessCalculation(newPopulation)
		Population = newPopulation[np.argsort(fitness)]

		if(len(history) is 0 or max(fitness) > history[-1]): 
			history.append(max(fitness))
			elite = Population[0,:]
		else: history.append(history[-1])

		print('Generation: {}, Solution: {}'.format(generation, history[-1]))
		if(len(history) > progress and history[-1] == history[-progress]):
			plotter.plotArea(Population[0,:])
			plotter.plotConvCurve(history)
			break