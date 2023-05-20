import unittest
from copy import deepcopy

from piperabm.transporation import Transportation
from piperabm.agent.config import Walk


class TestTransportaionClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.transportation = Walk()

    def test_how_long(self):
        length = 1000
        delta_t = self.transportation.how_long(length)
        self.assertEqual(delta_t.total_seconds(), 12 * 60)

    def test_how_much_fuel(self):
        length = 1000
        result = self.transportation.how_much_fuel(length)
        expected_result = {
            'food': 0.016666666666666666,
            'water': 0.008333333333333333,
            'energy': 0.0
        }
        self.assertDictEqual(expected_result, result.to_dict())

    def test_dict(self):
        dictionary = self.transportation.to_dict()
        expected_result = {
            'name': 'foot',
            'speed': 1.3888888888888888,
            'fuel_rate': {
                'food': 2.3148148148148147e-05,
                'water': 1.1574074074074073e-05,
                'energy': 0.0
            }
        }
        self.assertDictEqual(dictionary, expected_result)
        transportation = Transportation()
        transportation.from_dict(dictionary)
        self.assertEqual(transportation, self.transportation)

    def test_delta(self):
        transportation_previous = deepcopy(self.transportation)
        self.transportation.speed = 2
        delta = self.transportation - transportation_previous
        expected_result = {'speed': 0.6111111111111112}
        self.assertDictEqual(expected_result, delta)
        transportation_previous + delta
        self.assertEqual(transportation_previous, self.transportation)


if __name__ == "__main__":
    unittest.main()