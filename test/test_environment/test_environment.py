import unittest
from copy import deepcopy

from piperabm.environment.sample import env_0, env_1
from piperabm.unit import Date, DT


class TestEnvironmentClass1(unittest.TestCase):

    env = env_0

    def test_find_node(self):
        env = deepcopy(self.env)
        index = env.find_node("John's Home")
        self.assertEqual(index, 0, msg="find node by name")
        index = env.find_node([-1, -1])
        self.assertEqual(index, 0, msg="find node by pos")
        index = env.find_node(0)
        self.assertEqual(index, 0, msg="find node by index")

    def test_edge_info_path(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        all_settlements = env.all_nodes('settlement')
        path = path_graph.edge_info(all_settlements[0], all_settlements[1], 'path')
        expected_result = [0, 2, 1]
        self.assertListEqual(path.path, expected_result)
        self.assertEqual(0, path.start_pos())
        self.assertEqual(1, path.end_pos())

    def test_path(self): ###########
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        all_settlements = env.all_nodes('settlement')
        path = path_graph.edge_info(all_settlements[0], all_settlements[1], 'path')
        #result = path.path
        #self.assertListEqual(result, expected_result)

    def test_all_settlements(self):
        settlements = self.env.all_nodes('settlement')
        self.assertEqual(len(settlements), 2)

    def test_node_info(self):
        env = deepcopy(self.env)
        info = env.node_info(
            node=0,
            property="boundary"
        )
        expected_result = [-2, -2]
        self.assertListEqual(info.center, expected_result)
        node_type = env.node_info("Peter's Home", 'type')
        self.assertEqual(node_type, 'settlement')

    def test_edge_info(self):
        env = deepcopy(self.env)
        info = env.edge_info(
            start="John's Home",
            end=[20, 0],
            property="initiation_date"
        )
        expected_result = Date(2020, 1, 2)
        self.assertEqual(info.year, expected_result.year)
        self.assertEqual(info.month, expected_result.month)
        self.assertEqual(info.day, expected_result.day)


class TestEnvironmentClass2(unittest.TestCase):

    env = env_1

    #env.show(Date.today(), Date.today()+DT(hours=1))

    def to_link_graph(self):
        env = deepcopy(self.env)
        start_date = Date.today()
        end_date = start_date + DT(days=3)
        link_graph = env.to_link_graph(start_date, end_date)

    def to_path_graph(self):
        env = deepcopy(self.env)
        start_date = Date.today()
        end_date = start_date + DT(days=3)
        path_graph = env.to_path_graph(start_date, end_date)


if __name__ == "__main__":
    unittest.main()