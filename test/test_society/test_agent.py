import unittest
from copy import deepcopy

from piperabm import Agent
from piperabm.resource import Resource
from piperabm.unit import DT


class TestAgentClass(unittest.TestCase):

    def setUp(self):
        resource = Resource(
            current_resource={
                'food': 20,
                'water': 30,
                'energy': 40
            },
            max_resource={
                'food': 100,
                'water': 100,
                'energy': 100
            }
        )
        agent = Agent(
            name='John',
            origin_node='1',
            transportation=None,
            queue=None,
            resource=resource,
            idle_fuel_rate=None,
            balance=0,
            wealth_factor=1
        )

        self.agent = agent

    def test_idle_time_pass(self):
        agent = deepcopy(self.agent)
        agent.idle_time_pass(DT(days=7))
        self.assertTrue(agent.alive)
        agent.idle_time_pass(DT(days=1))
        self.assertFalse(agent.alive)
    
    
if __name__ == "__main__":
    unittest.main()