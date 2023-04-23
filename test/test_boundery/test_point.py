import unittest

from piperabm.boundary import Point
from piperabm.boundary.point.samples import point_0 as point
from piperabm.tools.symbols import SYMBOLS


class TestPointClass(unittest.TestCase):
    
    def setUp(self):
        self.point = point
        self.center = [30, 40]

        self.pos_0 = [0, 0]
        self.pos_1 = [29, 40]
        self.pos_2 = [30, 40]

    def test_is_in_0(self):
        pos = self.pos_0
        center = self.center
        self.assertFalse(self.point.is_in(pos, center))

    def test_is_in_1(self):
        pos = self.pos_1
        center = self.center
        self.assertFalse(self.point.is_in(pos, center))

    def test_is_in_2(self):
        pos = self.pos_2
        center = self.center
        self.assertTrue(self.point.is_in(pos, center))

    def test_random_pos(self):
        center = self.center
        pos = self.point.rand_pos(center)
        self.assertTrue(self.point.is_in(pos, center))

    def test_distance_0(self):
        pos = self.pos_0
        distance = self.point.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 50, places=5)
        distance = self.point.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, 50, places=5)

    def test_distance_1(self):
        pos = self.pos_1
        distance = self.point.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 1, places=5)
        distance = self.point.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, 1, places=5)

    def test_distance_2(self):
        pos = self.pos_2
        distance = self.point.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 0, places=5)
        distance = self.point.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, 0, places=5)

    def test_dict(self):
        dictionary = self.point.to_dict()
        expected_result = {'shape': {'radius': SYMBOLS['eps'], 'type': 'dot'}}
        self.assertDictEqual(dictionary, expected_result)
        new_point = Point()
        new_point.from_dict(dictionary)
        self.assertEqual(self.point, new_point)


if __name__ == "__main__":
    unittest.main()