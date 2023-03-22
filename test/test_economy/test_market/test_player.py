import unittest
from copy import deepcopy

from piperabm.economy.market import Player


class TestEconomyClass(unittest.TestCase):

    def setUp(self):
        p = Player(
            1,
            source={
                'food': 4,
                'water': 5,
            },
            demand={
                'food': 6,
                'water': 5,
            },
            wallet=10
        )
        self.p = p

    def test_to_delta_0(self):
        p = deepcopy(self.p)
        delta_source, delta_demand, delta_wealth = p.to_delta()
        expected_delta_source = {
            'food': 0,
            'water': 0,
        }
        self.assertDictEqual(delta_source.current_resource, expected_delta_source)
        expected_delta_demand = {
            'food': 0,
            'water': 0,
        }
        self.assertDictEqual(delta_demand.current_resource, expected_delta_demand)
        expected_delta_wallet = 0
        self.assertEqual(delta_wealth, expected_delta_wallet)

    def test_to_delta(self):
        p = deepcopy(self.p)
        p.new_source = {
            'food': 2,
            'water': 2,
        }
        p.new_demand = {
            'food': 10,
            'water': 5,
        }
        p.new_wallet = 20
        #result = p.delta()
        delta_source, delta_demand, delta_wealth = p.to_delta()
        expected_delta_source = {
            'food': 2,
            'water': 3,
        }
        self.assertDictEqual(delta_source.current_resource, expected_delta_source)
        expected_delta_demand = {
            'food': -4,
            'water': 0,
        }
        self.assertDictEqual(delta_demand.current_resource, expected_delta_demand)
        expected_delta_wallet = -10
        self.assertEqual(delta_wealth, expected_delta_wallet)


if __name__ == "__main__":
    unittest.main()