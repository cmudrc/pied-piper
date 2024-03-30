import unittest

from piperabm.measures import Accessibility
from piperabm.time import Date


class TestAccessibilityClass(unittest.TestCase):

    def setUp(self):
        self.measure = Accessibility()
        self.measure.library = {
            1: [
                {
                    'food': 1,
                    'water': 1,
                    'energy': 1,
                },
                {
                    'food': 0.9,
                    'water': 0.8,
                    'energy': 0.7,
                },
                {
                    'food': 0.8,
                    'water': 0.7,
                    'energy': 0.6,
                },
                {
                    'food': 0.7,
                    'water': 0.6,
                    'energy': 0.5,
                },
                {
                    'food': 0.6,
                    'water': 0.5,
                    'energy': 0.4,
                },
            ],
            2: [
                {
                    'food': 0.8,
                    'water': 0.7,
                    'energy': 0.6,
                },
                {
                    'food': 0.5,
                    'water': 0.6,
                    'energy': 0.4,
                },
                {
                    'food': 0.2,
                    'water': 0.4,
                    'energy': 0.3,
                },
                {
                    'food': 0,
                    'water': 0.3,
                    'energy': 0.2,
                },
                {
                    'food': 0,
                    'water': 0.3,
                    'energy': 0.2,
                },
            ],
        }
        self.measure.dates = [
            Date(2020, 1, 1),
            Date(2020, 1, 2),
            Date(2020, 1, 3),
            Date(2020, 1, 4),
            Date(2020, 1, 5),
            Date(2020, 1, 6),
        ]

    def test_len(self):
        self.assertEqual(self.measure.len, 5)

    def test_agent_resource_accessilibity(self):
        values = self.measure.agent_resource_accessilibity(id=1, resource_name='food')
        self.assertListEqual(values, [1, 0.9, 0.8, 0.7, 0.6])
        average = self.measure.average(values)
        self.assertAlmostEqual(average, 0.8, places=2)

    def test_agent_resources_accessibility(self):
        values = self.measure.agent_resources_accessibility(id=1)
        self.assertListEqual(values, [1.0, 0.7958114415792784, 0.6952053289772899, 0.594392195276313, 0.49324241486609405])
        average = self.measure.average(values)
        self.assertAlmostEqual(average, 0.7157302761397951, places=2)

    def test_agents_resource_accessibility(self):
        values = self.measure.agents_resource_accessibility(resource_name='food')
        self.assertListEqual(values, [0.9, 0.7, 0.5, 0.35, 0.3])
        average = self.measure.average(values)
        self.assertAlmostEqual(average, 0.55, places=2)

    def test_agents_resources_accessibility(self):
        values = self.measure.agents_resources_accessibility()
        self.assertListEqual(values, [0.8490184748775548, 0.6459311910914377, 0.4983277467062982, 0.3805831305510122, 0.3301927248894627])
        average = self.measure.average(values)
        self.assertAlmostEqual(average, 0.540810653623153, places=2)


if __name__ == "__main__":
    unittest.main()
