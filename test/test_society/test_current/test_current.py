import unittest
from copy import deepcopy

from piperabm.society.samples import society_1
from piperabm.unit import Date


class TestSocietyCurrentClass(unittest.TestCase):

    def setUp(self):
        self.society = deepcopy(society_1)

    def test_to_current_0(self):
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 2)
        current_graph = self.society.to_current_graph(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 0)
        self.assertEqual(len(current_graph.G.edges()), 0)

    def test_to_current_1(self):
        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 3)
        current_graph = self.society.to_current_graph(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 1)
        self.assertEqual(len(current_graph.G.edges()), 0)

    def test_to_current_2(self):
        start_date = Date(2020, 1, 3)
        end_date = Date(2020, 1, 4)
        current_graph = self.society.to_current_graph(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 1)
        self.assertEqual(len(current_graph.G.edges()), 0)

    def test_to_current_3(self):
        start_date = Date(2020, 1, 4)
        end_date = Date(2020, 1, 5)
        current_graph = self.society.to_current_graph(start_date, end_date)
        self.assertEqual(len(current_graph.G.nodes()), 2)
        self.assertEqual(len(current_graph.G.edges()), 1)


if __name__ == "__main__":
    unittest.main()