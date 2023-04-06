import unittest
from copy import deepcopy

from piperabm import Model, Society
from piperabm.unit import Date, DT

from piperabm.economy.exchange.sample import exchange_0
from piperabm.environment.sample import env_0
from piperabm.society.agent.sample import sample_agent_0, sample_agent_1


class TestSocietyClass_0(unittest.TestCase):
    """
    Single agent
    """

    def setUp(self):
        society = Society(
            env=deepcopy(env_0),
            gini=0.3,
            exchange_rate=deepcopy(exchange_0)
        )
        agents = [
            deepcopy(sample_agent_0)
        ]
        society.add(agents)
        self.society = society

    def test_(self):
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=12)
        self.society.env.update_elements(start_date, end_date)
        # env
        self.assertListEqual(list(self.society.env.G.nodes()), [0, 1, 2])
        self.assertListEqual(list(self.society.env.G.edges()), [(0, 2), (1, 2)])
        # link graph
        self.assertListEqual(list(self.society.env.link_graph.G.nodes()), [])
        self.assertListEqual(list(self.society.env.link_graph.G.edges()), [])
        self.society.update_elements(start_date, end_date)


class TestSocietyClass_1(unittest.TestCase):
    """
    Two agents
    """

    def setUp(self):
        society = Society(
            env=deepcopy(env_0),
            gini=0.3,
            exchange_rate=deepcopy(exchange_0)
        )
        agents = [
            deepcopy(sample_agent_0),
            deepcopy(sample_agent_1)
        ]
        society.add(agents)
        self.society = society

    def test_(self):
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=12)
        self.society.env.update_elements(start_date, end_date)
        # env
        self.assertListEqual(list(self.society.env.G.nodes()), [0, 1, 2])
        self.assertListEqual(list(self.society.env.G.edges()), [(0, 2), (1, 2)])
        # link graph
        self.assertListEqual(list(self.society.env.link_graph.G.nodes()), [])
        self.assertListEqual(list(self.society.env.link_graph.G.edges()), [])
        self.society.update_elements(start_date, end_date)
    

if __name__ == "__main__":
    unittest.main()