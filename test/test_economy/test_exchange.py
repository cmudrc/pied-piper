import unittest
from copy import deepcopy

from piperabm.resource import Resource
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.resource.samples import resource_0, resource_delta_0


class TestExchangeClass(unittest.TestCase):

    def setUp(self):
        self.exchange = deepcopy(exchange_rate_0)
        self.resource = deepcopy(resource_0)
        self.resource_delta = deepcopy(resource_delta_0)

    def test_rate(self):
        e = deepcopy(self.exchange)
        rate = e.rate('food', 'water')
        self.assertEqual(rate, 5)

    def test_resource_value(self):
        result = self.resource.value(exchange_rate=self.exchange)
        expected_result = {
            'food': 50,
            'water': 16,
        }
        self.assertDictEqual(result, expected_result)

    def test_delta_resource_value(self):
        dr = deepcopy(self.dr)
        result = dr.value(exchange_rate=self.exchange)
        expected_result = {
            'food': 50,
            'water': 16,
        }
        self.assertDictEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()