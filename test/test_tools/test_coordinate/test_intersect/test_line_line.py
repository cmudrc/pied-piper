import unittest

from piperabm.tools import intersect_line_line


class TestLineLineFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.line_1_point_1 = [0, 0]
        self.line_1_point_2 = [2, 0]

    def test_case_in(self):
        """
        Intersection within the segments
        """
        line_2_point_1 = [1, 1]
        line_2_point_2 = [1, -1]
        intersection = intersect_line_line(
            self.line_1_point_1,
            self.line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertListEqual(intersection, [1, 0])

    def test_case_boundary(self):
        """
        Intersection on one end of the segments
        """
        line_2_point_1 = [0, 1]
        line_2_point_2 = [0, -1]
        intersection = intersect_line_line(
            self.line_1_point_1,
            self.line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertListEqual(intersection, [0, 0])

    def test_case_out(self):
        """
        Intersection on out of the segments
        """
        line_2_point_1 = [-1, 1]
        line_2_point_2 = [-1, -1]
        intersection = intersect_line_line(
            self.line_1_point_1,
            self.line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertListEqual(intersection, [-1, 0])

    def test_case_parallel(self):
        """
        Lines parallel to each other
        """
        line_2_point_1 = [0, 1]
        line_2_point_2 = [2, 1]
        intersection = intersect_line_line(
            self.line_1_point_1,
            self.line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertEqual(intersection, None)

    def test_case_4(self):
        """
        Lines on top of each other
        """
        line_2_point_1 = [-1, 0]
        line_2_point_2 = [1, 0]
        intersection = intersect_line_line(
            self.line_1_point_1,
            self.line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertEqual(intersection, None)


if __name__ == "__main__":
    unittest.main()