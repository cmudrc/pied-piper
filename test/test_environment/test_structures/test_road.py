import unittest
from copy import deepcopy

from piperabm.environment.structures.road.samples import road_1
from piperabm.tools.symbols import SYMBOLS


class TestRoadClass(unittest.TestCase):

    def setUp(self) -> None:
        self.road = deepcopy(road_1)

    def test_length(self):
        length_ideal = self.road.length(mode='ideal')
        expected_result = SYMBOLS['eps']
        self.assertEqual(length_ideal, expected_result)
        length_adjusted = self.road.length(mode='adjusted')
        expected_result = SYMBOLS['eps'] * 1.5
        self.assertEqual(length_adjusted, expected_result)

    def test_width(self):
        width = self.road.width()
        self.assertEqual(width, 2)


if __name__ == "__main__":
    unittest.main()