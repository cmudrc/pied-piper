import unittest
from copy import deepcopy

from piperabm.transportation import Foot


class TestExistanecFunction(unittest.TestCase):
    
    def test_how_long(self):
        transportation = Foot()
        length = 1000
        delta_t = transportation.how_long(length)
        self.assertEqual(delta_t.total_seconds(), 12*60)

    def test_how_much_fuel(self):
        transportation = Foot()
        length = 1000
        delta_f = transportation.how_much_fuel(length)
        print('delta_f:', delta_f)


if __name__ == "__main__":
    unittest.main()