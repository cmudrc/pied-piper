import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_0


class TestNodeSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_0)

    def test_find_node_by_name(self):
        index = self.env._find_node_by_name("John's Home")
        self.assertEqual(index, 0)
        index = self.env._find_node_by_name("My Home")
        self.assertEqual(index, None)

    def test_find_node_by_index(self):
        index = self.env._find_node_by_index(0)
        self.assertEqual(index, 0)
        index = self.env._find_node_by_index(10)
        self.assertEqual(index, None)
    
    def test_find_node_by_pos(self):
        index = self.env._find_node_by_pos([-2, -2])
        self.assertEqual(index, 0)
        index = self.env._find_node_by_pos([-3, -3])
        self.assertEqual(index, 0)
        index = self.env._find_node_by_pos([-10, -10])
        self.assertEqual(index, None)


if __name__ == "__main__":
    unittest.main()