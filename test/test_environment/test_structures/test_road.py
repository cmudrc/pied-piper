import unittest
from copy import deepcopy

from piperabm.environment.structures.road.samples import road_0


class TestRoadClass(unittest.TestCase):

    def setUp(self) -> None:
        self.road = deepcopy(road_0)

    def test_length(self):
        length_ideal = self.road.length(mode='ideal')
        self.assertEqual(length_ideal, 4)
        length_adjusted = self.road.length(mode='adjusted')
        self.assertEqual(length_adjusted, 6)

    def test_width(self):
        width = self.road.width()
        self.assertEqual(width, 2)


if __name__ == "__main__":
    unittest.main()