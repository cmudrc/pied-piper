import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_0
from piperabm.environment.structures.settlement.samples import settlement_0


class TestEnvironmentNodeQuery(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_0)

    def test_all_indexes(self):
        indexes = self.env.all_indexes()
        self.assertListEqual(list(indexes), [0])
        indexes = self.env.all_indexes(type='settlement')
        self.assertListEqual(list(indexes), [0])

    def test_get_node_object(self):
        structure = self.env.get_node_object(0)
        self.assertEqual(structure, settlement_0)

    def test_get_node_pos(self):
        pos = self.env.get_node_pos(0)
        self.assertEqual(pos, [-2, -2])

    def test_oldest_node(self):
        oldest_node = self.env.oldest_node()
        self.assertEqual(oldest_node, 0)


if __name__ == "__main__":
    unittest.main()