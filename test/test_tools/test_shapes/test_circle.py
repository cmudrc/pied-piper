import unittest
from copy import deepcopy

from piperabm.tools.shapes import Circle
from piperabm.tools.shapes.circle.samples import circle_0 as circle


class TestCircleClass(unittest.TestCase):
    
    def setUp(self):
        self.circle = circle
        
        self.pos_0 = [0, 0]
        self.pos_1 = [3, 4]
        self.pos_2 = [30, 40]

    def test_is_in_0(self):
        self.assertTrue(self.circle.is_in(self.pos_0))

    def test_is_in_1(self):
        self.assertTrue(self.circle.is_in(self.pos_1))

    def test_is_in_2(self):
        self.assertFalse(self.circle.is_in(self.pos_2))

    def test_random_pos(self):
        pos = self.circle.rand_pos()
        self.assertTrue(self.circle.is_in(pos))

    def test_distance_0(self):
        pos = self.pos_0
        distance = self.circle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 0, places=5)
        distance = self.circle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, -5, places=5)

    def test_distance_1(self):
        pos = self.pos_1
        distance = self.circle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 5, places=5)
        distance = self.circle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 0, places=5)

    def test_distance_2(self):
        pos = self.pos_2
        distance = self.circle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 50, places=5)
        distance = self.circle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 45, places=5)

    def test_dict(self):
        dictionary = self.circle.to_dict()
        expected_result = {'type': 'circle', 'radius': 5}
        self.assertDictEqual(dictionary, expected_result)
        new_circle = Circle()
        new_circle.from_dict(dictionary)
        self.assertEqual(self.circle, new_circle)

    def test_delta(self):
        circle = deepcopy(self.circle)
        delta = {'radius': 2,}
        circle + delta
        self.assertEqual(circle.radius, 7)
        circle_old = deepcopy(self.circle)
        self.assertEqual(circle_old - circle, delta)


if __name__ == "__main__":
    unittest.main()