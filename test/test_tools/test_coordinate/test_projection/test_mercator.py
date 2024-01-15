import unittest

from piperabm.tools.coordinate.projection.mercator import Mercator


class TestMercatorClass(unittest.TestCase):

    def test_mercator_projection(self):
        latitude = 0
        longitude = 0
        radius = 1
        x, y = Mercator.project(latitude, longitude, radius)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)

    def test_inverse_mercator_projection(self):
        x = 0
        y = 0
        radius = 1
        latitude, longitude = Mercator.inverse(x, y, radius)
        self.assertAlmostEqual(latitude, 0, places=2)
        self.assertAlmostEqual(longitude, 0, places=2)


if __name__ == '__main__':
    unittest.main()