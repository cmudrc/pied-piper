import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_0, environment_1
from piperabm.environment.items import Junction, Settlement, Road


class TestEnvironmentClass_0(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_0)

    def test_all_nodes(self):
        self.assertEqual(len(self.env.all_nodes()), 2)
    
    def test_all_edges(self):
        self.assertEqual(len(self.env.all_edges()), 1)

    def test_calculate_nodes_distance(self):
        nodes_distance = self.env.calculate_nodes_distance(pos=[1, 1])
        self.assertEqual(nodes_distance[0][0], nodes_distance[1][0])

    def test_calculate_edges_distance(self):
        edges_distance = self.env.calculate_edges_distance(pos=[1, 1])
        self.assertAlmostEqual(edges_distance[0][0], 0, places=1)

    def test_sort_nodes_by_distance(self):
        nodes_distance = self.env.sort_nodes_by_distance(pos=[0, 0])
        self.assertLess(nodes_distance[0][0], nodes_distance[1][0])

    def test_find_nearest_node(self):
        distance, index = self.env.find_nearest_node(pos=[0.1, 0.1])
        item = self.env.get_node_object(index)
        self.assertListEqual(item.pos, [0, 0])

    def test_find_nearest_edge(self):
        distance, indexes = self.env.find_nearest_edge(pos=[1.1, 1.1])
        item = self.env.get_edge_object(*indexes)
        self.assertListEqual(item.pos_1, [0.05, 0])
        self.assertListEqual(item.pos_2, [2, 2])

    def test_add_node_proximity_node(self):
        ''' new node is getting added in proximity of an existing node '''
        env = deepcopy(self.env)
        new_item = Junction(pos=[0.05, 0])
        env.add(new_item)
        self.assertEqual(len(env.all_nodes()), 2)
    
    def test_add_node_proximity_edge(self):
        ''' new node is getting added in proximity of an existing edge '''
        env = deepcopy(self.env)
        new_item = Junction(pos=[1, 1])
        env.add(new_item)
        self.assertEqual(len(env.all_nodes()), 3)
        self.assertEqual(len(env.all_edges()), 2)


class TestEnvironmentClass_1(unittest.TestCase):       

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_all_nodes(self):
        result = self.env.all_nodes()
        self.assertEqual(len(result), 5)

    def test_all_edges(self):
        result = self.env.all_edges()
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    unittest.main()