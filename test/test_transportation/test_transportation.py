import unittest
from copy import deepcopy

from piperabm.transportation import Transportation
from piperabm.transportation.samples import transportation_0
from piperabm.matter.containers.samples import containers_0


class TestTransportationClass(unittest.TestCase):

    def setUp(self) -> None:
        self.transportation = deepcopy(transportation_0)

    def test_length_by_duration(self):
        length = self.transportation.length_by_duration(duration=720)
        self.assertEqual(length, 1000)

    def test_duration_by_length(self):
        duration = self.transportation.duration_by_length(length=1000)
        self.assertEqual(duration.total_seconds(), 720)

    def test_fuels_by_duration(self):
        fuels_rate = self.transportation.fuels_by_duration(duration=720)
        self.assertAlmostEqual(fuels_rate('food'), 0.0166, places=3)
        self.assertAlmostEqual(fuels_rate('water'), 0.0083, places=3)
        self.assertAlmostEqual(fuels_rate('energy'), 0, places=3)

    def test_fuels_by_length(self):
        fuels_rate = self.transportation.fuels_by_length(length=1000)
        self.assertAlmostEqual(fuels_rate('food'), 0.0166, places=3)
        self.assertAlmostEqual(fuels_rate('water'), 0.0083, places=3)
        self.assertAlmostEqual(fuels_rate('energy'), 0, places=3)

    def test_duration_by_fuels(self):
        fuels = containers_0
        duration = self.transportation.duration_by_fuels(fuels)
        self.assertEqual(duration, 2592000)

    def test_length_by_fuels(self):
        fuels = containers_0
        length = self.transportation.length_by_fuels(fuels)
        self.assertEqual(length, 3600000)

    def test_serialization(self):
        dictionary = self.transportation.serialize()
        new_transportation = Transportation()
        new_transportation.deserialize(dictionary)
        self.assertEqual(self.transportation, new_transportation)

    
if __name__ == '__main__':
    unittest.main()