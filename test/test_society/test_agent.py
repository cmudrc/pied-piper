import unittest
from copy import deepcopy

from piperabm.society.agent.samples import agent_0
from piperabm.matter.containers.samples import containers_0 as resources
from piperabm.time import DeltaTime, Date


class TestAgentClass(unittest.TestCase):

    def setUp(self):
        self.agent = deepcopy(agent_0)

    def test_update(self):
        self.assertTrue(self.agent.alive)
        date_start = Date.today()
        date_end = date_start + DeltaTime(days=20)
        balance_initial = deepcopy(self.agent.balance)
        self.agent.update(date_start, date_end)
        self.assertFalse(self.agent.alive)
        self.assertEqual(self.agent.death_reason, 'water')
        balance_final = deepcopy(self.agent.balance)
        self.assertLess(balance_initial, balance_final)

    
if __name__ == '__main__':
    unittest.main()