import unittest

from piperabm.measures import Accessibility
from piperabm.measures.accessibility import average, average_geometric, average_list, average_weighted
from piperabm.time import Date


class TestAccessibilityClass_0(unittest.TestCase):
    """
    One agent, one resource, two time_steps
    """

    def setUp(self):
        self.measure = Accessibility()
        self.measure.library = {
            1: [
                {'food': 1,},
                {'food': 0.8,},
            ],
        }
        self.measure.dates = [
            Date(2020, 1, 1),
            Date(2020, 1, 2),
            Date(2020, 1, 4),
        ]

    def test_len(self):
        self.assertEqual(self.measure.len, 2)

    def test_accessibility(self):
        values = self.measure.accessibility(agents=1, resources='food')
        self.assertEqual(values, [1, 0.8])
        average = self.measure.average(values)
        expected_result = (1 * 1 + 0.8 * 2) / 3
        self.assertEqual(average, expected_result)

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

'''

class TestAccessibilityClass_0(unittest.TestCase):

    def setUp(self):
        self.measure = Accessibility()
        self.measure.library = {
            1: [
                {'food': 1,},
                {'food': 0.9,},
            ],
            2: [
                {'food': 0.8,},
                {'food': 0.5,},
            ],
        }
        self.measure.dates = [
            Date(2020, 1, 1),
            Date(2020, 1, 2),
            Date(2020, 1, 3),
        ]

    def test_len(self):
        self.assertEqual(self.measure.len, 2)

    def test_accessibility(self):
        # One agent
        values = self.measure.accessibility(agents=1, resources='food')
        self.assertEqual(values, [1, 0.9])
        average = self.measure.average(values)
        self.assertEqual(average, 0.95)

        # Two agents
        values = self.measure.accessibility(agents='all', resources='food')
        self.assertEqual(values, [1, 0.9])
        average = self.measure.average(values)
        self.assertEqual(average, 0.95)
'''

if __name__ == "__main__":
    unittest.main()
