import unittest

from piperabm.boundary import Boundary
from piperabm.boundary.samples.point import point_0
from piperabm.boundary.samples.circular import circular_0
from piperabm.boundary.samples.rectangular import rectangular_0


class TestCircularClass(unittest.TestCase):
    
    def setUp(self):
        self.boundary = Boundary()

    def test_relative_pos(self):
        center = [10, 10]
        pos = [13, 14]
        relative_pos = self.boundary.relative_pos(pos, center)
        self.assertEqual(relative_pos, [3, 4])

    def test_laod_point(self):
        boundary = point_0
        dictionary = boundary.to_dict()
        new_boundary = Boundary()
        new_boundary.from_dict(dictionary)
        self.assertEqual(boundary, new_boundary)

    def test_laod_circular(self):
        boundary = circular_0
        dictionary = boundary.to_dict()
        new_boundary = Boundary()
        new_boundary.from_dict(dictionary)
        self.assertEqual(boundary, new_boundary)

    def test_laod_rectangular(self):
        boundary = rectangular_0
        dictionary = boundary.to_dict()
        new_boundary = Boundary()
        new_boundary.from_dict(dictionary)
        self.assertEqual(boundary, new_boundary)


if __name__ == "__main__":
    unittest.main()