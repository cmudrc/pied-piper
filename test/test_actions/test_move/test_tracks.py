import unittest

from piperabm.actions.move.tracks import Tracks
from piperabm.actions.move.track import Track
from piperabm.transporation.samples import transportation_0 as transportation


class TestTracksClass(unittest.TestCase):

    def setUp(self) -> None:
        self.track_1 = Track(
            pos_start=[0, 0],
            pos_end=[5000, 0],
            adjustment_factor=1
        )
        self.track_2 = Track(
            pos_start=[5000, 0],
            pos_end=[5000, 5000],
            adjustment_factor=2
        )
        self.tracks = Tracks([self.track_1, self.track_2])

    def test_duration(self):
        duration_1 = self.track_1.duration(transportation).total_seconds()
        duration_2 = self.track_2.duration(transportation).total_seconds()
        expected_result = duration_1 + duration_2
        duration = self.tracks.duration(transportation).total_seconds()
        self.assertEqual(duration, expected_result)

    def test_find_active_track(self):
        duration_1 = self.track_1.duration(transportation).total_seconds()
        duration_2 = self.track_2.duration(transportation).total_seconds()

        # Before track_1
        delta_time = -5000
        active_track, remainder_time = self.tracks.find_active_track(delta_time, transportation)
        self.assertEqual(active_track, self.track_1)
        self.assertEqual(remainder_time, 0)

        # On track_1
        delta_time = 0
        active_track, remainder_time = self.tracks.find_active_track(delta_time, transportation)
        self.assertEqual(active_track, self.track_1)
        self.assertEqual(remainder_time, delta_time)

        delta_time = 1800
        active_track, remainder_time = self.tracks.find_active_track(delta_time, transportation)
        self.assertEqual(active_track, self.track_1)
        self.assertEqual(remainder_time, delta_time)

        delta_time = 3600
        active_track, remainder_time = self.tracks.find_active_track(delta_time, transportation)
        self.assertEqual(active_track, self.track_1)
        self.assertEqual(remainder_time, delta_time)

        # On track_2
        delta_time = 7200
        active_track, remainder_time = self.tracks.find_active_track(delta_time, transportation)
        self.assertEqual(active_track, self.track_2)
        self.assertEqual(remainder_time, delta_time - duration_1)

        delta_time = 10800
        active_track, remainder_time = self.tracks.find_active_track(delta_time, transportation)
        self.assertEqual(active_track, self.track_2)
        self.assertEqual(remainder_time, delta_time - duration_1)

        # After track_2
        delta_time = 15000
        active_track, remainder_time = self.tracks.find_active_track(delta_time, transportation)
        self.assertEqual(active_track, self.track_2)
        self.assertEqual(remainder_time, duration_2)

    def test_pos(self):
        # Before track_1
        delta_time = -5000
        pos = self.tracks.pos(delta_time, transportation)
        self.assertListEqual(pos, [0, 0])

        # On track_1
        delta_time = 0
        pos = self.tracks.pos(delta_time, transportation)
        self.assertListEqual(pos, [0, 0])

        delta_time = 1800
        pos = self.tracks.pos(delta_time, transportation)
        self.assertListEqual(pos, [2500, 0])

        delta_time = 3600
        pos = self.tracks.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 0])

        # On track_2
        delta_time = 7200
        pos = self.tracks.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 2500])

        delta_time = 10800
        pos = self.tracks.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 5000])

        # After track_2
        delta_time = 15000
        pos = self.tracks.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 5000])

    def test_serialization(self):
        dictionary = self.tracks.serialize()
        tracks = Tracks()
        tracks.deserialize(dictionary)
        self.assertEqual(self.tracks, tracks)

    
if __name__ == "__main__":
    unittest.main()