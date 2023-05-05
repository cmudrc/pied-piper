import unittest
from copy import deepcopy

from piperabm.resource import Resource
from piperabm.resource.samples import resource_0
from piperabm.resource.samples import resource_rate_0


class TestResourceClass(unittest.TestCase):

    def setUp(self) -> None:
        self.resource = deepcopy(resource_0)
        self.rate = resource_rate_0

    def test_call(self):
        resource = self.resource('food')
        self.assertEqual(resource, 6)
    
    def test_add(self):
        remainder = self.resource + self.rate
        expected_resource = {
            'food': {'max': 10, 'min': 0, 'amount': 10},
            'water': {'max': 20, 'min': 0, 'amount': 12},
            'energy': {'max': 25, 'min': 0, 'amount': 22},
        }
        self.assertDictEqual(self.resource.to_dict(), expected_resource)
        expected_remainder = {'food': 2, 'water': 0, 'energy': 0}
        self.assertDictEqual(remainder.to_dict(), expected_remainder)

    def test_sub(self):
        remainder = self.resource - self.rate
        expected_resource = {
            'food': {'max': 10, 'min': 0, 'amount': 0},
            'water': {'max': 20, 'min': 0, 'amount': 4},
            'energy': {'max': 25, 'min': 0, 'amount': 16},
        }
        self.assertDictEqual(self.resource.to_dict(), expected_resource)
        expected_remainder = {'food': 0, 'water': 0, 'energy': 0}
        self.assertDictEqual(remainder.to_dict(), expected_remainder)
    
    def test_mul(self):
        remainder = self.resource * 2
        expected_resource = {
            'food': {'max': 10, 'min': 0, 'amount': 10},
            'water': {'max': 20, 'min': 0, 'amount': 16},
            'energy': {'max': 25, 'min': 0, 'amount': 25},
        }
        self.assertDictEqual(self.resource.to_dict(), expected_resource)
        expected_remainder = {'food': 2, 'water': 0, 'energy': 13}
        self.assertDictEqual(remainder.to_dict(), expected_remainder)

    def test_truediv(self):
        remainder = self.resource / 0.5
        expected_resource = {
            'food': {'max': 10, 'min': 0, 'amount': 10},
            'water': {'max': 20, 'min': 0, 'amount': 16},
            'energy': {'max': 25, 'min': 0, 'amount': 25},
        }
        self.assertDictEqual(self.resource.to_dict(), expected_resource)
        expected_remainder = {'food': 2, 'water': 0, 'energy': 13}
        self.assertDictEqual(remainder.to_dict(), expected_remainder)

    def test_dict(self):
        dictionary = self.resource.to_dict()
        expected_result = {
            'food': {'max': 10, 'min': 0, 'amount': 6},
            'water': {'max': 20, 'min': 0, 'amount': 8},
            'energy': {'max': 25, 'min': 0, 'amount': 19}
        }
        self.assertEqual(dictionary, expected_result)
        resource = Resource()
        resource.from_dict(dictionary)
        self.assertEqual(resource, self.resource)

    def test_delta(self):
        resource_previous = deepcopy(self.resource)
        self.resource + self.rate
        delta = self.resource - resource_previous
        expected_delta = {
            'food': {'amount': 4},
            'water': {'amount': 4},
            'energy': {'amount': 3}
        }
        self.assertEqual(delta, expected_delta)
        resource_previous + delta
        self.assertEqual(resource_previous, self.resource)


if __name__ == "__main__":
    unittest.main()
