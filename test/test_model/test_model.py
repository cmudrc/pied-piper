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
        model = Model(
            society=self.society,
            step_size=DT(hours=12),
            current_date=Date(2020, 1, 1)
        )
        model.run(n=1)


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
        model = Model(
            society=self.society,
            step_size=DT(hours=12),
            current_date=Date(2020, 1, 1)
        )
        model.run(n=1)
    
    
if __name__ == "__main__":
    unittest.main()