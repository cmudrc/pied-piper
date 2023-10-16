import unittest
from copy import deepcopy

#from piperabm.resource import Resource
from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.resources.samples import resource_0, resource_delta_0


class TestExchangeRateClass(unittest.TestCase):

    def setUp(self):
        self.exchange_rate = deepcopy(exchange_rate_0)
        self.resource = deepcopy(resource_0)
        self.resource_delta = deepcopy(resource_delta_0)

    def test_rate(self):
        rate = self.exchange_rate.rate('food', 'water')
        self.assertEqual(rate, 5)
        rate = self.exchange_rate('food', 'water')
        self.assertEqual(rate, 5)

    def test_value(self):
        value = self.exchange_rate.value(resource_0)
        expected_result = {'food': 60.0, 'water': 16.0, 'energy': 76.0}
        self.assertDictEqual(value, expected_result)
        value = self.exchange_rate.value(resource_delta_0)
        expected_result = {'food': 60.0, 'water': 8.0, 'energy': 12.0}
        self.assertDictEqual(value, expected_result)

    def test_dict(self):
        dictionary = self.exchange_rate.to_dict()
        expected_result = {
            'food': {'to': 'wealth', 'rate': 10},
            'wealth': {'to': 'water', 'rate': 0.5},
            'wealth': {'to': 'energy', 'rate': 0.25}
        }
        self.assertDictEqual(dictionary, expected_result)
        exchange_rate = ExchangeRate()
        exchange_rate.from_dict(expected_result)
        self.assertEqual(exchange_rate, self.exchange_rate)


if __name__ == "__main__":
    unittest.main()