import unittest
from copy import deepcopy

from piperabm.environment.infrastructure.road.samples import road_1
from piperabm.tools.symbols import SYMBOLS
from piperabm.unit import Date


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

    def test_update(self):
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 15)
        road_previous = deepcopy(self.road)
        self.road.update(start_date, end_date)
        delta = self.road - road_previous
        self.assertDictEqual(delta, {'active': True})


if __name__ == "__main__":
    unittest.main()