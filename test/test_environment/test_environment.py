import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.tools import check_existance
from piperabm.unit import Date, DT
from piperabm.degradation import DiracDelta
from piperabm.boundary import Circular


class TestExistanecFunction(unittest.TestCase):

    start_date = Date(2020, 1, 2)
    end_date = Date(2020, 1, 4)

    def test_0(self):
        initiation_date = Date(2020, 1, 1)
        result = check_existance(initiation_date, None, None)
        self.assertTrue(result)

    def test_1(self):
        initiation_date = Date(2020, 1, 1)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)
    
    def test_2(self):
        initiation_date = Date(2020, 1, 2)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)

    def test_3(self):
        initiation_date = Date(2020, 1, 3)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)

    def test_4(self):
        initiation_date = Date(2020, 1, 4)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertFalse(result)

    def test_5(self):
        initiation_date = Date(2020, 1, 5)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertFalse(result)


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

    def test_9(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 14)
        env.update_elements(start_date, end_date)
        path = env.to_path(start_date, end_date)
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)


if __name__ == "__main__":
    unittest.main()