import unittest
from copy import deepcopy

from piperabm.resources import Resources, Resource
from piperabm.resources.samples import resources_0, resources_1
from piperabm.economy.exchange_rate.samples import exchange_rate_0


class TestResourceClass(unittest.TestCase):

    def setUp(self) -> None:
        self.resources = deepcopy(resources_0)
        self.other_resources = deepcopy(resources_1)

    def test_source(self):
        sources = self.resources.source
        self.assertEqual(sources("food"), 30)
        self.assertEqual(sources("water"), 40)
        self.assertEqual(sources("energy"), 40)

    def test_demand(self):
        demands = self.resources.demand
        self.assertEqual(demands("food"), 70)
        self.assertEqual(demands("water"), 60)
        self.assertEqual(demands("energy"), 60)

    def test_demand_actual_0(self):
        """
        When the balance is NOT a demand barrier
        """
        balance = 3000
        demands = self.resources.demand
        demands_actual = self.resources.demands_actual(exchange_rate_0, balance)
        self.assertEqual(demands, demands_actual)

    def test_demand_actual_1(self):
        """
        When the balance is a demand barrier
        """
        balance = 100
        demands_actual = self.resources.demands_actual(exchange_rate_0, balance)
        self.assertAlmostEqual(demands_actual("food"), 6.60, places=2)
        self.assertAlmostEqual(demands_actual("water"), 5.66, places=2)
        self.assertAlmostEqual(demands_actual("energy"), 5.66, places=2)

    def test_demand_actual_2(self):
        """
        When the balance is a demand barrier
        """
        balance = 0
        demands_actual = self.resources.demands_actual(exchange_rate_0, balance)
        self.assertAlmostEqual(demands_actual("food"), 0, places=2)
        self.assertAlmostEqual(demands_actual("water"), 0, places=2)
        self.assertAlmostEqual(demands_actual("energy"), 0, places=2)

    def test_max(self):
        resources_max = self.resources.max
        self.assertEqual(resources_max("food"), 100)
        self.assertEqual(resources_max("water"), 100)
        self.assertEqual(resources_max("energy"), 100)

    def test_value(self):
        values = self.resources.value(exchange_rate_0)
        self.assertEqual(values("food"), 300)
        expected_total = 300 + 80 + 160
        self.assertEqual(values.sum, expected_total)

    def test_biggest(self):
        name = self.resources.biggest
        self.assertEqual(name, "water")

    def test_cutoff(self):
        demands = self.resources.demand
        values = demands.value(exchange_rate_0)
        values.cutoff(100)
        self.assertEqual(values("food"), 100)

    def test_empty(self):
        food = Resource(name="food", amount=0)
        resources = Resources(food)
        self.assertTrue(resources.is_all_zero)
        water = Resource(name="water", amount=5)
        resources.add_resource(water)
        self.assertFalse(resources.is_all_zero)
        result = resources.check_empty(["food", "water"])
        self.assertListEqual(result, ["food"])
    
    def test_add(self):
        resources = deepcopy(self.resources)
        other_resources = deepcopy(self.other_resources)
        remainders = resources.add(other_resources)
        self.assertEqual(resources("food"), 30.2)
        self.assertEqual(resources("water"), 40.1)
        self.assertEqual(resources("energy"), 40.5)
        self.assertEqual(remainders("food"), 0)
        self.assertEqual(remainders("water"), 0)
        self.assertEqual(remainders("energy"), 0)
    
    def test_sub(self):
        resources = deepcopy(self.resources)
        other_resources = deepcopy(self.other_resources)
        remainders = resources.sub(other_resources)
        self.assertEqual(resources("food"), 29.8)
        self.assertEqual(resources("water"), 39.9)
        self.assertEqual(resources("energy"), 39.5)
        self.assertEqual(remainders("food"), 0)
        self.assertEqual(remainders("water"), 0)
        self.assertEqual(remainders("energy"), 0)
    
    def test_mul(self):
        resources = deepcopy(self.resources)
        remainders = resources.mul(3)
        self.assertEqual(resources("food"), 90)
        self.assertEqual(resources("water"), 100)
        self.assertEqual(resources("energy"), 100)
        self.assertEqual(remainders("food"), 0)
        self.assertEqual(remainders("water"), 20)
        self.assertEqual(remainders("energy"), 20)

    def test_truediv(self):
        resources = deepcopy(self.resources)
        remainders = resources.truediv(2)
        self.assertEqual(resources("food"), 15)
        self.assertEqual(resources("water"), 20)
        self.assertEqual(resources("energy"), 20)
        self.assertEqual(remainders("food"), 0)
        self.assertEqual(remainders("water"), 0)
        self.assertEqual(remainders("energy"), 0)
    
    def test_serialize(self):
        dictionary = self.resources.serialize()
        expected_result = {
            "food": {"amount": 30, "max": 100, "min": 0, "name": "food"},
            "water": {"amount": 40, "max": 100, "min": 0, "name": "water"},
            "energy": {"amount": 40, "max": 100, "min": 0, "name": "energy"},
        }
        self.assertDictEqual(dictionary, expected_result)

    def test_deserialize(self):
        dictionary = {
            "food": {"amount": 30, "max": 100, "min": 0, "name": "food"},
            "water": {"amount": 40, "max": 100, "min": 0, "name": "water"},
            "energy": {"amount": 40, "max": 100, "min": 0, "name": "energy"},
        }
        resources = Resources()
        resources.deserialize(dictionary)
        self.assertEqual(resources, self.resources)


if __name__ == "__main__":
    unittest.main()
