import unittest
from copy import deepcopy

from piperabm.society.agent.samples import agent_0
from piperabm.resource.samples import resource_delta_0 as resource_delta
from piperabm.unit import DT


class TestAgentClass(unittest.TestCase):

    def setUp(self):
        self.agent = deepcopy(agent_0)

    def test_add_resource(self):
        remaining = self.agent + resource_delta
        expected_result = {
            'food': {'max': 100, 'min': 0, 'amount': 26},
            'water': {'max': 100, 'min': 0, 'amount': 34},
            'energy': {'max': 100, 'min': 0, 'amount': 43}
        }
        self.assertDictEqual(self.agent.resource.to_dict(), expected_result)
        self.assertTrue(remaining.is_all_zero())

    def test_sub_resource(self):
        remaining = self.agent - resource_delta
        expected_result = {
            'food': {'max': 100, 'min': 0, 'amount': 14},
            'water': {'max': 100, 'min': 0, 'amount': 26},
            'energy': {'max': 100, 'min': 0, 'amount': 37}
        }
        self.assertDictEqual(self.agent.resource.to_dict(), expected_result)
        self.assertTrue(remaining.is_all_zero())

    def test_fuel_consumption_idle(self):
        fuel_consumption = self.agent.fuel_consumption_idle(duration=DT(days=7))
        self.agent - fuel_consumption
        self.assertTrue(self.agent.alive)

        fuel_consumption = self.agent.fuel_consumption_idle(duration=DT(days=1))
        remaining = self.agent - fuel_consumption
        self.assertFalse(self.agent.alive)
        self.assertFalse(remaining.is_all_zero())
        self.assertListEqual(self.agent.death_reason, ['water'])
    
    
if __name__ == "__main__":
    unittest.main()