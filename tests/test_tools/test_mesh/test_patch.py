import unittest
from piperabm.tools.mesh.triangle import Triangle
from piperabm.tools.mesh.patch import Patch


class TestPatch(unittest.TestCase):

    def test_patch(self):
        point_1 = [0, 0]
        point_2 = [1, 0]
        point_3 = [0, 1]
        density = 1
        triangle_1 = Triangle(point_1, point_2, point_3, density)
        point_4 = [0, 0]
        point_5 = [1, 0]
        point_6 = [0, 1]
        density = 1
        triangle_2 = Triangle(point_4, point_5, point_6, density)
        patch = Patch()
        patch.add(triangle_1, triangle_2)
        point = patch.random_point()
        # Is in?
        self.assertTrue(point[0] < point_2[0])
        self.assertTrue(point[1] < point_3[1])


if __name__ == "__main__":
    unittest.main()
