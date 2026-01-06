import unittest
from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_2 import model


class TestSocietyStatClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model)

    def test_stat(self):
        stat = self.model.infrastructure.stat
        expected_stat = {
            'node': {'home': 3, 'junction': 6, 'market': 1},
            'edge': {'neighborhood_access': 4, 'street': 5}
        }
        self.assertDictEqual(stat, expected_stat)


if __name__ == "__main__":
    unittest.main()
