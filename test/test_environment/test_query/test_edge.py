import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_1


class TestEdgeQuery(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_1)

    def test_(self):
        pass


if __name__ == "__main__":
    unittest.main()