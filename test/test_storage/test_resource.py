import unittest
from copy import deepcopy

from piperabm.storage.resource import Resource
from piperabm.storage.resource.samples import resource_0
from piperabm.tools.symbols import SYMBOLS


class TestResourceClass(unittest.TestCase):

    def setUp(self) -> None:
        self.resource = deepcopy(resource_0)

    def test_add_0(self):
        remainder = self.resource + 3
        self.assertEqual(self.resource.amount, 9)
        self.assertEqual(remainder, 0)
    
    def test_add_1(self):
        remainder = self.resource + 4
        self.assertEqual(self.resource.amount, 10)
        self.assertEqual(remainder, 0)
    
    def test_add_2(self):
        remainder = self.resource + 5
        self.assertEqual(self.resource.amount, 10)
        self.assertEqual(remainder, 1)

    def test_sub_0(self):
        remainder = self.resource - 5
        self.assertEqual(self.resource.amount, 1)
        self.assertEqual(remainder, 0)

    def test_sub_1(self):
        remainder = self.resource - 6
        self.assertEqual(self.resource.amount, 0)
        self.assertEqual(remainder, 0)

    def test_sub_2(self):
        remainder = self.resource - 7
        self.assertEqual(self.resource.amount, 0)
        self.assertEqual(remainder, 1)

    def test_mul_0(self):
        remainder = self.resource * 2
        self.assertEqual(self.resource.amount, 10)
        self.assertEqual(remainder, 2)
    
    def test_mul_1(self):
        remainder = self.resource * -2
        self.assertEqual(self.resource.amount, 0)
        self.assertEqual(remainder, 12)

    def test_div_0(self):
        remainder = self.resource / 0.5
        self.assertEqual(self.resource.amount, 10)
        self.assertEqual(remainder, 2)

    def test_div_1(self):
        remainder = self.resource / 0
        self.assertEqual(self.resource.amount, 10)
        self.assertEqual(remainder, SYMBOLS['inf'])

    def test_source_demand(self):
        self.assertEqual(self.resource.source, 6)
        self.assertEqual(self.resource.demand, 4)

    def test_dict(self):
        dictionary = self.resource.to_dict()
        expected_result = {'amount': 6, 'max': 10, 'min': 0}
        self.assertDictEqual(dictionary, expected_result)
        resource = Resource()
        resource.from_dict(dictionary)
        self.assertEqual(resource, self.resource)

    def test_delta(self):
        resource_previous = deepcopy(self.resource)
        resource = deepcopy(resource_previous)
        resource + 3
        delta = resource - resource_previous
        expected_result = {'amount': 3}
        self.assertDictEqual(delta, expected_result)
        resource_previous + delta
        self.assertEqual(resource, resource_previous)


if __name__ == "__main__":
    unittest.main()