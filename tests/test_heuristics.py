import unittest
from src.search_algorithms.manhattan_distance import ManhattanDistance
from src.search_algorithms.euclidian_distance import EuclidianDistance

from src.environment.Goal import Goal

class TestHeuristics(unittest.TestCase):
    def test_manhattan(self):
        self.assertEqual(ManhattanDistance.get_h(1,1,1,2), 1, "Distance should be 1")

    def test_euclidian(self):
        self.assertEqual(EuclidianDistance.get_h(1,1,1,3), 2, "Distance should be 2")

if __name__ == '__main__':
    unittest.main()