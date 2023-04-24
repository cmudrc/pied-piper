import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_1
from piperabm.environment.structures.settlement.samples import settlement_0
from piperabm.environment.structures.road.samples import road_0
from piperabm.unit import Date


class TestCurrentClassQuery(unittest.TestCase):

    def setUp(self):
        env = deepcopy(environment_1)
        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 3)
        self.current = env.current(start_date, end_date)

    def test_all_indexes(self):
        indexes = self.current.all_indexes(type='all')
        self.assertListEqual(list(indexes), [0, 2])
        indexes = self.current.all_indexes(type='hub')
        self.assertListEqual(list(indexes), [2])
        indexes = self.current.all_indexes(type='settlement')
        self.assertListEqual(list(indexes), [0])

    def test_get_node_object(self):
        structure = self.current.get_node_object(0)
        self.assertEqual(structure, settlement_0)
        structure = self.current.get_node_object(1)
        self.assertEqual(structure, None)
        structure = self.current.get_node_object(2)
        self.assertEqual(structure, None)

    def test_get_node_pos(self):
        pos = self.current.get_node_pos(0)
        self.assertListEqual(pos, [-2, -2])
        pos = self.current.get_node_pos(1)
        self.assertEqual(pos, None)
        pos = self.current.get_node_pos(2)
        self.assertListEqual(pos, [20, 0])

    def test_get_edge_object(self):
        structure = self.current.get_edge_object(0, 2)
        #### road_0 has a different boundary
        structure = self.current.get_edge_object(2, 1)
        self.assertEqual(structure, None)

    def test_get_edge_pos(self):
        pos = self.current.get_edge_pos(0, 2)
        self.assertListEqual(pos, [9.0, -1.0])

    def test_find_node(self):
        index = self.current.find_node("John's Home")
        self.assertEqual(index, 0)
        index = self.current.find_node("Peter's Home")
        self.assertEqual(index, None)

    def test_node_degree(self):
        degree = self.current.node_degree(0)
        self.assertEqual(degree, 1)
        degree = self.current.node_degree(1)
        self.assertEqual(degree, None)
        degree = self.current.node_degree(2)
        self.assertEqual(degree, 1)

    def test_xylim(self):
        x_lim, y_lim = self.current.xy_lim()
        self.assertListEqual(x_lim, [-2, 20])
        self.assertListEqual(y_lim, [-2, 0])

    def test_size(self):
        size = self.current.size()
        self.assertListEqual(size, [22, 2])


if __name__ == "__main__":
    unittest.main()
