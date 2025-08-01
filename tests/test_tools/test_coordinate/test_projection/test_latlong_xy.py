import unittest
from piperabm.tools.coordinate.projection.latlong_xy import latlong_xy, xy_latlong


class TestLatlongXY(unittest.TestCase):

    def test_latlong_xy(self):
        latitude_0 = 70
        longitude_0 = -150
        x, y = latlong_xy(latitude_0, longitude_0, latitude_0, longitude_0)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)
        latitude = latitude_0 + 1
        longitude = longitude_0 + 1
        x, y = latlong_xy(latitude_0, longitude_0, latitude, longitude)
        self.assertAlmostEqual(x, 36245.207676322, places=2)
        self.assertAlmostEqual(y, 111620.02680148499, places=2)

    def test_xy_latlong(self):
        latitude_0 = 70
        longitude_0 = -150
        latitude, longitude = xy_latlong(latitude_0, longitude_0, 0, 0)
        self.assertAlmostEqual(latitude, latitude_0, places=2)
        self.assertAlmostEqual(longitude, longitude_0, places=2)
        x = 36245.207676322
        y = 111620.02680148499
        latitude, longitude = xy_latlong(latitude_0, longitude_0, x, y)
        self.assertAlmostEqual(latitude, latitude_0 + 1, places=2)
        self.assertAlmostEqual(longitude, longitude_0 + 1, places=2)


if __name__ == "__main__":
    unittest.main()