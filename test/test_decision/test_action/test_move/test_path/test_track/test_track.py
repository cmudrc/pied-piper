import unittest

from piperabm import path


class TestLinearTrackClass(unittest.TestCase):

    track = path.Linear([0, 0], [1, 1], length=3)

    def test_pos(self):
        self.assertListEqual(self.track.pos(current_length=1.5), [0.5, 0.5])
    
    def test_progress(self):
        self.assertEqual(self.track.progress(current_length=1.5), 0.5)

    def test_status(self):
        progress = self.track.progress(current_length=1.5)
        self.assertEqual(self.track.status(progress=progress), 'in progress')


if __name__ == "__main__":
    unittest.main()
