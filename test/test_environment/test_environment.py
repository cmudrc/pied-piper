import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.unit import Date, DT
from piperabm.degradation import DiracDelta
from piperabm.boundary import Circular


class TestEnvironmentClass(unittest.TestCase):

    env = Environment()

    env.add_settlement(
        name="John's Home",
        pos=[-2, -2],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 2),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        boundary=Circular(radius=5),
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

    def test_find_node(self):
        env = deepcopy(self.env)
        index = env.find_node("John's Home")
        self.assertEqual(index, 0, msg="find node by name")
        index = env.find_node([-1, -1])
        self.assertEqual(index, 0, msg="find node by pos")
        index = env.find_node(0)
        self.assertEqual(index, 0, msg="find node by index")

    def test_1(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=12)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_2(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 2)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_3(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 3)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_4(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 4)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_5(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 5)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 2)

    def test_6(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 2)

    def test_7(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 2)
    
    def test_8(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 12)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_9(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 13)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_10(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 14)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_route_info(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        all_settlements = env.all_settlements()
        route = path.route_info(all_settlements[0], all_settlements[1], 'path')
        expected_result = [0, 2, 1]
        self.assertListEqual(route, expected_result)

    def test_all_settlements(self):
        settlements = self.env.all_settlements()
        self.assertEqual(len(settlements), 2)

    def test_settlement_info(self):
        env = deepcopy(self.env)
        info = env.settlement_info(
            node="Peter's Home",
            property="initiation_date"
            )
        expected_result = Date(2020, 1, 4)
        self.assertEqual(info.year, expected_result.year)
        self.assertEqual(info.month, expected_result.month)
        self.assertEqual(info.day, expected_result.day)

    def test_node_type(self):
        env = deepcopy(self.env)
        node_type = env.node_type(1)
        self.assertEqual(node_type, 'settlement')

    def test_node_info(self):
        env = deepcopy(self.env)
        info = env.node_info(
            node_index=0,
            property="boundary"
        )
        expected_result = [-2, -2]
        self.assertListEqual(info.center, expected_result)

    def test_link_info(self):
        env = deepcopy(self.env)
        info = env.link_info(
            start="John's Home",
            end=[20, 0],
            property="initiation_date"
        )
        expected_result = Date(2020, 1, 2)
        self.assertEqual(info.year, expected_result.year)
        self.assertEqual(info.month, expected_result.month)
        self.assertEqual(info.day, expected_result.day)

    def test_size(self):
        env = deepcopy(self.env)
        x_lim, y_lim = env.size()
        expected_result = [-2, 20]
        self.assertListEqual(x_lim, expected_result)
        expected_result = [-2, 20]
        self.assertListEqual(y_lim, expected_result)


if __name__ == "__main__":
    unittest.main()