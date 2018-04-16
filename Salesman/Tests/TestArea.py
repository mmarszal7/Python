import sys 
sys.path.append('..')
import unittest
import numpy as np
from area import Area
import time as timeasure

class TestArea(unittest.TestCase):

	def test_area_size(self):
		area = Area('draw', 10)
		
		self.assertEqual(area.numberOfBlocks, 10)
		self.assertEqual(area.cords.shape, (10,2))
		self.assertEqual(area.sizes.shape, (10,))
		self.assertEqual(area.distances.shape, (10,10))

	def test_area_calculateDistances(self):
		area = Area(5)
		area.saveArea()
		testArea = Area('file')
		
		self.assertEqual(testArea.numberOfBlocks, 5)
		self.assertEqual(testArea.cords.shape, (5,2))
		self.assertEqual(testArea.sizes.shape, (5,))
		self.assertEqual(testArea.distances.shape, (5,5))

if __name__ == '__main__':
	try:
		unittest.main()
		wait = input()
	except:
		wait = input()
