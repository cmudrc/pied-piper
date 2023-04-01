import unittest
from copy import deepcopy

from piperabm.resource import Resource
from piperabm.economy.exchange.sample import exchange_0


class TestExchangeClass(unittest.TestCase):

    def setUp(self):
        self.exchange = deepcopy(exchange_0)

        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            },
            max_resource={
                'food': 10,
                'water': 10,
            }
        )
        self.dr = Resource(
            {
                'food': 5,
                'water': 8,
            }
        )

    def test_exchange(self):
        e = deepcopy(self.exchange)
        rate = e.rate('food', 'water')
        self.assertEqual(rate, 5)

    def test_resource_value(self):
        r = deepcopy(self.r)
        result = r.value(exchange_rate=self.exchange)
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