import unittest
from copy import deepcopy

from piperabm.matter import DeltaMatter
from piperabm.matter.delta_matter.samples import delta_matter_0, delta_matter_1, delta_matter_3
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestDeltaMatterClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.delta_food_1 = deepcopy(delta_matter_0)
        self.delta_food_2 = deepcopy(delta_matter_3)
        self.delta_water = deepcopy(delta_matter_1)

    def test_serialization(self):
        dictionary = self.delta_water.serialize()
        delta_water = DeltaMatter()
        delta_water.deserialize(dictionary)

    def test_value(self):
        value = self.delta_food_1.value(exchange_rate)
        self.assertEqual(value, 50)

    def test_of_value(self):
        delta_matter = DeltaMatter(name='food')
        delta_matter.from_value(50, exchange_rate)
        self.assertEqual(delta_matter.amount, 5)

    def test_add_0(self):
        """ DeltaMatter + (int, flaot) """
        result = self.delta_food_1 + 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, 13)

    def test_add_1(self):
        """ DeltaMatter + DeltaMatter """
        result = self.delta_food_1 + self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, 13)

    def test_sum(self):
        """ sum() """
        delta_matter_list = [self.delta_food_1, self.delta_food_2]
        start = DeltaMatter(name=self.delta_food_1.name)
        result = sum(delta_matter_list, start)
        self.assertEqual(result.amount, 13)

    def test_sub_0(self):
        """ DeltaMatter - (int, flaot) """
        result = self.delta_food_1 - 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, -3)

    def test_sub_1(self):
        """ DeltaMatter - DeltaMatter """
        result = self.delta_food_1 - self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, -3)

    def test_mul_0(self):
        """ DeltaMatter * (int, flaot) """
        result = self.delta_food_1 * 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, 40)

    def test_mul_1(self):
        """ DeltaMatter * DeltaMatter """
        result = self.delta_food_1 * self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, 40)

    def test_truediv_0(self):
        """ DeltaMatter / (int, flaot) """
        result = self.delta_food_1 / 8
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(result.amount, 5/8)

    def test_truediv_1(self):
        """ DeltaMatter / DeltaMatter """
        result = self.delta_food_1 / self.delta_food_2
        self.assertEqual(self.delta_food_1.amount, 5)
        self.assertEqual(self.delta_food_2.amount, 8)
        self.assertEqual(result.amount, 5/8)


if __name__ == '__main__':
    unittest.main()