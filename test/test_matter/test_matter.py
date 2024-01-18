import unittest
from copy import deepcopy

from piperabm.matter import Matter
from piperabm.matter.matter.samples import matter_0, matter_3
from piperabm.matter.delta_matter.samples import delta_matter_0
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestMatterClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.food_1 = deepcopy(matter_0)
        self.food_2 = deepcopy(matter_3)
        self.delta_food = deepcopy(delta_matter_0)

    def test_value(self):
        value = self.food_1.value(exchange_rate)
        self.assertEqual(value, 30 * 10)

    def test_serialization(self):
        dictionary = self.food_1.serialize()
        food_1 = Matter()
        food_1.deserialize(dictionary)

    def test_add_0(self):
        """ Matter + (int, flaot) """
        remainder = self.food_1 + 80
        self.assertEqual(self.food_1.amount, 100)
        self.assertEqual(remainder.amount, 10)

    def test_add_1(self):
        """ Matter + DeltaMatter """
        remainder = self.food_1 + self.delta_food
        self.assertEqual(self.food_1.amount, 35)
        self.assertEqual(remainder.amount, 0)

    def test_add_2(self):
        """ Matter + Matter """
        remainder = self.food_1 + self.food_2
        self.assertEqual(self.food_1.amount, 100)
        self.assertEqual(remainder.amount, 10)

    def test_sub_0(self):
        """ Matter - (int, flaot) """
        remainder = self.food_1 - 80
        self.assertEqual(self.food_1.amount, 0)
        self.assertEqual(remainder.amount, 50)

    def test_sub_1(self):
        """ Matter - DeltaMatter """
        remainder = self.food_1 - self.delta_food
        self.assertEqual(self.food_1.amount, 25)
        self.assertEqual(remainder.amount, 0)

    def test_sub_2(self):
        """ Matter - Matter """
        remainder = self.food_1 - self.food_2
        self.assertEqual(self.food_1.amount, 0)
        self.assertEqual(remainder.amount, 50)

    def test_mul(self):
        """ Matter * (int, flaot) """
        self.food_1 * 10
        self.assertEqual(self.food_1.amount, 300)
        self.assertEqual(self.food_1.min, 0)
        self.assertEqual(self.food_1.max, 1000)

    def test_truediv_0(self):
        """ Matter / (int, flaot) """
        result = self.food_1 / 80
        self.assertEqual(self.food_1.amount, 30)
        self.assertEqual(result, 30 / 80)

    def test_truediv_1(self):
        """ Matter / DeltaMatter """
        result = self.food_1 / self.delta_food
        self.assertEqual(self.food_1.amount, 30)
        self.assertEqual(result, 30 / 5)

    def test_truediv_2(self):
        """ Matter / Matter """
        result = self.food_1 / self.food_2
        self.assertEqual(self.food_1.amount, 30)
        self.assertEqual(result, 30 / 80)

        
if __name__ == '__main__':
    unittest.main()