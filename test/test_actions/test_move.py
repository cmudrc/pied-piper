import unittest
from copy import deepcopy

from piperabm.actions.move import Move
from piperabm.actions.move.samples import move_0


class TestMoveClass(unittest.TestCase):

    def setUp(self):
        self.move = deepcopy(move_0)

    def test_duration(self):
        self.assertAlmostEqual(self.move.duration.total_seconds(), 37.5, places=1)

    def test_dates(self):
        self.assertEqual(self.move.start_date.day, 5)
        expected_end_date = self.move.start_date + self.move.duration
        self.assertEqual(self.move.end_date, expected_end_date)

    def test_fuel(self):
        expected_result = {
            'food': 0.0008681787037037036,
            'water': 0.0004340893518518518,
            'energy': 0.0
        }
        self.assertDictEqual(self.move.fuel_consumption.to_dict(), expected_result)

    def test_progress(self):
        duration = self.move.duration / 2
        date = self.move.start_date + duration
        progress = self.move.progress(date)
        self.assertEqual(progress, 0.5)

    def test_current_track(self):
        # when reaches intermediary node?
        #print(self.move.environment.get_edge_object(0, 2).duration(self.move.transportation))
        
        date = self.move.start_date
        index, elapsed = self.move.current_track(date)
        self.assertEqual(index, 0)
        self.assertAlmostEqual(elapsed, 0, places=1)

        duration = self.move.duration / 4
        date = self.move.start_date + duration
        index, elapsed = self.move.current_track(date)
        self.assertEqual(index, 0)
        self.assertAlmostEqual(elapsed, 9.37, places=1)

        duration = self.move.duration / 2
        date = self.move.start_date + duration
        index, elapsed = self.move.current_track(date)
        self.assertEqual(index, 1)
        self.assertAlmostEqual(elapsed, 2.85, places=1)

        duration = self.move.duration
        date = self.move.start_date + duration
        index, elapsed = self.move.current_track(date)
        self.assertEqual(index, 1)
        self.assertAlmostEqual(elapsed, 21.60, places=1)

    def test_pos(self):
        date = self.move.start_date
        pos = self.move.pos(date)
        expected_pos = [-2.0, -2.0]
        self.assertListEqual(pos, expected_pos)

        duration = self.move.duration / 4
        date = self.move.start_date + duration
        pos = self.move.pos(date)
        expected_pos = [10.969198984993701, -0.8209819104551195]
        self.assertListEqual(pos, expected_pos)

        duration = self.move.duration / 2
        date = self.move.start_date + duration
        pos = self.move.pos(date)
        expected_pos = [20.0, 2.636425925925925]
        self.assertListEqual(pos, expected_pos)

        duration = self.move.duration
        date = self.move.start_date + duration
        pos = self.move.pos(date)
        expected_pos = [20.0, 19.999999999999996]
        self.assertListEqual(pos, expected_pos)

    def test_dict(self):
        dictionary = self.move.to_dict()
        expected_result = {
            'start_date': {'year': 2020, 'month': 1, 'day': 5, 'hour': 0, 'minute': 0, 'second': 0},
            'end_date': {'year': 2020, 'month': 1, 'day': 5, 'hour': 0, 'minute': 0, 'second': 37},
            'duration': 37.50532,
            'done': False,
            'type': 'move',
            'path': [(0, 2), (2, 1)],
            'transportation': {
                'fuel_rate': {
                    'energy': 0.0,
                    'food': 2.3148148148148147e-05,
                    'water': 1.1574074074074073e-05
                },
                'name': 'foot',
                'speed': 1.3888888888888888},
        }
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        move = Move()
        move.from_dict(dictionary)
        self.assertDictEqual(move.to_dict(), self.move.to_dict())


if __name__ == "__main__":
    unittest.main()