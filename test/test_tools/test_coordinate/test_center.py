import unittest

from piperabm.tools.coordinate.center import center


class TestRotateFunction(unittest.TestCase):
    
    def test_0(self):
        pos_start = [0, 0]
        pos_end = [4, 4]
        pos_center = center(pos_start, pos_end)
        expected_result = [2, 2]
        self.assertAlmostEqual(pos_center, expected_result, places=5)


if __name__ == "__main__":
    unittest.main()