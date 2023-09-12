import unittest

from piperabm.tools import intersect_line_circle


class TestLineCircleFunction(unittest.TestCase):

    def test_case_0(self):
        """ Line intersects circle """
        point_1 = [0, 0]
        point_2 = [2, 2]
        circle_center = [1.4, 0.6]
        circle_radius = 0.6
        result = intersect_line_circle(point_1, point_2, circle_center, circle_radius)
        self.assertTrue(result)

    def test_case_1(self):
        """ Line doesn't intersect circle """
        point_1 = [0, 0]
        point_2 = [2, 2]
        circle_center = [1.4, 0.6]
        circle_radius = 0.5
        result = intersect_line_circle(point_1, point_2, circle_center, circle_radius)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()