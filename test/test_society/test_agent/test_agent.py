import unittest
from copy import deepcopy

from piperabm.society.agent.sample import agent_0
from piperabm.unit import DT


class TestAgentClass(unittest.TestCase):

    def setUp(self):
        self.agent = deepcopy(agent_0)

    def test_idle_time_pass(self):
        agent = deepcopy(self.agent)
        agent.idle_time_pass(DT(days=7))
        self.assertTrue(agent.alive)
        agent.idle_time_pass(DT(days=1))
        self.assertFalse(agent.alive)
    
    
if __name__ == "__main__":
    unittest.main()