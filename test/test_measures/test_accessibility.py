import unittest

from piperabm.measures import Accessibility
from piperabm.measures.accessibility import average, average_geometric, average_list, average_weighted
from piperabm.time import Date


class TestAccessibilityClass_0(unittest.TestCase):
    """
    Two agent, one resource, two time_steps
    """

    def setUp(self):
        self.measure = Accessibility()
        self.measure.library = {
            1: [
                {'food': 1,},
                {'food': 0.8,},
            ],
            2: [
                {'food': 0.8,},
                {'food': 0.4,},
            ],
        }
        self.measure.dates = [
            Date(2020, 1, 1),
            Date(2020, 1, 2),
            Date(2020, 1, 4),
        ]

    def test_len(self):
        self.assertEqual(self.measure.len, 2)

    def test_accessibility_1a_gent(self):
        values = self.measure.accessibility(agents=1, resources='food')
        self.assertEqual(values, [1, 0.8])
        average = self.measure.average(values)
        expected_result = (1 * 1 + 0.8 * 2) / 3
        self.assertEqual(average, expected_result)

    def test_accessibility_2_agent(self):
        values = self.measure.accessibility(agents=[1, 2], resources='food')
        expected_result = [0.9, 0.6]
        for i in range(len(values)):
            self.assertAlmostEqual(values[i], expected_result[i], places=2)
        average = self.measure.average(values)
        expected_result = (0.9 * 1 + 0.6 * 2) / 3
        self.assertAlmostEqual(average, expected_result, places=2)

    def test_durations(self):
        durations = self.measure.durations()
        self.assertEqual(durations, [24 * 60 * 60, 2 * 24 * 60 * 60])
        accessibility_dictionary = self.measure.organize_data(agents=1, resources='food')
        self.assertDictEqual(accessibility_dictionary, {1: {'food': [1, 0.8]}})


class TestAccessibilityHelperFucntions(unittest.TestCase):

    def test_average(self):
        values = [1, 0.5, 0]
        result = average(values)
        self.assertEqual(result, 0.5)

    def test_average_geometric(self):
        values = [1, 0.5, 0]
        result = average_geometric(values)
        self.assertEqual(result, 0)

        values = [1, 1, 1]
        result = average_geometric(values)
        self.assertEqual(result, 1)

    def test_average_list(self):
        list_values = [
            [1, 0.9, 0],
            [1, 0.1, 0.1],
        ]
        result = average_list(list_values, method='normal')
        self.assertEqual(result, [1, 0.5, 0.05])

        result = average_list(list_values, method='geometric')
        expected_result = [1, 0.3, 0]
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected_result[i], places=2)

    def test_average_weighted(self):
        values = [1, 0.75, 0]
        weights = [1, 2, 2]
        result = average_weighted(values, weights)
        self.assertEqual(result, 0.5)


class TestAccessibilityClass_0(unittest.TestCase):

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

    def test_accessibility(self):
        # One agent, one resource
        values_1 = self.measure.accessibility(agents=1, resources='food')
        values_2 = self.measure.accessibility(agents=2, resources='food')
        self.assertEqual(values_1, [1.0, 0.9, 0.8, 0.7, 0.6])
        self.assertEqual(values_2, [0.8, 0.5, 0.2, 0, 0])
        average_1 = self.measure.average(values_1)
        self.assertEqual(average_1, 0.8)
        average_2 = self.measure.average(values_2)
        self.assertEqual(average_2, 0.3)

        # Two agents, one resource
        values = self.measure.accessibility(agents='all', resources='food')
        self.assertEqual(values, [0.9, 0.7, 0.5, 0.35, 0.3])
        average = self.measure.average(values)
        self.assertEqual(average, 0.55)

        # Two agents, all resources
        values = self.measure.accessibility(agents='all', resources='all')
        average = self.measure.average(values)
        self.assertAlmostEqual(average, 0.5055, places=2)


if __name__ == "__main__":
    unittest.main()
