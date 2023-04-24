import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_1


class TestNodeSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_1)

    def test_find_node_by_name(self):
        index = self.env._find_node_by_name("Peter's Home")
        self.assertEqual(index, 1)
        index = self.env._find_node_by_name("My Home")
        self.assertEqual(index, None)

    def test_find_node_by_index(self):
        index = self.env._find_node_by_index(1)
        self.assertEqual(index, 1)
        index = self.env._find_node_by_index(10)
        self.assertEqual(index, None)
    
    def test_find_node_by_pos(self):
        index = self.env._find_node_by_pos([20, 20])
        self.assertEqual(index, 1)
        index = self.env._find_node_by_pos([21, 21])
        self.assertEqual(index, 1)
        index = self.env._find_node_by_pos([-10, -10])
        self.assertEqual(index, None)


if __name__ == "__main__":
    unittest.main()