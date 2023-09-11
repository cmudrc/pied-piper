import unittest

from piperabm.tools import line_intersecting_line


class TestSymbols(unittest.TestCase):

    def test_case_0(self):
        """ Normal intersection """
        line_1_point_1 = [0, 0]
        line_1_point_2 = [2, 2]
        line_2_point_1 = [0, 2]
        line_2_point_2 = [2, 0]
        result = line_intersecting_line(
            line_1_point_1,
            line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertListEqual(list(result), [1, 1])

    def test_case_1(self):
        """ Lines parallel to axes """
        line_1_point_1 = [1, 0]
        line_1_point_2 = [1, 2]
        line_2_point_1 = [0, 1]
        line_2_point_2 = [2, 1]
        result = line_intersecting_line(
            line_1_point_1,
            line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertListEqual(list(result), [1, 1])

    def test_case_2(self):
        """ Lines parallel to axes """
        line_1_point_1 = [1, 0]
        line_1_point_2 = [1, 0.5]
        line_2_point_1 = [0, 1]
        line_2_point_2 = [0.5, 1]
        result = line_intersecting_line(
            line_1_point_1,
            line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertEqual(result, None)

    def test_case_3(self):
        """ Lines parallel to each other """
        line_1_point_1 = [0, 0]
        line_1_point_2 = [2, 0]
        line_2_point_1 = [0, 2]
        line_2_point_2 = [2, 2]
        result = line_intersecting_line(
            line_1_point_1,
            line_1_point_2,
            line_2_point_1,
            line_2_point_2
        )
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()