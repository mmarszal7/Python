import unittest
import numpy as np
import area
import time as timeasure

class TestArea(unittest.TestCase):

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
