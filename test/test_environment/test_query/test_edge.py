import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_1


class TestEdgeQuery(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_1)

    def test_all_edges(self):
        edges = self.env.all_edges()
        expected_result = [(0, 2), (1, 2)]
        self.assertListEqual(edges, expected_result)


if __name__ == "__main__":
    unittest.main()