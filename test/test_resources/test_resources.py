import unittest
from copy import deepcopy

from piperabm.resources import Resources, Resource
from piperabm.resources.samples import resources_0, resources_1


class TestResourceClass(unittest.TestCase):

    def setUp(self) -> None:
        self.resources = deepcopy(resources_0)
        self.other_resources = deepcopy(resources_1)

    def test_source(self):
        source = self.resources.source
        self.assertEqual(source('food'), 30)
        self.assertEqual(source('water'), 40)
        self.assertEqual(source('energy'), 40)

    def test_demand(self):
        demand = self.resources.demand
        self.assertEqual(demand('food'), 70)
        self.assertEqual(demand('water'), 60)
        self.assertEqual(demand('energy'), 60)

    def test_empty(self):
        food = Resource(name='food', amount=0)
        resources = Resources(food)
        self.assertTrue(resources.is_all_zero)
        water = Resource(name='water', amount=5)
        resources.add_resource(water)
        self.assertFalse(resources.is_all_zero)
        result = resources.check_empty(['food', 'water'])
        self.assertListEqual(result, ['food'])
    
    def test_add(self):
        resources = deepcopy(self.resources)
        other_resources = deepcopy(self.other_resources)
        remainders = resources.add(other_resources)
        self.assertEqual(resources('food'), 30.2)
        self.assertEqual(resources('water'), 40.1)
        self.assertEqual(resources('energy'), 40.5)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)
    
    def test_sub(self):
        resources = deepcopy(self.resources)
        other_resources = deepcopy(self.other_resources)
        remainders = resources.sub(other_resources)
        self.assertEqual(resources('food'), 29.8)
        self.assertEqual(resources('water'), 39.9)
        self.assertEqual(resources('energy'), 39.5)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)
    
    def test_mul(self):
        resources = deepcopy(self.resources)
        remainders = resources.mul(3)
        self.assertEqual(resources('food'), 90)
        self.assertEqual(resources('water'), 100)
        self.assertEqual(resources('energy'), 100)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 20)
        self.assertEqual(remainders('energy'), 20)

    def test_truediv(self):
        resources = deepcopy(self.resources)
        remainders = resources.truediv(2)
        self.assertEqual(resources('food'), 15)
        self.assertEqual(resources('water'), 20)
        self.assertEqual(resources('energy'), 20)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)
    
    def test_serialize(self):
        dictionary = self.resources.serialize()
        expected_result = {
            'food': {'amount': 30, 'max': 100, 'min': 0, 'name': 'food'},
            'water': {'amount': 40, 'max': 100, 'min': 0, 'name': 'water'},
            'energy': {'amount': 40, 'max': 100, 'min': 0, 'name': 'energy'},
        }
        self.assertDictEqual(dictionary, expected_result)

    def test_deserialize(self):
        dictionary = {
            'food': {'amount': 30, 'max': 100, 'min': 0, 'name': 'food'},
            'water': {'amount': 40, 'max': 100, 'min': 0, 'name': 'water'},
            'energy': {'amount': 40, 'max': 100, 'min': 0, 'name': 'energy'},
        }
        resources = Resources()
        resources.deserialize(dictionary)
        self.assertEqual(resources, self.resources)


if __name__ == "__main__":
    unittest.main()
