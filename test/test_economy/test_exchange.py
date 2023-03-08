import unittest
from copy import deepcopy

from piperabm.resource import Resource
from piperabm.economy import Exchange


class TestExchangeClass(unittest.TestCase):

    def setUp(self):
        self.exchange = Exchange()
        self.exchange.add('food', 'wealth', 10)
        self.exchange.add('water', 'wealth', 2)
        self.exchange.add('energy', 'wealth', 5)

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

    def test_exchange_0(self):
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