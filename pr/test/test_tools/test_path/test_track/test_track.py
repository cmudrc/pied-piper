import unittest

from tools.path import Linear


class TestLinearTrackClass(unittest.TestCase):

    track = Linear([0, 0], [1, 1], length=3)

    def test_pos(self):
        self.assertListEqual(self.track.pos(current_length=1.5), [0.5, 0.5])
    
    def test_progress(self):
        self.assertEqual(self.track.progress(current_length=1.5), 0.5)

    def test_status(self):
        progress = self.track.progress(current_length=1.5)
        self.assertEqual(self.track.status(progress=progress), 'in progress')
