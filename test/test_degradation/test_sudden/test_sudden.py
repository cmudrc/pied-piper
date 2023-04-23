import unittest
from copy import deepcopy

from piperabm.unit import DT, Date
from piperabm.degradation.sudden import SuddenDegradation
from piperabm.degradation.sudden.distributions.samples.dirac_delta import dirac_delta_0


class TestSuddenDegradation(unittest.TestCase):

    def setUp(self):
        distribution = deepcopy(dirac_delta_0)
        self.degradation = SuddenDegradation(distribution)

    def test_date_to_time(self):
        time_start, time_end = self.degradation.date_to_time(
            initiation_date=Date(2000, 1, 1),
            start_date=Date(2000, 1, 2),
            end_date=Date(2000, 1, 3)
        )
        seconds_per_day = 60 * 60 * 24
        self.assertEqual(time_start, seconds_per_day * 1)
        self.assertEqual(time_end, seconds_per_day * 2)

    def test_is_active_0(self):
        result = self.degradation.is_active(
            initiation_date=Date(2000, 1, 1),
            start_date=Date(2000, 1, 2),
            end_date=Date(2000, 1, 4)
        )
        self.assertTrue(result)

    def test_is_active_1(self):
        result = self.degradation.is_active(
            initiation_date=Date(2000, 1, 1),
            start_date=Date(2000, 1, 9),
            end_date=Date(2000, 1, 11)
        )
        self.assertFalse(result)

    def test_dict(self):
        dictionary = self.degradation.to_dict()
        expected_result = {
            'distribution': {
                'type': 'dirac delta',
                'main': DT(days=10).total_seconds()
            },
            'unit_size': None}
        self.assertDictEqual(dictionary, expected_result)
        new_degradation = SuddenDegradation()
        new_degradation.from_dict(dictionary)
        self.assertEqual(self.degradation, new_degradation)


if __name__ == "__main__":
    unittest.main()
