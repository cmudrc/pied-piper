import unittest

from piperabm.transporation import Walk
from piperabm.transporation.load import load_transportation


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
        self.assertAlmostEqual(result('food'), 0.01666666666)
        self.assertAlmostEqual(result('water'), 0.00833333333)
        self.assertAlmostEqual(result('energy'), 0)

    def test_dict(self):
        dictionary = self.transportation.to_dict()
        print(dictionary)
        #######

    def test_load(self):
        dictionary = {} #######
        #transportation = load_transportation(dictionary)


if __name__ == "__main__":
    unittest.main()