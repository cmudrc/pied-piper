import unittest
from copy import deepcopy

from piperabm.resource import Resource, DeltaResource
from piperabm.economy import Exchange


class TestExchangeClass(unittest.TestCase):

    exchange = Exchange()
    exchange.add('food', 'wealth', 10)
    exchange.add('water', 'wealth', 2)
    exchange.add('energy', 'wealth', 5)

    r = Resource(
        current_resource={
            'food': 5,
            'water': 8,
        },
        max_resource={
            'food': 10,
            'water': 10,
        }
    )
    dr = DeltaResource(
        batch={
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
        self.assertDictEqual(result.batch, expected_result)

    def test_delta_resource_value(self):
        dr = deepcopy(self.dr)
        result = dr.value(exchange_rate=self.exchange)
        expected_result = {
            'food': 50,
            'water': 16,
        }
        self.assertDictEqual(result.batch, expected_result)


if __name__ == "__main__":
    unittest.main()