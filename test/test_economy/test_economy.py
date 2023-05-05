import unittest
from copy import deepcopy

from piperabm.economy import Economy
from piperabm.society.agent.samples import sample_agent_0, sample_agent_1
from piperabm.economy.exchange.sample import exchange_0 as exchange


class TestEconomyClass_0Agents(unittest.TestCase):

    def setUp(self):
        agents = []
        eco = Economy(agents, exchange)
        self.eco = eco

    def test_all_nodes(self):
        eco = deepcopy(self.eco)
        result = eco.all_nodes()
        self.assertListEqual(result, [])

    def test_create_markets(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        self.assertDictEqual(eco.markets, {})

    def test_sort_markets(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        sorted_markets_index = eco.sort_markets()
        self.assertListEqual(sorted_markets_index, [])
    
    def test_biggest_market(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        biggest_market = eco.biggest_market()
        self.assertEqual(biggest_market, None)

    def test_solve_biggest_market(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        #print(eco)
        stat = eco.solve_biggest_market()
        self.assertDictEqual(stat, {})
        #print(stat)
        #print(eco)


class TestEconomyClass(unittest.TestCase):

    def setUp(self):
        agent_0 = deepcopy(sample_agent_0)
        agent_1 = deepcopy(sample_agent_1)
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

    def test_size(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        #print(eco.size())

    def test_create_markets(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        #print(markets)
        self.assertEqual(len(eco.markets), 2)

    def test_sort_markets(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        sorted_markets_index = eco.sort_markets()
        expected_result = [0, 1]
        self.assertListEqual(sorted_markets_index, expected_result)

    def test_biggest_market(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        biggest_market = eco.biggest_market()
        #print(biggest_market)

    def test_solve_biggest_market(self):
        eco = deepcopy(self.eco)
        eco.create_markets()
        #print(eco)
        stat = eco.solve_biggest_market()
        #print(stat)
        #print(eco)


if __name__ == "__main__":
    unittest.main()