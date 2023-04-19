import unittest

from piperabm.boundary import Rectangular
from piperabm.boundary.samples.rectangular import rectangular_1 as rectangular


class TestRectangularClass(unittest.TestCase):
    
    def setUp(self):
        self.rectangular = rectangular
        self.center = [30, 40]
    
        self.pos_0 = [36, 40]
        self.pos_1 = [36, 42]
        self.pos_2 = [36, 44]

    def test_is_in_0(self):
        pos = self.pos_0
        center = self.center
        self.assertTrue(self.rectangular.is_in(pos, center))

    def test_is_in_1(self):
        pos = self.pos_1
        center = self.center
        self.assertFalse(self.rectangular.is_in(pos, center))

    def test_is_in_2(self):
        pos = self.pos_2
        center = self.center
        self.assertFalse(self.rectangular.is_in(pos, center))

    def test_random_pos(self):
        center = self.center
        pos = self.rectangular.rand_pos(center)
        self.assertTrue(self.rectangular.is_in(pos, center))

    def test_distance_0(self):
        pos = self.pos_0
        distance = self.rectangular.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 6, places=5)
        distance = self.rectangular.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, -1.0710678, places=5)

    def test_distance_1(self):
        pos = self.pos_1
        distance = self.rectangular.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance**2, 6**2 + 2**2, places=5)
        distance = self.rectangular.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, 0.734385, places=5)

    def test_distance_2(self):
        pos = self.pos_2
        distance = self.rectangular.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 7.21110, places=5)
        distance = self.rectangular.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, 2.1120830, places=5)

    def test_dict(self):
        dictionary = self.rectangular.to_dict()
        expected_result = {'shape': {'type': 'rectangle', 'width': 10, 'height': 10, 'angle': 0.7853981633974483}}
        self.assertDictEqual(dictionary, expected_result)
        new_rectangular = Rectangular()
        new_rectangular.from_dict(dictionary)
        self.assertEqual(self.rectangular, new_rectangular)


if __name__ == "__main__":
    unittest.main()