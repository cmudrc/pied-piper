import unittest
from copy import deepcopy

from piperabm.model.samples import model_2


class TestInfrastructureClass(unittest.TestCase):

    def setUp(self):
        self.infrastrucure = deepcopy(model_2.infrastrucure)

    def test_create(self):
        self.assertEqual(len(self.infrastrucure.all_nodes()), 5)
        self.assertEqual(len(self.infrastrucure.all_edges()), 4)

    def test_find_path(self):
        all_nodes = self.infrastrucure.all_nodes()
        index_1, _ = self.infrastrucure.find_nearest_node(pos=[-60, 40], items=all_nodes)
        index_2, _ = self.infrastrucure.find_nearest_node(pos=[200, 20], items=all_nodes)
        path = self.infrastrucure.find_path(index_1, index_2)
        self.assertEqual(len(path), 4)
        for node_index in path:
            item = self.infrastrucure.get(node_index)
            self.assertEqual(item.category, "node")


if __name__ == "__main__":
    unittest.main()