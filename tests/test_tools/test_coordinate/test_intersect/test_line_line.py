import unittest
from piperabm.tools.coordinate.intersect import line_line


class TestIntersect(unittest.TestCase):

    def test_intersect_line_line(self):
        line_1_point_1 = [1, 0]
        line_1_point_2 = [1, 2]
        line_2_point_1 = [0, 1]
        line_2_point_2 = [2, 1]
        point = line_line(
            line_1_point_1, line_1_point_2, line_2_point_1, line_2_point_2
        )
        self.assertListEqual(point, [1.0, 1.0])


if __name__ == "__main__":
    unittest.main()
