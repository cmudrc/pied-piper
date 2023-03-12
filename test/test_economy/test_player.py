import unittest
from copy import deepcopy

from piperabm.economy import Player


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

    def test_delta_0(self):
        p = deepcopy(self.p)
        result = p.delta()
        expected_result = {
            'source': {
                'food': 0,
                'water': 0,
            },
            'demand': {
                'food': 0,
                'water': 0,
            },
            'wallet': 0,
        }
        self.assertDictEqual(result, expected_result)

    def test_delta(self):
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
        result = p.delta()
        expected_result = {
            'source': {
                'food': -2,
                'water': -3,
            },
            'demand': {
                'food': 4,
                'water': 0,
            },
            'wallet': 10,
        }
        self.assertDictEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()