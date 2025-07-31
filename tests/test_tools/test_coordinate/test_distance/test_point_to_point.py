import unittest
from piperabm.tools.coordinate.distance.point_to_point import point_to_point


class TestPointToPoint(unittest.TestCase):

    def test_point_to_point(self):
        point_1 = [0, 0]
        point_2 = [3, 4]
        distance = point_to_point(point_1, point_2)
        self.assertEqual(distance, 5)
        

if __name__ == "__main__":
    unittest.main()