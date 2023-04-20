import unittest
import numpy as np

from piperabm.tools.coordinate.rotate import rotate_coordinate


class TestRotateCoordinateFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.pos = [1, 0]

    def test_0(self):
        angle = 0
        new_pos = rotate_coordinate(self.pos, angle)
        expected = [1, 0]
        self.assertAlmostEqual(new_pos[0], expected[0], places=5)
        self.assertAlmostEqual(new_pos[1], expected[1], places=5)

    def test_1(self):
        angle = np.pi / 2
        new_pos = rotate_coordinate(self.pos, angle)
        expected = [0, -1]
        self.assertAlmostEqual(new_pos[0], expected[0], places=5)
        self.assertAlmostEqual(new_pos[1], expected[1], places=5)

    def test_2(self):
        angle = np.pi
        new_pos = rotate_coordinate(self.pos, angle)
        expected = [-1, 0]
        self.assertAlmostEqual(new_pos[0], expected[0], places=5)
        self.assertAlmostEqual(new_pos[1], expected[1], places=5)

    def test_3(self):
        angle = np.pi * 3 / 2
        new_pos = rotate_coordinate(self.pos, angle)
        expected = [0, 1]
        self.assertAlmostEqual(new_pos[0], expected[0], places=5)
        self.assertAlmostEqual(new_pos[1], expected[1], places=5)


if __name__ == "__main__":
    unittest.main()