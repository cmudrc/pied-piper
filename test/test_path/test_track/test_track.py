import unittest
from copy import deepcopy

from piperabm import path


class TestLinearTrackClass(unittest.TestCase):

    track = path.Linear([0, 0], [1, 1], length=3)

    def test_pos_0(self):
        pos = self.track.pos(current_length=1.5)
        self.assertListEqual(pos, [0.5, 0.5])

    def test_pos_1(self):
        """
        Set difficulty of track to 2 (default=1)
        """
        track = deepcopy(self.track)
        track.difficulty = 2
        pos = track.pos(current_length=1.5)
        self.assertListEqual(pos, [0.25, 0.25])
    
    def test_progress_0(self):
        progress = self.track.progress(current_length=1.5)
        self.assertEqual(progress, 0.5)

    def test_progress_1(self):
        """
        Set difficulty of track to 2 (default=1)
        """
        track = deepcopy(self.track)
        track.difficulty = 2
        progress = track.progress(current_length=1.5)
        self.assertEqual(progress, 0.25)

    def test_status(self):
        progress = self.track.progress(current_length=1.5)
        self.assertEqual(self.track.status(progress=progress), 'in progress')

    def test_dict_conversion(self):
        """
        Test to_dict and from_dict methods
        """
        dictionary = self.track.to_dict()
        track_new = path.Linear()
        track_new.from_dict(dictionary)
        dictionary_new = track_new.to_dict()
        self.assertDictEqual(dictionary, dictionary_new)


if __name__ == "__main__":
    unittest.main()
