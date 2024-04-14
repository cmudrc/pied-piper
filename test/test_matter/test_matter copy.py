import unittest
from copy import deepcopy

from piperabm.matter import Matter
from piperabm.matter.matter.samples import matter_0, matter_3
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestMatterClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.food_1 = deepcopy(matter_0)
        self.food_2 = deepcopy(matter_3)

    def test_serialization(self):
        dictionary = self.food_1.serialize()
        matter = Matter()
        matter.deserialize(dictionary)
        self.assertEqual(self.food_1, matter)

    def test_value(self):
        value = self.food_1.value(exchange_rate)
        self.assertEqual(value, 60 * 10)

    def test_of_value(self):
        matter = Matter(name='food')
        matter.from_value(600, exchange_rate)
        self.assertEqual(matter.amount, 60)
    
    def test_add_int_float(self):
        """ Matter = Matter + (int, float) """
        result = self.food_1 + 15
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(result.amount, 60 + 15)

    def test_add_matter(self):
        """ Matter = Matter + Matter """
        result = self.food_1 + self.food_2
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(self.food_2.amount, 15)
        self.assertEqual(result.amount, 60 + 15)
    
    def test_sum(self):
        """ Matter = sum() """
        matter_list = [self.food_1, self.food_2]
        start = Matter(name=self.food_1.name)
        result = sum(matter_list, start)
        self.assertEqual(result.amount, 60 + 15)
    
    def test_sub_int_float(self):
        """ Matter = Matter - (int, float) """
        result = self.food_1 - 15
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(result.amount, 60 - 15)

    def test_sub_matter(self):
        """ Matter = Matter - Matter """
        result = self.food_1 - self.food_2
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(self.food_2.amount, 15)
        self.assertEqual(result.amount, 60 - 15)
    
    def test_mul_int_float(self):
        """ Matter = Matter * (int, float) """
        result = self.food_1 * 15
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(result.amount, 60 * 15)

    def test_mul_matter(self):
        """ Matter = Matter * Matter """
        result = self.food_1 * self.food_2
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(self.food_2.amount, 15)
        self.assertEqual(result.amount, 60 * 15)
    
    def test_truediv_int_float(self):
        """ (int, float) = Matter / (int, float) """
        result = self.food_1 / 15
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(result, 60 / 15)

    def test_truediv_matter(self):
        """ (int, float) = Matter / Matter """
        result = self.food_1 / self.food_2
        self.assertEqual(self.food_1.amount, 60)
        self.assertEqual(self.food_2.amount, 15)
        self.assertEqual(result, 60 / 15)


if __name__ == '__main__':
    unittest.main()