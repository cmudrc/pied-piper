import unittest
from piperabm.tools.coordinate.distance.point_to_line import point_to_line


class TestPointToPoint(unittest.TestCase):

    def test_point_to_point_magnitude(self):
        point = [0, 0]
        line_1 = [1, 0]
        line_2 = [0, 1]
        distance = point_to_line(point, line_1, line_2)
        self.assertAlmostEqual(distance, 0.707, places=2)

    def test_point_to_point_vector(self):
        point = [0, 0]
        line_1 = [1, 0]
        line_2 = [0, 1]
        vector = point_to_line(point, line_1, line_2, vector=True, ndarray=False)
        self.assertAlmostEqual(vector[0], 0.5, places=2)
        self.assertAlmostEqual(vector[1], 0.5, places=2)
        

if __name__ == "__main__":
    unittest.main()