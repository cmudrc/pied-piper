import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_0, environment_1
from piperabm.environment.items import Junction, Settlement, Road


class TestEnvironmentClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_0)
    
    def test_all_edges(self):
        self.assertEqual(len(self.env.all_edges()), 1)

    def test_add_node_proximity_node(self):
        ''' new item is in proximity of other items '''
        env = deepcopy(self.env)
        new_item = Junction(pos=[0.05, 0])
        env.add(new_item)
        self.assertEqual(len(env.all_nodes()), 2)
    
    def test_add_node_proximity_edge(self):
        ''' new item is in proximity of an existing edge '''
        env = deepcopy(self.env)
        new_item = Junction(pos=[1, 1])
        env.add(new_item)
        self.assertEqual(len(env.all_nodes()), 3)
        self.assertEqual(len(self.env.all_edges()), 2)

    def test_sort_nodes_by_distance(self):
        nodes_distance = self.env.sort_nodes_by_distance(pos=[0.3, 0.4])
        nearest = nodes_distance[0]
        distance = nearest[0]
        index = nearest[1]
        item = self.env.get_node_object(index)
        self.assertEqual(item.name, 'Sample Junction')
        self.assertEqual(distance, 0.5)


class TestEnvironmentClass_1(unittest.TestCase):       

    def setUp(self) -> None:
        self.env = deepcopy(environment_1)

    def test_all_nodes(self):
        result = self.env.all_nodes()
        self.assertEqual(len(result), 5)

    def test_all_edges(self):
        result = self.env.all_edges()
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    unittest.main()