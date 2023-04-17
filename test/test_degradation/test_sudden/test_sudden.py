import unittest

from piperabm.unit import DT, Date
from piperabm.degradation.sudden import SuddenDegradation
from piperabm.degradation.sudden.distributions import DiracDelta


class TestSuddenDegradation_Default(unittest.TestCase):
    """
    Test instance of class with empty input
    """

    def setUp(self):
        self.degradation = SuddenDegradation()

    def test_is_active(self):
        result = self.degradation.is_active(
            initiation_date=Date(2000, 1, 1),
            start_date=Date(2000, 1, 2),
            end_date=Date(2000, 1, 3)
        )
        self.assertTrue(result)


class TestSuddenDegradation_Distribution(unittest.TestCase):
    """
    Test instance of class with empty input
    """

    def setUp(self):
        distribution = DiracDelta(DT(days=5))
        self.degradation = SuddenDegradation(distribution)

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
            start_date=Date(2000, 1, 4),
            end_date=Date(2000, 1, 6)
        )
        self.assertFalse(result)

    def test_dict(self):
        dictionary = self.degradation.to_dict()
        expected_result = {
            'distribution': {
                'type': 'dirac delta',
                'main': DT(days=5).total_seconds()
            },
            'coeff': 1}
        self.assertDictEqual(dictionary, expected_result)
        new_degradation = SuddenDegradation()
        new_degradation.from_dict(dictionary)
        self.assertEqual(self.degradation, new_degradation)


if __name__ == "__main__":
    unittest.main()
