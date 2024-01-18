import unittest
from copy import deepcopy

from piperabm.matter import Container
from piperabm.matter.container.samples import container_0, container_3
from piperabm.matter.matter.samples import matter_0
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestMatterClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.food_container_1 = deepcopy(container_0)
        self.food_container_2 = deepcopy(container_3)
        self.food = deepcopy(matter_0)

    def test_value(self):
        value = self.food_container_1.value(exchange_rate)
        self.assertEqual(value, 60 * 10)

    def test_serialization(self):
        dictionary = self.food_container_1.serialize()
        container = Container()
        container.deserialize(dictionary)
        self.assertEqual(self.food_container_1, container)

    def test_add_0(self):
        """ Matter = Container + (int, flaot) """
        remainder = self.food_container_1 + 60
        self.assertEqual(self.food_container_1.amount, 100)
        self.assertEqual(remainder.amount, 20)

    def test_add_1(self):
        """ Matter = Container + Matter """
        remainder = self.food_container_1 + self.food
        self.assertEqual(self.food_container_1.amount, 100)
        self.assertEqual(self.food.amount, 60)
        self.assertEqual(remainder.amount, 20)
    
    def test_add_2(self):
        """ Container = Container + Container """
        new_container = self.food_container_1 + self.food_container_2
        self.assertEqual(self.food_container_1.amount, 60)
        self.assertEqual(self.food_container_2.amount, 15)
        self.assertEqual(new_container.amount, 60 + 15)
        self.assertEqual(new_container.min, 0 + 0)
        self.assertEqual(new_container.max, 100 + 50)
    
    def test_sub_0(self):
        """ Matter = Container - (int, flaot) """
        remainder = self.food_container_1 - 80
        self.assertEqual(self.food_container_1.amount, 0)
        self.assertEqual(remainder.amount, 80 - 60)

    def test_sub_1(self):
        """ Matter = Container - Matter """
        remainder = self.food_container_1 - self.food
        self.assertEqual(self.food_container_1.amount, 60 - 60)
        self.assertEqual(remainder.amount, 0)

    def test_sub_2(self):
        """ Container = Container - Container """
        new_container = self.food_container_1 - self.food_container_2
        self.assertEqual(self.food_container_1.amount, 60)
        self.assertEqual(self.food_container_2.amount, 15)
        self.assertEqual(new_container.amount, 60 - 15)
        self.assertEqual(new_container.min, 0 - 0)
        self.assertEqual(new_container.max, 100 - 50)
    
    def test_mul(self):
        """ Container = Container * (int, flaot) """
        new_container = self.food_container_1 * 10
        self.assertEqual(self.food_container_1.amount, 60)
        self.assertEqual(new_container.amount, 60 * 10)
        self.assertEqual(new_container.min, 0 * 10)
        self.assertEqual(new_container.max, 100 * 10)
    
    def test_truediv_0(self):
        """ Container = Container / (int, flaot) """
        new_container = self.food_container_1 / 10
        self.assertEqual(self.food_container_1.amount, 60)
        self.assertEqual(new_container.amount, 60 / 10)
        self.assertEqual(new_container.min, 0 / 10)
        self.assertEqual(new_container.max, 100 / 10)

    def test_truediv_1(self):
        """ (int, float) = Container / Matter """
        ratio = self.food_container_1 / self.food
        self.assertEqual(self.food_container_1.amount, 60)
        self.assertEqual(self.food.amount, 60)
        self.assertEqual(ratio, 60 / 60)

    def test_truediv_2(self):
        """ (int, float) = Container / Container """
        ratio = self.food_container_1 / self.food_container_2
        self.assertEqual(self.food_container_1.amount, 60)
        self.assertEqual(self.food_container_2.amount, 15)
        self.assertEqual(ratio, 60 / 15)

        
if __name__ == '__main__':
    unittest.main()