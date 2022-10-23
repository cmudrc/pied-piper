import unittest

from tools.path import Path, Linear


class TestLinearTrackClass(unittest.TestCase):
    tracks = [
        Linear(pos_start=[0, 0], pos_end=[0, 3]),
        Linear(pos_start=[0, 3], pos_end=[4, 3])
    ]
    path = Path(tracks)

    def test_add_next(self):
        pass

    def test_total_length(self):
        self.assertEqual(self.path.total_length(), 7)

    def test_pos_0(self):
        current_length = 0
        self.assertListEqual(self.path.pos(current_length), [0, 0])

    def test_pos_1(self):
        current_length = 3
        self.assertListEqual(self.path.pos(current_length), [0, 3])

    def test_pos_2(self):
        current_length = 8
        self.assertListEqual(self.path.pos(current_length), [4, 3])
