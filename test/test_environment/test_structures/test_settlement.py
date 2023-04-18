import unittest

from piperabm.environment.structures import Settlement
from piperabm.environment.structures.samples import settlement_0 as settlement
from piperabm.unit import Date, DT


class TestSettlementClass(unittest.TestCase):

    def setUp(self):
        self.settlement = settlement

    def test_dict(self):
        dictionary = self.settlement.to_dict()
        print(self.settlement.boundary)
        expected_result = {
            'boundary': {'shape': {'type': 'dot', 'radius': 2.220446049250313e-16}},
            'active': True,
            'start_date': {'year': 2020, 'month': 1, 'day': 2, 'hour': 0, 'minute': 0, 'second': 0},
            'end_date': None,
            'sudden_degradation': {'distribution': {'type': 'dirac delta', 'main': 864000.0}, 'coeff': 1},
            'progressive_degradation': {'usage_max': 'inf', 'usage_current': 0, 'formula_name': 'formula_01'},
            'type': 'settlement'
        }
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        new_settlement = Settlement()
        new_settlement.from_dict(dictionary)
        self.assertEqual(self.settlement, new_settlement)

    def test_progressive_degradation(self):
        self.settlement.add_usage(amount=5)
        self.assertEqual(self.settlement.degradation_factor(), 1)

    def test_sudden_degradation(self):
        start_date = Date(2020, 1, 2)
        end_date = start_date + DT(days=9)
        active = self.settlement.degradation_active(start_date, end_date)
        self.assertTrue(active)
        end_date = start_date + DT(days=10)
        active = self.settlement.degradation_active(start_date, end_date)
        self.assertFalse(active)
        end_date = start_date + DT(days=11)
        active = self.settlement.degradation_active(start_date, end_date)
        self.assertFalse(active)

    def test_exists(self):
        start_date = Date(2020, 1, 4)
        end_date = start_date + DT(days=2)
        exists = self.settlement.exists(start_date, end_date)
        self.assertTrue(exists)
        start_date = Date(2020, 1, 1)
        end_date = start_date + DT(days=1)
        exists = self.settlement.exists(start_date, end_date)
        self.assertFalse(exists)


if __name__ == "__main__":
    unittest.main()