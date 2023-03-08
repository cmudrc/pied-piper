import unittest
from copy import deepcopy

from piperabm.environment.sample import env_0
from piperabm.unit import Date, DT


class TestPathGraph(unittest.TestCase):

    def setUp(self):
        self.env = env_0

    def test_to_path_graph(self):
        """
        Similar to the natural flow of program during simulation
        """
        env = deepcopy(self.env)
        nodes_count_dict = {} # {day: nodes_count}
        edges_count_dict = {} # {day: edges_count}
        start_date = Date(2020, 1, 1)
        delta = DT(days=1)
        end_date = start_date + delta
        for i in range(15):
            env.update_elements(start_date, end_date)
            path_graph = env.to_path_graph(start_date, end_date)
            nodes_count_dict[i] = path_graph.G.number_of_nodes()
            edges_count_dict[i] = path_graph.G.number_of_edges()
            start_date += delta
            end_date += delta
        expected_result = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 1, 11: 1, 12: 0, 13: 0, 14: 0}
        #print(nodes_count_dict)
        self.assertDictEqual(nodes_count_dict, expected_result)
        expected_result = {0: 0, 1: 0, 2: 0, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        #print(edges_count_dict)
        self.assertDictEqual(edges_count_dict, expected_result)

    def test_to_path_graph_1(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=12)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_path_graph_2(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 2)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_path_graph_3(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 3)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_path_graph_4(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 4)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_path_graph_5(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 5)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 2)

    def test_to_path_graph_6(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 2)
    
    def test_to_path_graph_7(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 12)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_path_graph_8(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 13)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_path_graph_9(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 14)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_path_graph_10(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 3)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)


if __name__ == "__main__":
    unittest.main()