import unittest

from piperabm.model import Model
from piperabm.model.samples import model_3
from piperabm.infrastructure import Settlement
from piperabm.society import Agent
from piperabm.resources import Resources, Resource
from piperabm.economy import Trade
from piperabm.economy.exchange_rate.samples import exchange_rate_0 as exchange_rate


class TestTradeClass_0(unittest.TestCase):

    def setUp(self):
        model = Model(exchange_rate=exchange_rate)

        settlement = Settlement()
        model.add(settlement)

        food_0 = Resource(name="food", amount=100, max=100)
        water_0 = Resource(name="water", amount=0, max=100)
        energy_0 = Resource(name="energy", amount=0, max=100)
        resources_0 = Resources(food_0, water_0, energy_0)
        agent_0 = Agent(resources=resources_0, balance=100)
        food_1 = Resource(name="food", amount=0, max=100)
        water_1 = Resource(name="water", amount=80, max=100)
        energy_1 = Resource(name="energy", amount=0, max=100)
        resources_1 = Resources(food_1, water_1, energy_1)
        agent_1 = Agent(resources=resources_1, balance=100)
        food_2 = Resource(name="food", amount=0, max=100)
        water_2 = Resource(name="water", amount=0, max=100)
        energy_2 = Resource(name="energy", amount=90, max=100)
        resources_2 = Resources(food_2, water_2, energy_2)
        agent_2 = Agent(resources=resources_2, balance=100)
        model.add(agent_0, agent_1, agent_2)

        players = model.all_alive_agents

        self.trade = Trade(players, model)

    def test_best_transaction(self):
        transation = self.trade.best_transaction()
        self.assertEqual(transation["resource"], "food")

    def test_solve(self):
        self.trade.solve()
        transactions = self.trade.history
        self.assertEqual(transactions[0]["resource"], "food")
        self.assertEqual(transactions[1]["resource"], "energy")
        self.assertEqual(transactions[2]["resource"], "water")
        self.assertEqual(transactions[3]["resource"], "energy")
        self.assertEqual(transactions[4]["resource"], "energy")
        self.assertEqual(transactions[5]["resource"], "energy")


class TestTradeClass_1(unittest.TestCase):

    def setUp(self):
        players = model_3.all_alive_agents
        self.trade = Trade(players, model_3)

    def test_solve(self):
        self.trade.solve()
        transactions = self.trade.history
        self.assertEqual(transactions[0]["resource"], "food")
        self.assertEqual(transactions[1]["resource"], "food")
        self.assertEqual(transactions[2]["resource"], "food")


if __name__ == "__main__":
    unittest.main()