import unittest

from piperabm.boundary.shapes import Dot
from piperabm.boundary.shapes.samples.dot import dot_0 as dot
from piperabm.tools.symbols import SYMBOLS


class TestDotClass(unittest.TestCase):
    
    def setUp(self):
        self.dot = dot
        
        self.pos_0 = [0, 0]
        self.pos_1 = [3, 4]

    def test_is_in_0(self):
        self.assertTrue(self.dot.is_in(self.pos_0))

    def test_is_in_1(self):
        self.assertFalse(self.dot.is_in(self.pos_1))

    def test_random_pos(self):
        pos = self.dot.rand_pos()
        self.assertAlmostEqual(pos[0], 0, places=5)
        self.assertAlmostEqual(pos[1], 0, places=5)

    def test_distance_0(self):
        pos = self.pos_0
        distance = self.dot.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 0, places=5)
        distance = self.dot.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 0, places=5)

    def test_distance_1(self):
        pos = self.pos_1
        distance = self.dot.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 5, places=5)
        distance = self.dot.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 5, places=5)

    def test_dict(self):
        dictionary = self.dot.to_dict()
        expected_result = {'type': 'dot', 'radius': SYMBOLS['eps']}
        self.assertDictEqual(dictionary, expected_result)
        new_dot = Dot()
        new_dot.from_dict(dictionary)
        self.assertEqual(self.dot, new_dot)


if __name__ == "__main__":
    unittest.main()