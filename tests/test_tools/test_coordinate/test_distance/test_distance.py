import unittest
from piperabm.tools.coordinate.distance import distance as ds


class TestDistance(unittest.TestCase):

    def test_distance_point_to_point(self):
        point_1 = [0, 0]
        point_2 = [3, 4]
        distance = ds.point_to_point(point_1, point_2)
        self.assertEqual(distance, 5)
        

if __name__ == "__main__":
    unittest.main()