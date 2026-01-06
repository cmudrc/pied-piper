import unittest
from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_2 import model


class TestSocietyStatClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model)
        homes = self.model.infrastructure.homes
        self.model.society.neighbor_radius = 270
        self.model.society.add_agent(home_id=homes[0], id=1)
        self.model.society.add_agent(home_id=homes[0], id=2)
        self.model.society.add_agent(home_id=homes[1], id=3)
        self.model.society.add_friend(id_1=2, id_2=3)

    def test_stat(self):
        stat = self.model.society.stat
        expected_stat = {
            'node': {'alive': 3, 'dead': 0, 'total': 3},
            'edge': {'family': 1, 'friend': 1, 'neighbor': 2}
        }
        self.assertDictEqual(stat, expected_stat)


if __name__ == "__main__":
    unittest.main()
