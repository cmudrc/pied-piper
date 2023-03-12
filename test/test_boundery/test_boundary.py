import unittest
from copy import deepcopy

from piperabm.boundary import Circular, Point


class TestCircularClass(unittest.TestCase):
    
    def setUp(self):
        boundary = Circular(radius=2)
        boundary.center = [10, 10]
        self.boundary = boundary

    def test_circular_boundary_in(self):
        boundary = deepcopy(self.boundary)
        other = Point()
        other.center = [11, 11]
        self.assertTrue(boundary.is_in(other), msg="Should be equal")

    def test_circular_boundary_out(self):
        boundary = deepcopy(self.boundary)
        other = Point()
        other.center = [11, 12]
        self.assertFalse(boundary.is_in(other), msg="Should be equal")

    def test_random_pos(self):
        boundary = deepcopy(self.boundary)
        pos = boundary.rand_pos()
        self.assertTrue(boundary.is_in(pos))

    def test_distance_from_center(self):
        boundary = deepcopy(self.boundary)
        pos = [14, 10]
        distance = boundary.distance(pos)
        self.assertEqual(distance, 4)

    def test_distance_from_boundary(self):
        boundary = deepcopy(self.boundary)
        pos = [14, 10]
        distance = boundary.distance(pos, mode='boundary')
        self.assertEqual(distance, 2)


if __name__ == "__main__":
    unittest.main()