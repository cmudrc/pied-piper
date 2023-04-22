import unittest

from piperabm.environment.elements import Link
from piperabm.environment.elements.link.samples import link_0 as link
from piperabm.unit import Date, DT


class TestSettlementClass(unittest.TestCase):

    def setUp(self):
        self.link = link

    def test_dict(self):
        dictionary = self.link.to_dict()
        new_link = Link()
        new_link.from_dict(dictionary)
        self.assertEqual(self.link, new_link)

    def test_exists(self):
        start_date = Date(2020, 1, 4)
        end_date = start_date + DT(days=2)
        exists = self.link.exists(start_date, end_date)
        self.assertTrue(exists)
        start_date = Date(2020, 1, 1)
        end_date = start_date + DT(days=1)
        exists = self.link.exists(start_date, end_date)
        self.assertFalse(exists)


if __name__ == "__main__":
    unittest.main()