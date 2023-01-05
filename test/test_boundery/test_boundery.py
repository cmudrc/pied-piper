import unittest

from piperabm.boundery import Circular, Rectangular


class Other():
    """ Only a helper class """

    def __init__(self, pos):
        self.pos = pos


class TestCircularClass(unittest.TestCase):
    
    def test_circular_boundery_in(self):
        other = Other(pos=[1, 1])
        boundery = Circular(radius=2)
        boundery.center = [0, 0]
        self.assertTrue(boundery.is_in(other), msg="Should be equal")

    def test_circular_boundery_out(self):
        other = Other(pos=[1, 2])
        boundery = Circular(radius=2)
        boundery.center = [0, 0]
        self.assertFalse(boundery.is_in(other), msg="Should be equal")


class TestRectangularClass(unittest.TestCase):

    def test_rectangular_boundery_in(self):
        other = Other(pos=[0.7, 0.7])
        boundery = Rectangular(width=2, height=1, theta=0.1)
        boundery.center = [0, 0]
        self.assertFalse(boundery.is_in(other))

    def test_rectangular_boundery_out(self):
        other = Other(pos=[0.7, 0.7])
        boundery = Rectangular(width=2, height=1, theta=0.5)
        boundery.center = [0, 0]
        self.assertTrue(boundery.is_in(other))

    def test_distance_from_boundery_in(self):
        other = Other(pos=[0.4, 0.4])
        boundery = Rectangular(width=2, height=1, theta=0.1)
        boundery.center = [0, 0]
        self.assertEqual(boundery.distance(other, mode='boundery'), 0)

    def test_distance_from_boundery_out(self):
        other = Other(pos=[0.7, 0.7])
        boundery = Rectangular(width=2, height=1, theta=0.1)
        boundery.center = [0, 0]
        self.assertAlmostEqual(boundery.distance(other, mode='boundery'), 0.2, places=4)


if __name__ == "__main__":
    unittest.main()