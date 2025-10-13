import unittest
from copy import deepcopy

from piperabm.economy.trade.nash_bargaining import NashBargaining as nb


class TestSingleResourceSolver_0(unittest.TestCase):

    def setUp(self):
        price = 10
        player_1 = {
            "id": 1,
            "type": "agent",
            "resource": 0,
            "enough_resource": 10,
            "balance": 200,
        }
        player_2 = {
            "id": 2,
            "type": "market",
            "resource": 100,
            "enough_resource": 100,
            "balance": 0,
        }
        self.players_initial = [player_1, player_2]

        # Solve
        transactions = nb.transactions(self.players_initial, price)
        self.players_final = nb.apply(deepcopy(self.players_initial), transactions)
        # self.players_final = nb.(deepcopy(self.players_initial), price)

    def test_solve(self):
        total_resource_initial = (
            self.players_initial[0]["resource"] + self.players_initial[1]["resource"]
        )
        total_resource_final = (
            self.players_final[0]["resource"] + self.players_final[1]["resource"]
        )
        self.assertAlmostEqual(total_resource_initial, total_resource_final, places=12)
        total_balance_initial = (
            self.players_initial[0]["balance"] + self.players_initial[1]["balance"]
        )
        total_balance_final = (
            self.players_final[0]["balance"] + self.players_final[1]["balance"]
        )
        self.assertAlmostEqual(total_balance_initial, total_balance_final, places=12)


class TestSingleResourceSolver_1(unittest.TestCase):

    def setUp(self):
        price = 10
        player_1 = {
            "id": 1,
            "type": "agent",
            "resource": 19,
            "enough_resource": 10,
            "balance": 100,
        }
        player_2 = {
            "id": 2,
            "type": "agent",
            "resource": 8,
            "enough_resource": 10,
            "balance": 100,
        }
        player_3 = {
            "id": 3,
            "type": "agent",
            "resource": 3,
            "enough_resource": 10,
            "balance": 10,
        }
        self.players_initial = [player_1, player_2, player_3]

        # Solve
        transactions = nb.transactions(deepcopy(self.players_initial), price)
        self.players_final = nb.apply(deepcopy(self.players_initial), transactions)

    def test_solve(self):
        total_resource_initial = (
            self.players_initial[0]["resource"]
            + self.players_initial[1]["resource"]
            + self.players_initial[2]["resource"]
        )
        total_resource_final = (
            self.players_final[0]["resource"]
            + self.players_final[1]["resource"]
            + self.players_final[2]["resource"]
        )
        self.assertAlmostEqual(total_resource_initial, total_resource_final, places=13)
        total_balance_initial = (
            self.players_initial[0]["balance"]
            + self.players_initial[1]["balance"]
            + self.players_initial[2]["balance"]
        )
        total_balance_final = (
            self.players_final[0]["balance"]
            + self.players_final[1]["balance"]
            + self.players_final[2]["balance"]
        )
        self.assertAlmostEqual(total_balance_initial, total_balance_final, places=13)


class TestSingleResourceSolver_2(unittest.TestCase):

    def setUp(self):
        price = 10
        player_1 = {
            "id": 1,
            "type": "market",
            "resource": 100,
            "enough_resource": 100,
            "balance": 0,
        }
        player_2 = {
            "id": 2,
            "type": "agent",
            "resource": 8,
            "enough_resource": 10,
            "balance": 100,
        }
        player_3 = {
            "id": 3,
            "type": "agent",
            "resource": 2,
            "enough_resource": 10,
            "balance": 100,
        }
        self.players_initial = [player_1, player_2, player_3]

        # Solve
        transactions = nb.transactions(self.players_initial, price)
        self.players_final = nb.apply(deepcopy(self.players_initial), transactions)

    def test_solve(self):
        player_1_final_resource = self.players_final[0]["resource"]
        player_2_final_resource = self.players_final[1]["resource"]
        player_3_final_resource = self.players_final[2]["resource"]
        self.assertAlmostEqual(player_1_final_resource, 90, places=10)
        self.assertAlmostEqual(player_2_final_resource, 10, places=10)
        self.assertAlmostEqual(player_3_final_resource, 10, places=10)

        player_1_final_balance = self.players_final[0]["balance"]
        player_2_final_balance = self.players_final[1]["balance"]
        player_3_final_balance = self.players_final[2]["balance"]
        self.assertAlmostEqual(player_1_final_balance, 100, places=9)
        self.assertAlmostEqual(player_2_final_balance, 80, places=10)
        self.assertAlmostEqual(player_3_final_balance, 20, places=10)


if __name__ == "__main__":
    unittest.main()
