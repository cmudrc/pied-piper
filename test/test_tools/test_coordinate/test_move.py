import unittest

from piperabm.tools.coordinate.move import move_coordinate, move_point


class TestMovePointFunction(unittest.TestCase):
    
    def test_0(self):
        pos = [0, 0]
        vector = [2, 3]
        new_pos = move_point(pos, vector)
        expected_result = [2, 3]
        self.assertListEqual(new_pos, expected_result)

    def test_1(self):
        pos = [2, 3]
        vector = [2, 3]
        new_pos = move_point(pos, vector)
        expected_result = [4, 6]
        self.assertListEqual(new_pos, expected_result)


class TestMoveCoordinateFunction(unittest.TestCase):
    
    def test_0(self):
        pos = [0, 0]
        vector = [2, 3]
        new_pos = move_coordinate(pos, vector)
        expected_result = [-2, -3]
        self.assertListEqual(new_pos, expected_result)

    def test_1(self):
        pos = [2, 3]
        vector = [2, 3]
        new_pos = move_coordinate(pos, vector)
        expected_result = [0, 0]
        self.assertListEqual(new_pos, expected_result)


if __name__ == "__main__":
    unittest.main()