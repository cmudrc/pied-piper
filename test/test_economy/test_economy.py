import unittest
from copy import deepcopy

from piperabm.economy import Economy
from piperabm.society.agent.sample import agent_0, agent_1
from piperabm.economy.exchange.sample import exchange_0 as exchange


class TestEconomyClass(unittest.TestCase):

    def setUp(self):
        agent_1.current_node = agent_0.current_node # 0
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

    def test_create_markets(self):
        eco = deepcopy(self.eco)
        markets = eco.create_markets()
        #print(markets)
        self.assertEqual(len(markets), 2)

    def test_sort_markets(self):
        eco = deepcopy(self.eco)
        markets = eco.create_markets()
        sorted_markets_index = eco.sort_markets(markets)
        expected_result = [0, 1]
        self.assertListEqual(sorted_markets_index, expected_result)

    def test_biggest_market(self):
        eco = deepcopy(self.eco)
        biggest_market = eco.biggest_market()
        #print(biggest_market)

    def test_solve_biggest_market(self):
        eco = deepcopy(self.eco)
        #print(eco)
        stat = eco.solve_biggest_market()
        print(stat)
        #print(eco)


if __name__ == "__main__":
    unittest.main()