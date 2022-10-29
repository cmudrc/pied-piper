import unittest
from copy import deepcopy

from pr.asset import Asset
from pr.asset import Resource
from pr.asset import Produce, Use, Deficiency, Storage


class TestAssetClass(unittest.TestCase):

    food = Resource(
        name='food',
        use=Use(rate=5),
        produce=Produce(rate=1),
        storage=Storage(current_amount=10, max_amount=20),
        deficiency=Deficiency(current_amount=0, max_amount=20)
    )
    water = Resource(
        name='water',
        use=Use(rate=0.1),
        storage=Storage(current_amount=10, max_amount=10),
        deficiency=Deficiency(current_amount=0, max_amount=20)
    )
    energy = Resource(
        name='energy',
        use=Use(rate=1),
        storage=Storage(current_amount=5, max_amount=10)
    )
    a = Asset()
    a.add_resources(food, water, energy)
    a.refill(delta_t=5)

    def test_add_resource(self):
        a_1 = self.a
        a_2 = Asset([self.food, self.water, self.energy])
        a_2.refill(delta_t=5)
        self.assertEqual(a_1.resources['energy'].use.current_amount, a_2.resources['energy'].use.current_amount)

    def test_refill(self):
        use_current_amount = self.a.resources['energy'].use.current_amount
        self.assertEqual(use_current_amount, 5)

    def test_add(self):
        a = deepcopy(self.a)
        remaining = a.add('energy', 15)
        self.assertEqual(remaining, 5)

    def test_sub(self):
        a = deepcopy(self.a)
        remaining = a.sub('energy', 10)
        self.assertEqual(remaining, 5)

    def test_source(self):
        self.assertEqual(self.a.source('energy'), 5)

    def test_demand(self):
        self.assertEqual(self.a.demand('energy'), 10)


if __name__ == "__main__":
    unittest.main()
