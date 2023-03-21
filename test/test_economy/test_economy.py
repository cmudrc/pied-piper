import unittest
from copy import deepcopy

from piperabm.economy import Economy
from piperabm.society.agent.sample import agent_0, agent_1
from piperabm.economy.exchange.sample import exchange_0 as exchange


class TestEconomyClass(unittest.TestCase):

    def setUp(self):
        agents = [agent_0, agent_1]
        eco = Economy(agents, exchange)
        self.eco = eco

    def test_all_nodes(self):
        eco = deepcopy(self.eco)
        result = eco.all_nodes()
        expected_result = [0, 1]
        self.assertListEqual(result, expected_result)

    def test_find_agent(self):
        eco = deepcopy(self.eco)
        agent = eco.find_agent(index=0)
        self.assertEqual(agent.index, 0)
        agent = eco.find_agent(index=1)
        self.assertEqual(agent.index, 1)

    def test_markets(self):
        eco = deepcopy(self.eco)
        markets = eco.create_markets()
        #print(markets)
        sorted_markets_index = eco.sort_markets(markets)
        expected_result = [1, 0]
        self.assertListEqual(sorted_markets_index, expected_result)

    def test_solve(self):
        eco = deepcopy(self.eco)
        eco.solve_biggest()


if __name__ == "__main__":
    unittest.main()