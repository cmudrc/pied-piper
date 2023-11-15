import unittest

from piperabm.actions.move.tracks import Tracks
from piperabm.actions.move.track import Track
from piperabm.transporation.samples import transportation_0


class TestTracksClass(unittest.TestCase):

    def setUp(self) -> None:
        self.track_1 = Track(
            pos_start=[0, 0],
            pos_end=[4000, 0],
            adjustment_factor=1,
            transportation=transportation_0
        )
        self.track_2 = Track(
            pos_start=[4000, 0],
            pos_end=[4000, 3000],
            adjustment_factor=2,
            transportation=transportation_0
        )
        self.tracks = Tracks([self.track_1, self.track_2])

    def test_duration(self):
        duration_1 = self.track_1.duration.total_seconds()
        duration_2 = self.track_2.duration.total_seconds()
        expected_result = duration_1 + duration_2
        duration = self.tracks.duration.total_seconds()
        self.assertEqual(duration, expected_result)

    def test_find_active_track(self):
        delta_time = 1000
        active_track, remainder_time = self.tracks.find_active_track(delta_time)
        self.assertListEqual(list(active_track.pos_start), [0, 0])
        self.assertEqual(remainder_time, delta_time)

        delta_time = 5000
        active_track, remainder_time = self.tracks.find_active_track(delta_time)
        self.assertListEqual(list(active_track.pos_start), [4000, 0])
        duration_1 = self.track_1.duration.total_seconds()
        expected_result = delta_time - duration_1
        self.assertEqual(remainder_time, expected_result)

    def test_pos(self):
        delta_time = -1000
        pos = self.tracks.pos(delta_time)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = 0
        pos = self.tracks.pos(delta_time)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = self.track_1.duration / 2
        pos = self.tracks.pos(delta_time)
        expected_result = [2000, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = self.track_1.duration
        pos = self.tracks.pos(delta_time)
        expected_result = [4000, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = self.track_1.duration + self.track_2.duration / 2
        pos = self.tracks.pos(delta_time)
        expected_result = [4000, 1500]
        self.assertListEqual(pos, expected_result)

        delta_time = self.tracks.duration
        pos = self.tracks.pos(delta_time)
        expected_result = [4000, 3000]
        self.assertListEqual(pos, expected_result)

        delta_time = self.tracks.duration.total_seconds() + 1000
        pos = self.tracks.pos(delta_time)
        expected_result = [4000, 3000]
        self.assertListEqual(pos, expected_result)

    
if __name__ == "__main__":
    unittest.main()