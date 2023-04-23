import unittest
from copy import deepcopy

from piperabm.environment.elements import Hub
from piperabm.environment.elements.hub.samples import hub_0 as hub
from piperabm.unit import Date, DT


class TestHubClass(unittest.TestCase):

    def setUp(self):
        self.hub = deepcopy(hub)

    def test_dict(self):
        dictionary = self.hub.to_dict()
        new_hub = Hub()
        new_hub.from_dict(dictionary)
        self.assertEqual(self.hub, new_hub)

    def test_exists(self):
        start_date = Date(2020, 1, 4)
        end_date = start_date + DT(days=2)
        exists = self.hub.exists(start_date, end_date)
        self.assertTrue(exists)
        start_date = Date(2020, 1, 1)
        end_date = start_date + DT(days=1)
        exists = self.hub.exists(start_date, end_date)
        self.assertFalse(exists)

    def test_structure_exists(self):
        start_date = Date(2020, 1, 4)
        end_date = start_date + DT(days=2)
        exists = self.hub.structure.exists(start_date, end_date)
        self.assertTrue(exists)
        start_date = Date(2020, 1, 1)
        end_date = start_date + DT(days=1)
        exists = self.hub.structure.exists(start_date, end_date)
        self.assertFalse(exists)


if __name__ == "__main__":
    unittest.main()