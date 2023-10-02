import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_0, environment_1, environment_2
from piperabm.environment.items import Junction, Road
from piperabm.time import Date


class TestEnvironmentClass_0(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_0)

    def test_new_index(self):
        self.assertNotEqual(self.env.new_index, self.env.new_index)
    
    def test_current_items(self):
        items = self.env.current_items(
            date_start=Date(2019, 12, 29),
            date_end=Date(2019, 12, 30)
        )
        self.assertEqual(len(items), 0)
        items = self.env.current_items(
            date_start=Date(2020, 1, 1),
            date_end=Date(2020, 1, 2)
        )
        self.assertEqual(len(items), 1)

    def test_filter_category(self):
        items = self.env.current_items(
            date_start=Date(2020, 1, 1),
            date_end=Date(2020, 1, 2)
        )
        filtered_items = self.env.filter_category(items, category='node')
        self.assertEqual(len(filtered_items), 1)
        filtered_items = self.env.filter_category(items, category='edge')
        self.assertEqual(len(filtered_items), 0)


class TestEnvironmentClass_1(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_to_infrastrucure_graph(self):
        date_start = Date(2020, 1, 1)
        date_end = Date(2020, 1, 2)
        infrastrucure = self.env.to_infrastrucure_graph(date_start, date_end)
        print(infrastrucure.G)


if __name__ == '__main__':
    unittest.main()