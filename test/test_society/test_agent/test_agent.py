import unittest
from copy import deepcopy

from piperabm.society.agent.samples import agent_0
from piperabm.resource.samples import resource_rate_0
from piperabm.unit import DT


class TestAgentClass(unittest.TestCase):

    def setUp(self):
        self.agent = deepcopy(agent_0)

    def test_add_resource(self):
        self.agent + resource_rate_0
        print(self.agent.resource)

    def test_fuel_consumption_idle(self):
        self.agent.idle_time_pass(DT(days=7))
        self.assertTrue(self.agent.alive)
        self.agent.idle_time_pass(DT(days=1))
        self.assertFalse(self.agent.alive)
    
    
if __name__ == "__main__":
    unittest.main()