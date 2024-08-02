import unittest
from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_1 import model as model_0
from piperabm.society.samples.society_1 import model as model_1


class TestDegradationClass_0(unittest.TestCase):
    """
    No agent activity
    """

    def setUp(self) -> None:
        self.model = deepcopy(model_0)

    def test_degradation(self):
        street = self.model.infrastructure.streets[0]
        length = self.model.infrastructure.get_length(ids=street)
        
        # Initial
        adjusted_length_initial = self.model.infrastructure.get_adjusted_length(ids=street)
        self.assertEqual(length, adjusted_length_initial) # Adjusted length
        usage_impact_initial = self.model.infrastructure.get_usage_impact(ids=street)
        self.assertEqual(usage_impact_initial, 0) # Usage impact
        climate_impact_initial = self.model.infrastructure.get_climate_impact(ids=street)
        self.assertEqual(climate_impact_initial, 0) # Climate impact
        adjustment_factor_initial = self.model.infrastructure.adjustment_factor(ids=street)
        self.assertEqual(adjustment_factor_initial, 1) # Adjustment factor

        # Run
        self.model.update(duration=10)

        # Final
        adjusted_length_final = self.model.infrastructure.get_adjusted_length(ids=street)
        self.assertLess(adjusted_length_initial, adjusted_length_final) # Adjusted length
        usage_impact_final = self.model.infrastructure.get_usage_impact(ids=street)
        self.assertEqual(usage_impact_final, 0) # Usage impact
        climate_impact_final = self.model.infrastructure.get_climate_impact(ids=street)
        self.assertNotEqual(climate_impact_final, 0) # Climate impact
        adjustment_factor_final = self.model.infrastructure.adjustment_factor(ids=street)
        self.assertLess(1, adjustment_factor_final) # Adjustment factor
    

class TestDegradationClass_1(unittest.TestCase):
    """
    With agent activity
    """

    def setUp(self) -> None:
        self.model = deepcopy(model_1)
        self.id_agent = self.model.society.agents[0] # Agent
        self.id_start = self.model.society.get_home_id(id=self.id_agent) # Home
        self.id_end = self.model.infrastructure.markets[0] # Market
        self.model.society.go_and_comeback_and_stay(agent_id=self.id_agent, destination_id=self.id_end, duration=50)

    def test_degradation(self):
        street = self.model.infrastructure.streets[0]
        length = self.model.infrastructure.get_length(ids=street)

        # Initial
        adjusted_length_initial = self.model.infrastructure.get_adjusted_length(ids=street)
        self.assertEqual(length, adjusted_length_initial) # Adjusted length
        usage_impact = self.model.infrastructure.get_usage_impact(ids=street)
        self.assertEqual(usage_impact, 0) # Usage impact
        climate_impact = self.model.infrastructure.get_climate_impact(ids=street)
        self.assertEqual(climate_impact, 0) # Climate impact

        # Run
        self.model.update(duration=500)

        # Final
        adjusted_length_final = self.model.infrastructure.get_adjusted_length(ids=street)
        self.assertLess(adjusted_length_initial, adjusted_length_final) # Adjusted length
        usage_impact = self.model.infrastructure.get_usage_impact(ids=street)
        self.assertEqual(usage_impact, 1) # Usage impact
        climate_impact = self.model.infrastructure.get_climate_impact(ids=street)
        self.assertNotEqual(climate_impact, 0) # Climate impact

        # Top degraded
        edges = self.model.infrastructure.top_degraded_edges(percent=100)
        self.assertListEqual(list(edges[0]), list(street))


if __name__ == "__main__":
    unittest.main()