import unittest
from copy import deepcopy

from piperabm.matter import Matters
from piperabm.matter.matters import matters_sum
from piperabm.matter.matter.samples import matter_3, matter_4
from piperabm.matter.matters.samples import matters_0, matters_1
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestDeltaMattersClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.matters_1 = deepcopy(matters_0)
        self.matters_2 = deepcopy(matters_1)
        self.food = deepcopy(matter_3)
        self.water = deepcopy(matter_4)

    def test_value(self):
        """ total values """
        value = self.matters_1.value(exchange_rate)
        self.assertEqual(value, (60 * 10) + (70 * 2) + (80 * 4))

        """ value by name """
        values = self.matters_1.value(exchange_rate, total=False)
        expected_result = {
            'food': 60 * 10,
            'water': 70 * 2,
            'energy': 80 * 4,
        }
        self.assertDictEqual(values, expected_result)

    def test_from_values(self):
        values = {
            'food': 60 * 10,
            'water': 70 * 2,
            'energy': 80 * 4,
        }
        matters = Matters()
        matters.from_values(values, exchange_rate)
        self.assertEqual(matters, self.matters_1)

    def test_amounts(self):
        expected_result = {
            'food': 60,
            'water': 70,
            'energy': 80,
        }
        self.assertEqual(self.matters_1.amounts(), expected_result)

    def test_from_amounts(self):
        amounts = {
            'food': 60,
            'water': 70,
            'energy': 80,
        }
        matters = Matters()
        matters.from_amounts(amounts)
        self.assertEqual(matters, self.matters_1)

    def test_serialization(self):
        dictionary = self.matters_1.serialize()
        matters = Matters()
        matters.deserialize(dictionary)
        self.assertEqual(self.matters_1, matters)
    
    def test_add_0(self):
        """ Matters = Matters + dict """
        dictionary = {
            'food': 15,
            'water': 10,
            'energy': 5,
        }
        result = self.matters_1 + dictionary
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(result('food'), 60 + 15)
        self.assertEqual(result('water'), 70 + 10)
        self.assertEqual(result('energy'), 80 + 5)

    def test_add_1(self):
        """ Matters = Matters + Matter """
        result = self.matters_1 + self.food
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.food.amount, 15)
        self.assertEqual(result('food'), 60 + 15)
        self.assertEqual(result('water'), 70)
        self.assertEqual(result('energy'), 80)

    def test_add_2(self):
        """ Matters = Matters + Matters """
        result = self.matters_1 + self.matters_2
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.matters_2('food'), 15)
        self.assertEqual(self.matters_2('water'), 10)
        self.assertEqual(self.matters_2('energy'), 5)
        self.assertEqual(result('food'), 60 + 15)
        self.assertEqual(result('water'), 70 + 10)
        self.assertEqual(result('energy'), 80 + 5)
    
    def test_sum(self):
        """ Matters = sum(Matters) """
        matters_list = [self.matters_1, self.matters_2]
        result = matters_sum(matters_list)
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.matters_2('food'), 15)
        self.assertEqual(self.matters_2('water'), 10)
        self.assertEqual(self.matters_2('energy'), 5)
        self.assertEqual(result('food'), 60 + 15)
        self.assertEqual(result('water'), 70 + 10)
        self.assertEqual(result('energy'), 80 + 5)
    
    def test_sub_0(self):
        """ Matters = Matters - dict """
        dictionary = {
            'food': 15,
            'water': 10,
            'energy': 5,
        }
        result = self.matters_1 - dictionary
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(result('food'), 60 - 15)
        self.assertEqual(result('water'), 70 - 10)
        self.assertEqual(result('energy'), 80 - 5)

    def test_sub_1(self):
        """ Matters = Matters - Matter """
        result = self.matters_1 - self.food
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.food.amount, 15)
        self.assertEqual(result('food'), 60 - 15)
        self.assertEqual(result('water'), 70)
        self.assertEqual(result('energy'), 80)

    def test_sub_2(self):
        """ Matters = Matters - Matters """
        result = self.matters_1 - self.matters_2
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.matters_2('food'), 15)
        self.assertEqual(self.matters_2('water'), 10)
        self.assertEqual(self.matters_2('energy'), 5)
        self.assertEqual(result('food'), 60 - 15)
        self.assertEqual(result('water'), 70 - 10)
        self.assertEqual(result('energy'), 80 - 5)
    
    def test_mul_0(self):
        """ Matters = Matters * (int, flaot) """
        result = self.matters_1 * 10
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(result('food'), 60 * 10)
        self.assertEqual(result('water'), 70 * 10)
        self.assertEqual(result('energy'), 80 * 10)
    
    def test_mul_1(self):
        """ Matters = Matters * dict """
        dictionary = {
            'food': 15,
            'water': 10,
            'energy': 5,
        }
        result = self.matters_1 * dictionary
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(result('food'), 60 * 15)
        self.assertEqual(result('water'), 70 * 10)
        self.assertEqual(result('energy'), 80 * 5)

    def test_mul_2(self):
        """ Matters = Matters * Matter """
        result = self.matters_1 * self.food
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.food.amount, 15)
        self.assertEqual(result('food'), 60 * 15)
        self.assertEqual(result('water'), 70)
        self.assertEqual(result('energy'), 80)
    
    def test_mul_3(self):
        """ Matters = Matters * Matters """
        result = self.matters_1 * self.matters_2
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.matters_2('food'), 15)
        self.assertEqual(self.matters_2('water'), 10)
        self.assertEqual(self.matters_2('energy'), 5)
        self.assertEqual(result('food'), 60 * 15)
        self.assertEqual(result('water'), 70 * 10)
        self.assertEqual(result('energy'), 80 * 5)

    def test_truediv_0(self):
        """ Matters = Matters / (int, flaot) """
        result = self.matters_1 / 10
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(result('food'), 60 / 10)
        self.assertEqual(result('water'), 70 / 10)
        self.assertEqual(result('energy'), 80 / 10)
    
    def test_truediv_1(self):
        """ Matters = Matters / dict """
        dictionary = {
            'food': 15,
            'water': 10,
            'energy': 5,
        }
        result = self.matters_1 / dictionary
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(result('food'), 60 / 15)
        self.assertEqual(result('water'), 70 / 10)
        self.assertEqual(result('energy'), 80 / 5)
    
    def test_truediv_2(self):
        """ (int, float) = Matters / Matter """
        ratio = self.matters_1 / self.food
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.food.amount, 15)
        self.assertEqual(ratio, 60 / 15)

    def test_truediv_3(self):
        """ dict = Matters / Matters """
        ratios = self.matters_1 / self.matters_2
        self.assertEqual(self.matters_1('food'), 60)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 80)
        self.assertEqual(self.matters_2('food'), 15)
        self.assertEqual(self.matters_2('water'), 10)
        self.assertEqual(self.matters_2('energy'), 5)
        self.assertEqual(ratios['food'], 60 / 15)
        self.assertEqual(ratios['water'], 70 / 10)
        self.assertEqual(ratios['energy'], 80 / 5)


if __name__ == '__main__':
    unittest.main()