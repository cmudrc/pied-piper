import unittest

from piperabm.tools.shapes import Rectangle
from piperabm.tools.shapes.rectangle.samples import rectangle_0, rectangle_1


class TestRectangleClass_0(unittest.TestCase):
    
    def setUp(self):
        self.rectangle = rectangle_0
        
        self.pos_0 = [0, 1.4]
        self.pos_1 = [0, 1.5]
        self.pos_2 = [0, 1.6]

    def test_is_in_0(self):
        self.assertTrue(self.rectangle.is_in(self.pos_0))

    def test_is_in_1(self):
        self.assertTrue(self.rectangle.is_in(self.pos_1))

    def test_is_in_2(self):
        self.assertFalse(self.rectangle.is_in(self.pos_2))

    def test_random_pos(self):
        pos = self.rectangle.rand_pos()
        self.assertTrue(self.rectangle.is_in(pos))

    def test_distance_0(self):
        pos = self.pos_0
        distance = self.rectangle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 1.4, places=5)
        distance = self.rectangle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, -0.1, places=5)

    def test_distance_1(self):
        pos = self.pos_1
        distance = self.rectangle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 1.5, places=5)
        distance = self.rectangle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 0, places=5)

    def test_distance_2(self):
        pos = self.pos_2
        distance = self.rectangle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 1.6, places=5)
        distance = self.rectangle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 0.1, places=5)

    def test_dict(self):
        dictionary = self.rectangle.to_dict()
        expected_result = {'type': 'rectangle', 'width': 4, 'height': 3, 'angle': 0}
        self.assertDictEqual(dictionary, expected_result)
        new_rectangle = Rectangle()
        new_rectangle.from_dict(dictionary)
        self.assertEqual(self.rectangle, new_rectangle)


class TestRectangleClass_1(unittest.TestCase):
    
    def setUp(self):
        self.rectangle = rectangle_1
        
        self.pos_0 = [6, 0]
        self.pos_1 = [6, 2]
        self.pos_2 = [6, 4]

    def test_is_in_0(self):
        self.assertTrue(self.rectangle.is_in(self.pos_0))

    def test_is_in_1(self):
        self.assertFalse(self.rectangle.is_in(self.pos_1))

    def test_is_in_2(self):
        self.assertFalse(self.rectangle.is_in(self.pos_2))

    def test_random_pos(self):
        pos = self.rectangle.rand_pos()
        self.assertTrue(self.rectangle.is_in(pos))

    def test_distance_0(self):
        pos = self.pos_0
        distance = self.rectangle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 6, places=5)
        distance = self.rectangle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, -1.0710678, places=5)

    def test_distance_1(self):
        pos = self.pos_1
        distance = self.rectangle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance**2, 6**2 + 2**2, places=5)
        distance = self.rectangle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 0.734385, places=5)

    def test_distance_2(self):
        pos = self.pos_2
        distance = self.rectangle.distance(pos) # default: mode='center'
        self.assertAlmostEqual(distance, 7.21110, places=5)
        distance = self.rectangle.distance(pos, mode='body')
        self.assertAlmostEqual(distance, 2.1120830, places=5)

    def test_dict(self):
        dictionary = self.rectangle.to_dict()
        expected_result = {'type': 'rectangle', 'width': 10, 'height': 10, 'angle': 0.7853981633974483}
        self.assertDictEqual(dictionary, expected_result)
        new_rectangle = Rectangle()
        new_rectangle.from_dict(dictionary)
        self.assertEqual(self.rectangle, new_rectangle)


if __name__ == "__main__":
    unittest.main()