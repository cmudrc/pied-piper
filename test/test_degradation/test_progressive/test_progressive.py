import unittest
from copy import deepcopy

from piperabm.degradation.progressive import ProgressiveDegradation


class TestProgressiveDegradationClass(unittest.TestCase):

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

    def test_dict(self):
        dictionary = self.degradation.to_dict()
        expected_result = {
            'usage_max': 10,
            'usage_current': 3,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(dictionary, expected_result)
        new_degradation = ProgressiveDegradation()
        new_degradation.from_dict(dictionary)
        self.assertEqual(new_degradation, self.degradation)

    def test_delta(self):
        degradation = deepcopy(self.degradation)
        delta = {
            'usage_max': 2,
            'usage_current': 2,
        }
        print(degradation)
        degradation + delta
        expected_result = {
            'formula_name': 'formula_01',
            'usage_max': 12,
            'usage_current': 5,
        }
        self.assertDictEqual(degradation.to_dict(), expected_result)
        degradation_old = deepcopy(self.degradation)
        self.assertEqual(degradation - degradation_old, delta)


class TestProgressiveDegradationClass_usage_max_None(unittest.TestCase):

    def setUp(self):
        degradation = ProgressiveDegradation(
            usage_current=0,
            usage_max=None
        )
        degradation.add_usage(amount=3)
        self.degradation = degradation

    def test_ratio(self):
        ratio = self.degradation.ratio()
        self.assertEqual(ratio, 0)

    def test_factor(self):
        factor = self.degradation.factor()
        self.assertEqual(factor, 1)

    def test_dict(self):
        dictionary = self.degradation.to_dict()
        expected_result = {
            'usage_max': float('inf'),
            'usage_current': 3,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(dictionary, expected_result)
        new_degradation = ProgressiveDegradation()
        new_degradation.from_dict(dictionary)
        self.assertEqual(new_degradation, self.degradation)

    def test_delta(self):
        degradation = deepcopy(self.degradation)
        delta = {
            'usage_current': 2,
        }
        degradation + delta
        expected_result = {
            'usage_max': float('inf'),
            'usage_current': 5,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(degradation.to_dict(), expected_result)
        degradation_old = deepcopy(self.degradation)
        self.assertEqual(degradation - degradation_old, delta)


class TestProgressiveDegradationClass_usage_max_inf(unittest.TestCase):

    def setUp(self):
        degradation = ProgressiveDegradation(
            usage_current=0
        ) # usage_max = inf (as default)
        degradation.add_usage(amount=3)
        self.degradation = degradation

    def test_ratio(self):
        ratio = self.degradation.ratio()
        self.assertEqual(ratio, 0)

    def test_factor(self):
        factor = self.degradation.factor()
        self.assertEqual(factor, 1)

    def test_dict(self):
        dictionary = self.degradation.to_dict()
        expected_result = {
            'usage_max': float('inf'),
            'usage_current': 3,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(dictionary, expected_result)
        new_degradation = ProgressiveDegradation()
        new_degradation.from_dict(dictionary)
        print(new_degradation)
        self.assertEqual(new_degradation, self.degradation)

    def test_delta(self):
        degradation = deepcopy(self.degradation)
        delta = {
            'usage_current': None,
        }
        degradation + delta
        expected_result = {
            'usage_max': float('inf'),
            'usage_current': 3,
            'formula_name': 'formula_01'
        }
        self.assertDictEqual(degradation.to_dict(), expected_result)
        degradation_old = deepcopy(self.degradation)
        self.assertEqual(degradation - degradation_old, None)


if __name__ == "__main__":
    unittest.main()