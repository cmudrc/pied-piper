import unittest
import numpy as np

from piperabm.tools.coordinate.slope import slope


class TestSlopeFunction_0(unittest.TestCase):

    def setUp(self) -> None:
        self.start_pos = [0, 0]

    def test_0(self):
        end_pos = [1, 0]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, 0, places=5)

    def test_1(self):
        end_pos = [0, 1]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, np.pi / 2, places=5)

    def test_2(self):
        end_pos = [-1, 0]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, np.pi, places=5)

    def test_3(self):
        end_pos = [0, -1]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, np.pi * 3 / 2, places=5)


class TestSlopeFunction_1(unittest.TestCase):

    def setUp(self) -> None:
        self.start_pos = [1, 0]

    def test_0(self):
        end_pos = [2, 0]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, 0, places=5)

    def test_1(self):
        end_pos = [1, 1]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, np.pi / 2, places=5)

    def test_2(self):
        end_pos = [0, 0]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, np.pi, places=5)

    def test_3(self):
        end_pos = [1, -1]
        angle = slope(self.start_pos, end_pos)
        self.assertAlmostEqual(angle, np.pi * 3 / 2, places=5)


if __name__ == "__main__":
    unittest.main()