import unittest

from piperabm.tools.coordinate.projection.latlong_xy import latlong_xy, xy_latlong


class TestLatLongXYFunction(unittest.TestCase):

    def test_latlong_xy(self):
        latitude_0 = 0
        longitude_0 = 0

        latitude = latitude_0
        longitude = longitude_0

        x, y = latlong_xy(latitude_0, longitude_0, latitude, longitude)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)


class TestXYLatLongFunction(unittest.TestCase):

    def test_xy_latlong(self):
        latitude_0 = 0
        longitude_0 = 0

        x = 0
        y = 0

        latitude, longitude = xy_latlong(latitude_0, longitude_0, x, y)
        self.assertAlmostEqual(latitude, 0, places=2)
        self.assertAlmostEqual(longitude, 0, places=2)


if __name__ == '__main__':
    unittest.main()