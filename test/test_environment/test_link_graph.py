import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.unit import Date, DT
from piperabm.degradation import DiracDelta
from piperabm.boundary import Circular


class TestEnvironmentClass1(unittest.TestCase):

    env = Environment(links_unit_length=10)

    env.add_settlement(
        name="John's Home",
        pos=[-2, -2],
        initiation_date=Date(2020, 1, 2),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        initiation_date=Date(2020, 1, 4),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

    env.add_link(
        "John's Home",
        [20, 0],
        initiation_date=Date(2020, 1, 2),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_link(
        [20.3, 0.3],
        "Peter's Home",
        initiation_date=Date(2020, 1, 4),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

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
        self.assertEqual(nodes_count, 1) # cross remains!
        edges_count = link_graph.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_to_link_graph_9(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 14)
        env.update_elements(start_date, end_date)
        link_graph = env.to_link_graph(start_date, end_date)
        nodes_count = link_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
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