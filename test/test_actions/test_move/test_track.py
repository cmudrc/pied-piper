import unittest

from piperabm.actions.move.track import Track
from piperabm.transportation.samples import transportation_0 as transportation


class TestTrackClass(unittest.TestCase):

    def setUp(self):
        pos_start = [0, 0]
        pos_end = [5000, 0]
        self.track_1 = Track(
            pos_start,
            pos_end,
            adjustment_factor = 1
        )
        self.track_2 = Track(
            pos_start,
            pos_end,
            adjustment_factor = 2
        )

    def test_length(self):
        self.assertEqual(self.track_1.length_real, 5000)
        self.assertEqual(self.track_1.length_adjusted, 5000)
        self.assertEqual(self.track_2.length_real, 5000)
        self.assertEqual(self.track_2.length_adjusted, 10000)

    def test_vector(self):
        expected_result = [5000, 0]
        self.assertListEqual(list(self.track_1.vector), expected_result)
        self.assertListEqual(list(self.track_2.vector), expected_result)

    def test_unit_vector(self):
        expected_result = [1, 0]
        self.assertListEqual(list(self.track_1.unit_vector), expected_result)
        self.assertListEqual(list(self.track_2.unit_vector), expected_result)

    def test_duration(self):
        self.assertEqual(self.track_1.duration(transportation).total_seconds(), 3600)
        self.assertEqual(self.track_2.duration(transportation).total_seconds(), 7200)

    def test_total_fuel(self):
        total_fuel = self.track_1.total_fuel(transportation)
        self.assertAlmostEqual(total_fuel('food'), 0.083, places=2)
        self.assertAlmostEqual(total_fuel('water'), 0.042, places=2)
        self.assertAlmostEqual(total_fuel('energy'), 0, places=2)

        total_fuel = self.track_2.total_fuel(transportation)
        self.assertAlmostEqual(total_fuel('food'), 0.166, places=2)
        self.assertAlmostEqual(total_fuel('water'), 0.084, places=2)
        self.assertAlmostEqual(total_fuel('energy'), 0, places=2)
    
    def test_pos_by_progress(self):
        progress = -0.5
        pos = self.track_1.pos_by_progress(progress)
        self.assertListEqual(pos, [0, 0])
        pos = self.track_2.pos_by_progress(progress)
        self.assertListEqual(pos, [0, 0])

        progress = 0
        pos = self.track_1.pos_by_progress(progress)
        self.assertListEqual(pos, [0, 0])
        pos = self.track_2.pos_by_progress(progress)
        self.assertListEqual(pos, [0, 0])

        progress = 0.5
        pos = self.track_1.pos_by_progress(progress)
        self.assertListEqual(pos, [2500, 0])
        pos = self.track_2.pos_by_progress(progress)
        self.assertListEqual(pos, [2500, 0])

        progress = 1
        pos = self.track_1.pos_by_progress(progress)
        self.assertListEqual(pos, [5000, 0])
        pos = self.track_2.pos_by_progress(progress)
        self.assertListEqual(pos, [5000, 0])

        progress = 1.5
        pos = self.track_1.pos_by_progress(progress)
        self.assertListEqual(pos, [5000, 0])
        pos = self.track_2.pos_by_progress(progress)
        self.assertListEqual(pos, [5000, 0])

    def test_pos(self):
        delta_time = -1800
        pos = self.track_1.pos(delta_time, transportation)
        self.assertListEqual(pos, [0, 0])
        pos = self.track_2.pos(delta_time, transportation)
        self.assertListEqual(pos, [0, 0])

        delta_time = 0
        pos = self.track_1.pos(delta_time, transportation)
        self.assertListEqual(pos, [0, 0])
        pos = self.track_2.pos(delta_time, transportation)
        self.assertListEqual(pos, [0, 0])

        delta_time = 1800
        pos = self.track_1.pos(delta_time, transportation)
        self.assertListEqual(pos, [2500, 0])
        pos = self.track_2.pos(delta_time, transportation)
        self.assertListEqual(pos, [1250, 0])

        delta_time = 3600
        pos = self.track_1.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 0])
        pos = self.track_2.pos(delta_time, transportation)
        self.assertListEqual(pos, [2500, 0])

        delta_time = 7200
        pos = self.track_1.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 0])
        pos = self.track_2.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 0])

        delta_time = 10000
        pos = self.track_1.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 0])
        pos = self.track_2.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 0])

    def test_serialization(self):
        dictionary = self.track_1.serialize()
        track = Track()
        track.deserialize(dictionary)
        self.assertEqual(self.track_1, track)


if __name__ == "__main__":
    unittest.main()