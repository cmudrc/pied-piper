import unittest
from copy import deepcopy

from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.resources.samples import resources_0
from piperabm.resources.resource.samples import resource_0


class TestExchangeRateClass(unittest.TestCase):

    def setUp(self):
        self.exchange_rate = deepcopy(exchange_rate_0)
        self.resources = deepcopy(resources_0)

    def test_rate(self):
        expected_result = 5
        rate = self.exchange_rate.rate('food', 'water')
        self.assertEqual(rate, expected_result)
        rate = self.exchange_rate('food', 'water')
        self.assertEqual(rate, expected_result)
        rate = self.exchange_rate('water', 'food')
        self.assertEqual(rate, 1 / expected_result)

    def test_value(self):
        value = self.exchange_rate.value(resource_0)
        expected_result = 30 * 10
        self.assertEqual(value, expected_result)
        value = self.exchange_rate.value(resources_0)
        expected_result = (30 * 10) + (40 * 2) + (40 * 4)
        self.assertEqual(value, expected_result)

    def test_names(self):
        names = self.exchange_rate.names
        expected_result = ['food', 'wealth', 'water', 'energy']
        self.assertListEqual(names, expected_result)

    def test_serialization(self):
        dictionary = self.exchange_rate.serialize()
        expected_result = {
            'food': 10,
            'water': 2,
            'energy': 4,
        }
        self.assertDictEqual(dictionary, expected_result)
        exchange_rate = ExchangeRate()
        exchange_rate.deserialize(expected_result)
        self.assertEqual(exchange_rate, self.exchange_rate)


if __name__ == "__main__":
    unittest.main()