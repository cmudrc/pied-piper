import unittest

from piperabm.tools.coordinate.distance.point_to_line_segment import point_to_line_segment


class TestDistancePointToLineSegmentFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.line_point_1 = [0, 0]
        self.line_point_2 = [2, 0]
    
    def test_case_out(self):
        """
        Prependicular line is intersecting out of the segment
        """
        point = [-3, 4]
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2)
        self.assertEqual(distance, 5)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, vector=True)
        self.assertListEqual(distance, [3, -4])
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True)
        self.assertEqual(distance, None)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True, vector=True)
        self.assertEqual(distance, None)

    def test_case_boundary(self):
        """
        Prependicular line is intersecting in the boundary of the segment
        """
        point = [0, 4]
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2)
        self.assertEqual(distance, 4)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, vector=True)
        self.assertListEqual(distance, [0, -4])
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True)
        self.assertEqual(distance, 4)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True, vector=True)
        self.assertListEqual(distance, [0, -4])

    def test_case_in(self):
        """
        Prependicular line is intersecting inside of the segment
        """
        point = [1, 4]
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2)
        self.assertEqual(distance, 4)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, vector=True)
        self.assertListEqual(distance, [0, -4])
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True)
        self.assertEqual(distance, 4)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True, vector=True)
        self.assertListEqual(distance, [0, -4])

    def test_case_on_in(self):
        """
        The point is on the segment
        """
        point = [1, 0]
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2)
        self.assertEqual(distance, 0)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, vector=True)
        self.assertListEqual(distance, [0, 0])
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True)
        self.assertEqual(distance, 0)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True, vector=True)
        self.assertListEqual(distance, [0, 0])

    def test_case_on_out(self):
        """
        The point is on the line
        """
        point = [-1, 0]
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2)
        self.assertEqual(distance, 1)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, vector=True)
        self.assertListEqual(distance, [1, 0])
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True)
        self.assertEqual(distance, None)
        distance = point_to_line_segment(point, self.line_point_1, self.line_point_2, perpendicular_only=True, vector=True)
        self.assertEqual(distance, None)


if __name__ == '__main__':
    unittest.main()