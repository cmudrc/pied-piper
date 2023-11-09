import unittest

from piperabm.tools.coordinate.distance import point_to_line


class TestDistancePointToLineFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.line_point_1 = [0, 0]
        self.line_point_2 = [2, 0]
    
    def test_case_0(self):
        """
        Prependicular line is intersecting out of the segment
        """
        point = [-3, 4]
        distance = point_to_line(point, self.line_point_1, self.line_point_2)
        self.assertAlmostEqual(distance, 4, places=2)

    def test_case_boundary(self):
        """
        Prependicular line is intersecting in the boundary of the segment
        """
        point = [0, 4]
        distance = point_to_line(point, self.line_point_1, self.line_point_2)
        self.assertAlmostEqual(distance, 4, places=2)

    def test_case_in(self):
        """
        Prependicular line is intersecting inside of the segment
        """
        point = [1, 4]
        distance = point_to_line(point, self.line_point_1, self.line_point_2)
        self.assertAlmostEqual(distance, 4, places=2)

    def test_case_on_in(self):
        """
        The point is on the segment
        """
        point = [1, 0]
        distance = point_to_line(point, self.line_point_1, self.line_point_2)
        self.assertAlmostEqual(distance, 0, places=2)

    def test_case_on_out(self):
        """
        The point is on the line
        """
        point = [-1, 0]
        distance = point_to_line(point, self.line_point_1, self.line_point_2)
        self.assertAlmostEqual(distance, 0, places=2)


if __name__ == "__main__":
    unittest.main()