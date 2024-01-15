import unittest

from piperabm.tools.coordinate.projection.latlong_xyz import latlong_xyz, xyz_latlong


class TestLatLongXYZFunction(unittest.TestCase):

    def test_latlong_xyz(self):
        latitude = 0
        longitude = 0
        vector = latlong_xyz(latitude, longitude)
        self.assertListEqual(list(vector), [1, 0, 0])


class TestXYZLatLongFunction(unittest.TestCase):

    def test_xyz_latlong(self):
        vector = [1, 0, 0]
        latitude, longitude = xyz_latlong(vector)
        self.assertEqual(latitude, 0)
        self.assertEqual(longitude, 0)


if __name__ == '__main__':
    unittest.main()