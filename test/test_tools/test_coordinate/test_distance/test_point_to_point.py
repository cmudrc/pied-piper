import unittest

from piperabm.tools.coordinate.distance.point_to_point import point_to_point


class TestDistancePointToPointFunction(unittest.TestCase):
    
    def test_0(self):
        pos_start = [0, 0, 0]
        pos_end = [0, 0, 0]
        distance = point_to_point(pos_start, pos_end)
        self.assertEqual(distance, 0)
        distance = point_to_point(pos_start, pos_end, vector=True, ndarray=False)
        self.assertListEqual(distance, [0, 0, 0])

    def test_1(self):
        pos_start = [0, 3]
        pos_end = [4, 0]
        distance = point_to_point(pos_start, pos_end)
        self.assertEqual(distance, 5)
        distance = point_to_point(pos_start, pos_end, vector=True, ndarray=False)
        self.assertListEqual(distance, [4, -3])


if __name__ == '__main__':
    unittest.main()