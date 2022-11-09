import unittest

from piperabm.path import Path


class TestLinearTrackClass(unittest.TestCase):

    path = Path()
    path.add(pos=[0, 0])
    path.add(pos=[0, 3])
    path.add(pos=[4, 3])
    
    def test_total_length(self):
        self.assertEqual(self.path.total_length(), 7)

    def test_total_length_1(self):
        self.path.add(pos=[0, 0])
        self.assertEqual(self.path.total_length(), 12)

    def test_pos_0(self):
        current_length = 0
        self.assertListEqual(self.path.pos(current_length), [0, 0])

    def test_pos_1(self):
        current_length = 3
        self.assertListEqual(self.path.pos(current_length), [0, 3])

    def test_pos_2(self):
        current_length = 8
        self.assertListEqual(self.path.pos(current_length), [4, 3])


if __name__ == "__main__":
    unittest.main()