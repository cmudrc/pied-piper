import unittest

from piperabm.tools.coordinate.distance.distance_point_to_line import distance_point_to_line


class TestDistancePointToLineFunction(unittest.TestCase):
    
    def test_case_0(self):
        point = [1, 2]
        line_point_1 = [0, 0]
        line_point_2 = [2, 0]
        distance = distance_point_to_line(point, line_point_1, line_point_2)
        self.assertAlmostEqual(distance, 2, places=2)

    def test_case_1(self):
        point = [-1, 2]
        line_point_1 = [0, 0]
        line_point_2 = [2, 0]
        distance = distance_point_to_line(point, line_point_1, line_point_2)
        self.assertEqual(distance, None)


if __name__ == "__main__":
    unittest.main()