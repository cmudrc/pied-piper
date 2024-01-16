import unittest
from copy import deepcopy

from piperabm.matter import DeltaMatters
from piperabm.matter.delta_matters import delta_matters_sum
from piperabm.matter.delta_matter.samples import delta_matter_3, delta_matter_4
from piperabm.matter.delta_matters.samples import delta_matters_0, delta_matters_1
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestDeltaMattersClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.delta_matters_0 = deepcopy(delta_matters_0)
        self.delta_matters_1 = deepcopy(delta_matters_1)
        self.delta_food = deepcopy(delta_matter_3)
        self.delta_water = deepcopy(delta_matter_4)

    def test_serialization(self):
        dictionary = self.delta_matters_0.serialize()
        delta_matters = DeltaMatters()
        delta_matters.deserialize(dictionary)

    def test_add(self):
        """ DeltaMatters + DeltaMatter """
        result = self.delta_matters_0 + self.delta_food
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_food.amount, 8)
        self.assertEqual(result('food'), 13)
        self.assertEqual(result('water'), 6)
        self.assertEqual(result('energy'), 7)

        """ DeltaMatters + DeltaMatters """
        result = self.delta_matters_0 + self.delta_matters_1
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_matters_1('food'), 8)
        self.assertEqual(self.delta_matters_1('water'), 9)
        self.assertEqual(self.delta_matters_1('energy'), 10)
        self.assertEqual(result('food'), 13)
        self.assertEqual(result('water'), 15)
        self.assertEqual(result('energy'), 17)

    def test_sub(self):
        """ DeltaMatters - DeltaMatter """
        result = self.delta_matters_0 - self.delta_food
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_food.amount, 8)
        self.assertEqual(result('food'), -3)
        self.assertEqual(result('water'), 6)
        self.assertEqual(result('energy'), 7)

        """ DeltaMatters - DeltaMatters """
        result = self.delta_matters_0 - self.delta_matters_1
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_matters_1('food'), 8)
        self.assertEqual(self.delta_matters_1('water'), 9)
        self.assertEqual(self.delta_matters_1('energy'), 10)
        self.assertEqual(result('food'), -3)
        self.assertEqual(result('water'), -3)
        self.assertEqual(result('energy'), -3)

    def test_mul(self):
        """ DeltaMatters * (int, flaot) """
        result = self.delta_matters_0 * 8
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(result('food'), 40)
        self.assertEqual(result('water'), 48)
        self.assertEqual(result('energy'), 56)

        """ DeltaMatters * DeltaMatter """
        result = self.delta_matters_0 * self.delta_food
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_food.amount, 8)
        self.assertEqual(result('food'), 40)
        self.assertEqual(result('water'), 6)
        self.assertEqual(result('energy'), 7)

        """ DeltaMatters * DeltaMatters """
        result = self.delta_matters_0 * self.delta_matters_1
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_matters_1('food'), 8)
        self.assertEqual(self.delta_matters_1('water'), 9)
        self.assertEqual(self.delta_matters_1('energy'), 10)
        self.assertEqual(result('food'), 40)
        self.assertEqual(result('water'), 54)
        self.assertEqual(result('energy'), 70)

    def test_truediv(self):
        """ DeltaMatters / (int, flaot) """
        result = self.delta_matters_0 / 8
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(result('food'), 5/8)
        self.assertEqual(result('water'), 6/8)
        self.assertEqual(result('energy'), 7/8)

        """ DeltaMatters / DeltaMatter """
        result = self.delta_matters_0 / self.delta_food
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_food.amount, 8)
        self.assertEqual(result('food'), 5/8)
        self.assertEqual(result('water'), 6)
        self.assertEqual(result('energy'), 7)

        """ DeltaMatters / DeltaMatters """
        result = self.delta_matters_0 / self.delta_matters_1
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_matters_1('food'), 8)
        self.assertEqual(self.delta_matters_1('water'), 9)
        self.assertEqual(self.delta_matters_1('energy'), 10)
        self.assertEqual(result('food'), 5/8)
        self.assertEqual(result('water'), 6/9)
        self.assertEqual(result('energy'), 7/10)

    def test_sum(self):
        """ sum() """
        delta_matters_list = [self.delta_matters_0, self.delta_matters_1]
        result = delta_matters_sum(delta_matters_list)
        self.assertEqual(self.delta_matters_0('food'), 5)
        self.assertEqual(self.delta_matters_0('water'), 6)
        self.assertEqual(self.delta_matters_0('energy'), 7)
        self.assertEqual(self.delta_matters_1('food'), 8)
        self.assertEqual(self.delta_matters_1('water'), 9)
        self.assertEqual(self.delta_matters_1('energy'), 10)
        self.assertEqual(result('food'), 13)
        self.assertEqual(result('water'), 15)
        self.assertEqual(result('energy'), 17)

    def test_value(self):
        """ total values """
        value = self.delta_matters_0.value(exchange_rate)
        self.assertEqual(value, 90)

        """ value by name """
        values = self.delta_matters_0.value(exchange_rate, total=False)
        expected_result = {
            'food': 50,
            'water': 12,
            'energy': 28,
        }
        self.assertDictEqual(values, expected_result)

    def test_of_values(self):
        values = {
            'food': 50,
            'water': 12,
            'energy': 28,
        }
        delta_matters = DeltaMatters()
        delta_matters.of_values(values, exchange_rate)
        self.assertEqual(delta_matters, self.delta_matters_0)


if __name__ == '__main__':
    unittest.main()