import unittest

from piperabm.tools.coordinate import rotate


class TestRotateClass(unittest.TestCase):

    def setUp(self) -> None:
        self.pos = [1, 1, 1]

    def test_x(self):
        angle = 0
        pos = rotate.x(self.pos, angle, ndarray=False)
        expected = [1, 1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 90
        pos = rotate.x(self.pos, angle, ndarray=False)
        expected = [1, 1, -1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 180
        pos = rotate.x(self.pos, angle, ndarray=False)
        expected = [1, -1, -1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 270
        pos = rotate.x(self.pos, angle, ndarray=False)
        expected = [1, -1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

    def test_y(self):
        angle = 0
        pos = rotate.y(self.pos, angle, ndarray=False)
        expected = [1, 1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 90
        pos = rotate.y(self.pos, angle, ndarray=False)
        expected = [-1, 1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 180
        pos = rotate.y(self.pos, angle, ndarray=False)
        expected = [-1, 1, -1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 270
        pos = rotate.y(self.pos, angle, ndarray=False)
        expected = [1, 1, -1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

    def test_z(self):
        angle = 0
        pos = rotate.z(self.pos, angle, ndarray=False)
        expected = [1, 1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 90
        pos = rotate.z(self.pos, angle, ndarray=False)
        expected = [1, -1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 180
        pos = rotate.z(self.pos, angle, ndarray=False)
        expected = [-1, -1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)

        angle = 270
        pos = rotate.z(self.pos, angle, ndarray=False)
        expected = [-1, 1, 1]
        self.assertAlmostEqual(pos[0], expected[0], places=5)
        self.assertAlmostEqual(pos[1], expected[1], places=5)
        self.assertAlmostEqual(pos[2], expected[2], places=5)


if __name__ == '__main__':
    unittest.main()