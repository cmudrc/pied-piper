import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_2


class TestInfrastructureClass(unittest.TestCase):

    def setUp(self):
        self.infrastrucure = deepcopy(environment_2.infrastrucure)

    def test_create(self):
        self.assertEqual(len(self.infrastrucure.all_nodes()), 5)
        self.assertEqual(len(self.infrastrucure.all_edges()), 4)

    def test_find_path(self):
        index_1 = self.infrastrucure.find_nearest_node(pos=[-60, 40])
        index_2 = self.infrastrucure.find_nearest_node(pos=[200, 20])
        path = self.infrastrucure.find_path(index_1, index_2)
        self.assertEqual(len(path), 3)
        for edge_index in path:
            item = self.infrastrucure.get_item(edge_index)
            self.assertEqual(item.category, 'edge')


if __name__ == '__main__':
    unittest.main()