import unittest
from copy import deepcopy

from piperabm.matter import DeltaMatter
from piperabm.matter.delta_matter.samples import delta_matter_0, delta_matter_1, delta_matter_3
#from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestMatterClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.delta_food_1 = deepcopy(delta_matter_0)
        self.delta_food_2 = deepcopy(delta_matter_3)
        self.delta_water = deepcopy(delta_matter_1)

    def test_serialization(self):
        dictionary = self.delta_water.serialize()
        delta_water = DeltaMatter()
        delta_water.deserialize(dictionary)

    def test_add(self):
        result = self.delta_food_1 + 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, 13)

        result = self.delta_food_1 + self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, 13)

    def test_sub(self):
        result = self.delta_food_1 - 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, -3)

        result = self.delta_food_1 - self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, -3)

    def test_mul(self):
        result = self.delta_food_1 * 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, 40)

        result = self.delta_food_1 * self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, 40)

    def test_truediv(self):
        result = self.delta_food_1 / 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, 5/8)

        result = self.delta_food_1 / self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, 5/8)

    def test_sum(self):
        delta_food_0 = DeltaMatter(name='food', amount=2)
        result = delta_food_0 + self.delta_food_1 + self.delta_food_2
        self.assertEqual(result.amount, 15)

        food_list = [delta_food_0, self.delta_food_1, self.delta_food_2]
        result = sum(food_list, start=DeltaMatter(name=delta_food_0.name))
        self.assertEqual(result.amount, 15)
        

if __name__ == '__main__':
    unittest.main()