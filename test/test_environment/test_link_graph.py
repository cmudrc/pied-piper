import unittest
from copy import deepcopy

from piperabm.environment.sample import env_0
from piperabm.unit import Date, DT


class TestLinkGraph(unittest.TestCase):

    env = env_0

    def test_to_link_graph(self):
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
            link_graph = env.to_link_graph(start_date, end_date)
            nodes_count_dict[i] = link_graph.G.number_of_nodes()
            edges_count_dict[i] = link_graph.G.number_of_edges()
            start_date += delta
            end_date += delta
        expected_result = {0: 0, 1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 2, 11: 2, 12: 0, 13: 0, 14: 0}
        #print(nodes_count_dict)
        self.assertDictEqual(nodes_count_dict, expected_result)
        expected_result = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 1, 11: 1, 12: 0, 13: 0, 14: 0}
        #print(edges_count_dict)
        self.assertDictEqual(edges_count_dict, expected_result)

    def test_to_link_graph_1(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=12)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_link_graph_2(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 2)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_link_graph_3(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 3)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 1)

    def test_to_link_graph_4(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 4)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 1)

    def test_to_link_graph_5(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 5)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 3)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 2)

    def test_to_link_graph_6(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 11)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 3)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 2)
    
    def test_to_link_graph_7(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 13)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 1)

    def test_to_link_graph_8(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 15)
        env.update_elements(start_date, end_date)
        
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_link_graph_9(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 14)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_link_graph_10(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 13)
        end_date = Date(2020, 1, 15)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 1)

    def test_all_nodes(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 3)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        all_nodes = link_graph.all_nodes()
        settlement_nodes = link_graph.all_nodes('settlement')
        cross_nodes = link_graph.all_nodes('cross')
        self.assertListEqual(all_nodes, [0, 2])
        self.assertListEqual(settlement_nodes, [0])
        self.assertListEqual(cross_nodes, [2])


if __name__ == "__main__":
    unittest.main()