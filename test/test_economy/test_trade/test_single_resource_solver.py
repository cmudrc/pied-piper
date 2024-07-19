import unittest
from copy import deepcopy

from piperabm.economy.trade.single_resource_solver import solver


class TestSingleResourceSolver_0(unittest.TestCase):

    def setUp(self):
        price = 10
        player_1 = {
            'id': 1,
            'type': 'agent',
            'resource': 19,
            'enough_resource': 10,
            'balance': 100,
        }
        player_2 = {
            'id': 2,
            'type': 'agent',
            'resource': 8,
            'enough_resource': 10,
            'balance': 100,
        }
        player_3 = {
            'id': 3,
            'type': 'agent',
            'resource': 3,
            'enough_resource': 10,
            'balance': 10,
        }
        self.players_initial = [player_1, player_2, player_3]

        # Solve
        self.players_final = solver(deepcopy(self.players_initial), price)

    def test_solve(self):
        total_resource_initial = self.players_initial[0]['resource'] + self.players_initial[1]['resource'] + self.players_initial[2]['resource']
        total_resource_final = self.players_final[0]['resource'] + self.players_final[1]['resource'] + self.players_final[2]['resource']
        self.assertAlmostEqual(total_resource_initial, total_resource_final, places=13)
        total_balance_initial = self.players_initial[0]['balance'] + self.players_initial[1]['balance'] + self.players_initial[2]['balance']
        total_balance_final = self.players_final[0]['balance'] + self.players_final[1]['balance'] + self.players_final[2]['balance']
        self.assertAlmostEqual(total_balance_initial, total_balance_final, places=13)


if __name__ == "__main__":
    unittest.main()