import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_1
from piperabm.unit import Date


class TestCurrentClass(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_to_current_0(self):
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 2)
        current_graph = self.env.current(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 0)
        self.assertEqual(len(current_graph.G.edges()), 0)

    def test_to_current_0(self):
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 2)
        current_graph = self.env.current(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 0)
        self.assertEqual(len(current_graph.G.edges()), 0)

    def test_to_current_1(self):
        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 3)
        current_graph = self.env.current(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 2)
        self.assertEqual(len(current_graph.G.edges()), 1)

    def test_to_current_2(self):
        start_date = Date(2020, 1, 3)
        end_date = Date(2020, 1, 4)
        current_graph = self.env.current(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 2)
        self.assertEqual(len(current_graph.G.edges()), 1)

    def test_to_current_3(self):
        start_date = Date(2020, 1, 4)
        end_date = Date(2020, 1, 5)
        current_graph = self.env.current(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 3)
        self.assertEqual(len(current_graph.G.edges()), 2)


if __name__ == "__main__":
    unittest.main()