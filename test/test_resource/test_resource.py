import unittest
from copy import deepcopy

from piperabm.resource import Resource


class TestResourceClass0(unittest.TestCase):

    def setUp(self):
        self.r = Resource()

    def test_current_resource(self):
        r = deepcopy(self.r)
        expected_result = {}
        self.assertDictEqual(r.current_resource, expected_result)
    
    def test_max_resource(self):
        r = deepcopy(self.r)
        expected_result = {}
        self.assertDictEqual(r.max_resource, expected_result)

    def test_min_resource(self):
        r = deepcopy(self.r)
        expected_result = {}
        self.assertDictEqual(r.min_resource, expected_result)

    def test_source(self):
        r = deepcopy(self.r)
        expected_result = {}
        self.assertDictEqual(r.source().current_resource, expected_result)

    def test_demand(self):
        r = deepcopy(self.r)
        expected_result = {}
        self.assertDictEqual(r.demand().current_resource, expected_result)

    def test_is_zero(self):
        r = deepcopy(self.r)
        self.assertTrue(r.is_zero())

    def test_has_zero(self):
        r = deepcopy(self.r)
        self.assertTrue(r.has_zero())


class TestResourceClass1(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            },
            max_resource={
                'food': 10,
                'water': 10,
            }
        )
   
    def test_current_resource(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 5,
            'water': 8,
        }
        self.assertDictEqual(r.current_resource, expected_result)
   
    def test_max_resource(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 10,
            'water': 10,
        }
        self.assertDictEqual(r.max_resource, expected_result)

    def test_min_resource(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 0,
            'water': 0,
        }
        self.assertDictEqual(r.min_resource, expected_result)

    def test_source(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 5,
            'water': 8,
        }
        self.assertDictEqual(r.source().current_resource, expected_result)

    def test_demand(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 5,
            'water': 2,
        }
        self.assertDictEqual(r.demand().current_resource, expected_result)

    def test_is_zero(self):
        r = deepcopy(self.r)
        self.assertFalse(r.is_zero())

    def test_has_zero(self):
        r = deepcopy(self.r)
        self.assertFalse(r.has_zero())


class TestResourceClass2(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            },
            max_resource={
                'water': 10,
            },
            min_resource={
                'food': 1,
            }
        )

    def test_current_resource(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 5,
            'water': 8,
        }
        self.assertDictEqual(r.current_resource, expected_result)
    
    def test_max_resource(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': None,
            'water': 10,
        }
        self.assertDictEqual(r.max_resource, expected_result)

    def test_min_resource(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 1,
            'water': 0,
        }
        self.assertDictEqual(r.min_resource, expected_result)

    def test_source(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': 4,
            'water': 8,
        }
        self.assertDictEqual(r.source().current_resource, expected_result)

    def test_demand(self):
        r = deepcopy(self.r)
        expected_result = {
            'food': None,
            'water': 2,
        }
        self.assertDictEqual(r.demand().current_resource, expected_result)

    def test_is_zero(self):
        r = deepcopy(self.r)
        self.assertFalse(r.is_zero())

    def test_has_zero(self):
        r = deepcopy(self.r)
        self.assertFalse(r.has_zero())
        

if __name__ == "__main__":
    unittest.main()