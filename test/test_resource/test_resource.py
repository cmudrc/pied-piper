import unittest
from copy import deepcopy

from piperabm.resource import Resource
from piperabm.resource.samples import resource_0
from piperabm.economy.exchange_rate.samples import exchange_rate_0


class TestResourceClass(unittest.TestCase):

    def setUp(self) -> None:
        self.resource = deepcopy(resource_0)
        self.other_resource = Resource(
            name=self.resource.name,
            amount=100
        )
        self.exchange_rate = exchange_rate_0

    def test_source_0(self):
        source = self.resource.source
        self.assertEqual(source, 30)

    def test_demand_0(self):
        demand = self.resource.demand
        self.assertEqual(demand, 70)
        
    def test_source_1(self):
        resource = deepcopy(self.resource)
        resource.min = 50
        source = resource.source
        self.assertEqual(source, 0)

    def test_demand_1(self):
        resource = deepcopy(self.resource)
        resource.min = 50
        demand = self.resource.demand
        self.assertEqual(demand, 70)

    def test_value(self):
        value = self.exchange_rate.value(self.resource)
        self.assertEqual(value, 300)

    def test_add(self):
        resource = deepcopy(self.resource)
        other_resource = deepcopy(self.other_resource)
        remainder = resource.add(other_resource)
        self.assertEqual(resource.amount, 100)
        self.assertEqual(remainder, 30)

    def test_sub(self):
        resource = deepcopy(self.resource)
        other_resource = deepcopy(self.other_resource)
        remainder = resource.sub(other_resource)
        self.assertEqual(resource.amount, 0)
        self.assertEqual(remainder, 70)

    def test_mul(self):
        resource = deepcopy(self.resource)
        remainder = resource.mul(4)
        self.assertEqual(resource.amount, 100)
        self.assertEqual(remainder, 20)

    def test_truediv(self):
        resource = deepcopy(self.resource)
        remainder = resource.truediv(3)
        self.assertEqual(resource.amount, 10)
        self.assertEqual(remainder, 0)

    def test_serialize(self):
        dictionary = self.resource.serialize()
        expected_result = {'amount': 30, 'max': 100, 'min': 0, 'name': 'food'}
        self.assertDictEqual(dictionary, expected_result)

    def test_deserialize(self):
        dictionary = {'amount': 30, 'max': 100, 'min': 0, 'name': 'food'}
        resource = Resource()
        resource.deserialize(dictionary)
        self.assertEqual(resource, self.resource)


if __name__ == "__main__":
    unittest.main()
