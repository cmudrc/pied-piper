import unittest

from piperabm.tools.distance import euclidean_distance


class TestRotateFunction(unittest.TestCase):
    
    def test_0(self):
        pos_start = [0, 3]
        pos_end = [4, 0]
        distance = euclidean_distance(pos_start, pos_end)
        expected_result = 5
        self.assertAlmostEqual(distance, expected_result, places=5)

    def test_1(self):
        pos_start = [0, 0]
        pos_end = [0, 0]
        distance = euclidean_distance(pos_start, pos_end)
        expected_result = 0
        self.assertAlmostEqual(distance, expected_result, places=5)


if __name__ == "__main__":
    unittest.main()