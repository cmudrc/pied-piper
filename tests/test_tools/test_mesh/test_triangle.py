import unittest
from piperabm.tools.mesh.triangle import Triangle


class TestTriangle(unittest.TestCase):

    def test_triangle(self):
        point_1 = [0, 0]
        point_2 = [1, 0]
        point_3 = [0, 1]
        density = 1
        triangle = Triangle(point_1, point_2, point_3, density)
        point = triangle.random_point()
        # Is in?
        self.assertTrue(point[0] < point_2[0])
        self.assertTrue(point[1] < point_3[1])


if __name__ == "__main__":
    unittest.main()
