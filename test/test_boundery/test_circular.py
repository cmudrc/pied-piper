import unittest
from copy import deepcopy

from piperabm.boundary import Circular
from piperabm.boundary.circular.samples import circular_0 as circular


class TestCircularClass(unittest.TestCase):
    
    def setUp(self):
        self.circular = circular
        self.center = [30, 40]
        
        self.pos_0 = [24, 40]
        self.pos_1 = [25, 40]
        self.pos_2 = [26, 40]

    def test_is_in_0(self):
        pos = self.pos_0
        center = self.center
        self.assertFalse(self.circular.is_in(pos, center))

    def test_is_in_1(self):
        pos = self.pos_1
        center = self.center
        self.assertTrue(self.circular.is_in(pos, center))

    def test_is_in_2(self):
        pos = self.pos_2
        center = self.center
        self.assertTrue(self.circular.is_in(pos, center))

    def test_random_pos(self):
        center = self.center
        pos = self.circular.rand_pos(center)
        self.assertTrue(self.circular.is_in(pos, center))

    def test_distance_0(self):
        pos = self.pos_0
        distance = self.circular.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 6, places=5)
        distance = self.circular.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, 1, places=5)

    def test_distance_1(self):
        pos = self.pos_1
        distance = self.circular.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 5, places=5)
        distance = self.circular.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, 0, places=5)

    def test_distance_2(self):
        pos = self.pos_2
        distance = self.circular.distance(pos, self.center) # default: mode='center'
        self.assertAlmostEqual(distance, 4, places=5)
        distance = self.circular.distance(pos, self.center, mode='body')
        self.assertAlmostEqual(distance, -1, places=5)

    def test_dict(self):
        dictionary = self.circular.to_dict()
        expected_result = {'shape': {'radius': 5, 'type': 'circle'}}
        self.assertDictEqual(dictionary, expected_result)
        new_circular = Circular()
        new_circular.from_dict(dictionary)
        self.assertEqual(self.circular, new_circular)

    def test_delta(self):
        circular = deepcopy(self.circular)
        delta = {
            'shape': {'radius': 2,},
        }
        circular + delta
        self.assertEqual(circular.shape.radius, 7)
        circular_old = deepcopy(self.circular)
        self.assertEqual(circular - circular_old, delta)


if __name__ == "__main__":
    unittest.main()