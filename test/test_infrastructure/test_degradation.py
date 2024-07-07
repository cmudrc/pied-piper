import unittest
from copy import deepcopy

from piperabm.society.samples.society_1 import model


class TestDegradationClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model)
        self.id_agent = self.model.society.agents[0] # Agent
        self.id_start = self.model.society.get_home_id(id=self.id_agent) # Home
        self.id_end = self.model.infrastructure.markets[0] # Market
        self.model.society.go_and_comeback_and_stay(agent_id=self.id_agent, destination_id=self.id_end)

    def test_degradation(self):
        street = self.model.infrastructure.streets[0]
        length = self.model.infrastructure.get_length(ids=street)

        # Initial
        adjusted_length_0 = self.model.infrastructure.get_adjusted_length(ids=street)
        self.assertEqual(length, adjusted_length_0) # Adjusted length
        usage_impact = self.model.infrastructure.get_usage_impact(ids=street)
        self.assertEqual(usage_impact, 0) # Usage impact
        climate_impact = self.model.infrastructure.get_climate_impact(ids=street)
        self.assertEqual(climate_impact, 0) # Climate impact
        degradation = self.model.infrastructure.degradation(ids=street)
        self.assertEqual(degradation, 0) # Degradation

        # Run
        self.model.run(n=1, step_size=500)

        # Final
        adjusted_length_1 = self.model.infrastructure.get_adjusted_length(ids=street)
        self.assertLess(adjusted_length_0, adjusted_length_1) # Adjusted length
        usage_impact = self.model.infrastructure.get_usage_impact(ids=street)
        self.assertEqual(usage_impact, 1) # Usage impact
        climate_impact = self.model.infrastructure.get_climate_impact(ids=street)
        self.assertNotEqual(climate_impact, 0) # Climate impact
        degradation = self.model.infrastructure.degradation(ids=street)
        self.assertLess(1, degradation) # Degradation

if __name__ == "__main__":
    unittest.main()