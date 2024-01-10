import unittest
from copy import deepcopy

from piperabm.society.agent.samples import agent_0
from piperabm.resources.samples import resources_0
from piperabm.time import DeltaTime, Date


class TestAgentClass(unittest.TestCase):

    def setUp(self):
        self.agent = deepcopy(agent_0)

    def test_update(self):
        self.assertTrue(self.agent.alive)
        balance_initial = self.agent.balance
        date_start = Date.today()
        date_end = date_start + DeltaTime(days=8)
        self.agent.update(date_start, date_end)
        self.assertFalse(self.agent.alive)
        self.assertEqual(self.agent.death_reason, "water")
        balance_final = self.agent.balance
        self.assertLess(balance_initial, balance_final)

    '''
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
    '''
    
if __name__ == "__main__":
    unittest.main()