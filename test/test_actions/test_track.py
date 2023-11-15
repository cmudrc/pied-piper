import unittest
from copy import deepcopy

from piperabm.actions.move.track import Track
from piperabm.transporation.samples import transportation_0


class TestTrackClass(unittest.TestCase):

    def setUp(self):
        self.track = Track(
            pos_start=[0, 0],
            pos_end=[5000, 0],
            adjustment_factor=1,
            transportation=transportation_0
        )
        self.factor = 2

    def test_length(self):
        track = deepcopy(self.track)

        length = track.length
        expected_result = 5000
        self.assertEqual(length, expected_result)

        track.adjustment_factor = self.factor
        length = track.length
        expected_result = 5000
        self.assertEqual(length, expected_result)

    def test_length_adjusted(self):
        track = deepcopy(self.track)

        length_adjusted = track.length_adjusted
        expected_result = 5000
        self.assertEqual(length_adjusted, expected_result)

        track.adjustment_factor = self.factor
        length_adjusted = track.length_adjusted
        expected_result = 5000 * self.factor
        self.assertEqual(length_adjusted, expected_result)

    def test_vector(self):
        track = deepcopy(self.track)
        vector = track.vector
        expected_result = [5000, 0]
        self.assertListEqual(list(vector), expected_result)

        track.adjustment_factor = self.factor
        vector = track.vector
        expected_result = [5000, 0]
        self.assertListEqual(list(vector), expected_result)

    def test_unit_vector(self):
        track = deepcopy(self.track)
        unit_vector = track.unit_vector
        expected_result = [1, 0]
        self.assertListEqual(list(unit_vector), expected_result)

        track.adjustment_factor = self.factor
        unit_vector = track.unit_vector
        expected_result = [1, 0]
        self.assertListEqual(list(unit_vector), expected_result)

    def test_duration(self):
        track = deepcopy(self.track)
        duration = track.duration
        expected_result = 3600
        self.assertEqual(duration.total_seconds(), expected_result)

        track.adjustment_factor = self.factor
        duration = track.duration
        expected_result = 3600 * self.factor
        self.assertEqual(duration.total_seconds(), expected_result)

    def test_pos_progress(self):
        track_1 = deepcopy(self.track)
        track_2 = deepcopy(self.track)
        track_2.adjustment_factor = self.factor

        progress = -0.5
        pos = track_1.pos_by_progress(progress)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos_by_progress(progress)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)

        progress = 0
        pos = track_1.pos_by_progress(progress)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos_by_progress(progress)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)

        progress = 0.5
        pos = track_1.pos_by_progress(progress)
        expected_result = [2500, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos_by_progress(progress)
        expected_result = [2500, 0]
        self.assertListEqual(pos, expected_result)

        progress = 1
        pos = track_1.pos_by_progress(progress)
        expected_result = [5000, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos_by_progress(progress)
        expected_result = [5000, 0]
        self.assertListEqual(pos, expected_result)

        progress = 1.5
        pos = track_1.pos_by_progress(progress)
        expected_result = [5000, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos_by_progress(progress)
        expected_result = [5000, 0]
        self.assertListEqual(pos, expected_result)

    def test_pos(self):
        track_1 = deepcopy(self.track)
        track_2 = deepcopy(self.track)
        track_2.adjustment_factor = self.factor

        delta_time = -1800
        pos = track_1.pos(delta_time)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos(delta_time)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = 0
        pos = track_1.pos(delta_time)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos(delta_time)
        expected_result = [0, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = 1800
        pos = track_1.pos(delta_time)
        expected_result = [2500, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos(delta_time)
        expected_result = [1250, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = 1800
        pos = track_1.pos(delta_time)
        expected_result = [2500, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos(delta_time)
        expected_result = [1250, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = 3600
        pos = track_1.pos(delta_time)
        expected_result = [5000, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos(delta_time)
        expected_result = [2500, 0]
        self.assertListEqual(pos, expected_result)

        delta_time = 7200
        pos = track_1.pos(delta_time)
        expected_result = [5000, 0]
        self.assertListEqual(pos, expected_result)
        pos = track_2.pos(delta_time)
        expected_result = [5000, 0]
        self.assertListEqual(pos, expected_result)


if __name__ == "__main__":
    unittest.main()