import unittest
from copy import deepcopy

from piperabm.resource import ResourceRate
from piperabm.resource.samples import resource_rate_0


class TestResourceRateClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.rate = deepcopy(resource_rate_0)

    def test_call(self):
        rate = self.rate('food')
        self.assertEqual(rate, 6)

    def test_mul(self):
        self.rate * 2
        expected_result = {'energy': 6, 'food': 12, 'water': 8}
        self.assertDictEqual(self.rate.to_dict(), expected_result)

    def test_div(self):
        self.rate / 0.5
        expected_result = {'energy': 6, 'food': 12, 'water': 8}
        self.assertDictEqual(self.rate.to_dict(), expected_result)

    def test_dict(self):
        dictionary = self.rate.to_dict()
        expected_result = {'food': 6, 'water': 4, 'energy': 3}
        self.assertEqual(dictionary, expected_result)
        rate = ResourceRate()
        rate.from_dict(dictionary)
        self.assertEqual(rate, self.rate)

    def test_delta(self):
        rate_previous = deepcopy(self.rate)
        self.rate.db['food'].amount = 8
        delta = self.rate - rate_previous
        expected_delta = {'food': 2}
        self.assertDictEqual(delta, expected_delta)
        rate_previous + delta
        self.assertEqual(rate_previous, self.rate)


if __name__ == "__main__":
    unittest.main()
