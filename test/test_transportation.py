import unittest
from copy import deepcopy

from piperabm.transportation import Walk


class TestTransportaionClass(unittest.TestCase):
    
    def test_how_long(self):
        transportation = Walk()
        length = 1000
        delta_t = transportation.how_long(length)
        self.assertEqual(delta_t.total_seconds(), 12*60)

    def test_how_much_fuel(self):
        transportation = Walk()
        length = 1000
        result = transportation.how_much_fuel(length)
        self.assertAlmostEqual(result.batch['food'], 0.01666666666)
        self.assertAlmostEqual(result.batch['water'], 0.00833333333)
        self.assertAlmostEqual(result.batch['energy'], 0)


if __name__ == "__main__":
    unittest.main()