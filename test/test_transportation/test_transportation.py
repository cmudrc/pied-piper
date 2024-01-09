import unittest
from copy import deepcopy

from piperabm.transporation import Transportation
from piperabm.transporation.samples import transportation_0


class TestTransportationClass(unittest.TestCase):

    def setUp(self) -> None:
        self.transportation = deepcopy(transportation_0)

    def test_how_long(self):
        duration = self.transportation.how_long(length=1000)
        self.assertEqual(duration.total_seconds(), 720)

    def test_how_much_fuel(self):
        fuels_rate = self.transportation.how_much_fuel(length=1000)
        self.assertAlmostEqual(fuels_rate('food'), 0.0166, places=3)
        self.assertAlmostEqual(fuels_rate('water'), 0.0083, places=3)
        self.assertAlmostEqual(fuels_rate('energy'), 0, places=3)

    def test_serialization(self):
        dictionary = self.transportation.serialize()
        new_transportation = Transportation()
        new_transportation.deserialize(dictionary)
        self.assertEqual(self.transportation, new_transportation)

    
if __name__ == '__main__':
    unittest.main()