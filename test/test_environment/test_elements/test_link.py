import unittest
from copy import deepcopy

from piperabm.environment.elements import Link
from piperabm.environment.elements.link.samples import link_0 as link
from piperabm.unit import Date, DT


class TestLinkClass(unittest.TestCase):

    def setUp(self):
        self.link = deepcopy(link)

    def test_dict(self):
        dictionary = self.link.to_dict()
        expected_result = {
            'name': 'halfway 0',
            'pos': [0, 0],
            'start_date': {'year': 2020, 'month': 1, 'day': 2, 'hour': 0, 'minute': 0, 'second': 0},
            'end_date': None,
            'structure': {
                'boundary': {'shape': {'type': 'rectangle', 'width': 4, 'height': 2, 'angle': 0}},
                'active': True,
                'start_date': {'year': 2020, 'month': 1, 'day': 2, 'hour': 0, 'minute': 0, 'second': 0},
                'end_date': None,
                'sudden_degradation': {'distribution': {'type': 'dirac delta', 'main': 864000.0}, 'unit_size': None},
                'progressive_degradation': {'usage_max': 'inf', 'usage_current': 0, 'formula_name': 'formula_01'},
                'type': 'road',
                'actual_length': None,
                'difficulty': 1.5},
            'type': 'link'
        }
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
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
    
    def test_structure_exists(self):
        start_date = Date(2020, 1, 4)
        end_date = start_date + DT(days=2)
        exists = self.link.structure.exists(start_date, end_date)
        self.assertTrue(exists)
        start_date = Date(2020, 1, 1)
        end_date = start_date + DT(days=1)
        exists = self.link.structure.exists(start_date, end_date)
        self.assertFalse(exists)


if __name__ == "__main__":
    unittest.main()