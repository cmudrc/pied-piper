import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.items import Junction, Settlement, Road
from piperabm.time import Date


class TestEnvironmentClass(unittest.TestCase):

    def setUp(self) -> None:
        self.env = Environment()
        junction = Junction(
            name='sample junction',
            pos=[0, 0]
        )
        self.env.add(junction)
        settlement = Settlement(
            name='sample settlement',
            pos=[1, 1],
            date_start=Date(2020, 1, 1)
        )
        self.env.add(settlement)
        
        road = Road(
            pos_1=[0.05, 0],
            pos_2=[1, 1],
            name='sample road'
        )
        self.env.add(road)
    
    def test_all_edges(self):
        self.assertEqual(len(self.env.all_edges()), 1)

    def test_add_node_proximity(self):
        ''' new item is in proximity of other items '''
        env = deepcopy(self.env)
        new_item = Junction(pos=[0.05, 0])
        env.add(new_item)
        self.assertEqual(len(env.all_nodes()), 2)

    def test_sort_nodes_by_distance(self):
        nodes_distance = self.env.sort_nodes_by_distance(pos=[0.3, 0.4])
        nearest = nodes_distance[0]
        distance = nearest[0]
        index = nearest[1]
        item = self.env.get_node_object(index)
        self.assertEqual(item.name, 'sample junction')
        self.assertEqual(distance, 0.5)
        

if __name__ == '__main__':
    unittest.main()