import unittest
from copy import deepcopy

from piperabm.degradation.progressive import ProgressiveDegradation


class TestDiracDeltaClass(unittest.TestCase):

    def setUp(self):
        degradation = ProgressiveDegradation(
            usage_current=0,
            usage_max=10
        )
        degradation.add_usage(amount=3)
        self.degradation = degradation

    def test_ratio(self):
        ratio = self.degradation.ratio()
        self.assertEqual(ratio, 0.3)

    def test_factor(self):
        factor = self.degradation.factor()
        self.assertAlmostEqual(factor, 1.35, places=2)

    def test_to_dict(self):
        dictionary = self.degradation.to_dict()
        expected_result = {
            'usage_max': 10,
            'usage_current': 3,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(dictionary, expected_result)

    def test_from_dict(self):
        dictionary = self.degradation.to_dict()
        new_degradation = ProgressiveDegradation()
        new_degradation.from_dict(dictionary)
        new_dictionary = new_degradation.to_dict()
        expected_result = {
            'usage_max': 10,
            'usage_current': 3,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(new_dictionary, expected_result)

    def test_eq(self):
        dictionary = self.degradation.to_dict()
        new_degradation = ProgressiveDegradation()
        new_degradation.from_dict(dictionary)
        self.assertEqual(self.degradation, new_degradation)

    def test_sub(self):
        dictionary = self.degradation.to_dict()
        new_degradation = ProgressiveDegradation()
        new_degradation.from_dict(dictionary)
        new_degradation.add_usage(amount=2)
        delta = new_degradation - self.degradation
        expected_result = {
            'usage_current': 2,
        }
        self.assertDictEqual(delta, expected_result)

    def test_add(self):
        degradation = deepcopy(self.degradation)
        delta = {
            'usage_current': 2,
        }
        new_degradation = deepcopy(degradation)
        new_degradation + delta
        new_dictionary = new_degradation.to_dict()
        expected_result = {
            'usage_max': 10,
            'usage_current': 5,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(new_dictionary, expected_result)


if __name__ == "__main__":
    unittest.main()