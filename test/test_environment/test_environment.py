import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.items import Junction, Settlement
from piperabm.time import Date


class TestEnvironmentClass(unittest.TestCase):

    def setUp(self) -> None:
        self.env = Environment()
        junction = Junction(
            name='j_1',
            pos=[0, 0]
        )
        self.env.add_node(junction)
        settlement = Settlement(
            name='j_2',
            pos=[1, 1],
            date_start=Date(2020, 1, 1)
        )
        self.env.add_node(settlement)

    def test_add_node_proximity(self):
        ''' new item is in proximity of other items '''
        env = deepcopy(self.env)
        new_item = Junction(pos=[0.05, 0])
        env.add_node(new_item)
        self.assertEqual(len(env.all_nodes()), 2)
        

if __name__ == '__main__':
    unittest.main()