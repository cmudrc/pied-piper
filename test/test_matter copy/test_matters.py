import unittest
from copy import deepcopy

from piperabm.matter import Matters
from piperabm.matter.matter.samples import matter_0
from piperabm.matter.matters.samples import matters_0, matters_1
from piperabm.matter.delta_matter.samples import delta_matter_0
from piperabm.matter.delta_matters.samples import delta_matters_0
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestMattersClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.matters_0 = deepcopy(matters_0)
        self.matters_1 = deepcopy(matters_1)
        self.matter = deepcopy(matter_0)
        self.delta_matter = deepcopy(delta_matter_0)
        self.delta_matters = deepcopy(delta_matters_0)

    def test_value(self):
        """ total values """
        value = self.matters_0.value(exchange_rate)
        self.assertEqual(value, 30 * 10 + 40 * 2 + 50 * 4)

        """ value by name """
        values = self.matters_0.value(exchange_rate, total=False)
        expected_result = {
            'food': 30 * 10,
            'water': 40 * 2,
            'energy': 50 * 4,
        }
        self.assertDictEqual(values, expected_result)

    def test_add_0(self):
        """ Matters + dict """
        dictionary = self.delta_matters.amounts()
        remainders = self.matters_0 + dictionary
        self.assertEqual(self.matters_0('food'), 30 + 5)
        self.assertEqual(self.matters_0('water'), 40 + 6)
        self.assertEqual(self.matters_0('energy'), 50 + 7)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)

    def test_add_1(self):
        """ Matters + DeltaMatter """
        remainder = self.matters_0 + self.delta_matter
        self.assertEqual(self.matters_0('food'), 30 + 5)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.delta_matter.amount, 5)
        self.assertEqual(remainder.amount, 0)

    def test_add_2(self):
        """ Matters + DeltaMatters """
        remainders = self.matters_0 + self.delta_matters
        self.assertEqual(self.matters_0('food'), 30 + 5)
        self.assertEqual(self.matters_0('water'), 40 + 6)
        self.assertEqual(self.matters_0('energy'), 50 + 7)
        self.assertEqual(self.delta_matters('food'), 5)
        self.assertEqual(self.delta_matters('water'), 6)
        self.assertEqual(self.delta_matters('energy'), 7)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)

    def test_add_3(self):
        """ Matters + Matter """
        remainder = self.matters_0 + self.matter
        self.assertEqual(self.matters_0('food'), 30 + 30)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.matter.amount, 30)
        self.assertEqual(remainder.amount, 0)

    def test_add_4(self):
        """ Matters + Matters """
        remainders = self.matters_0 + self.matters_1
        self.assertEqual(self.matters_0('food'), 100)
        self.assertEqual(self.matters_0('water'), 100)
        self.assertEqual(self.matters_0('energy'), 100)
        self.assertEqual(self.matters_1('food'), 80)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 60)
        self.assertEqual(remainders('food'), 10)
        self.assertEqual(remainders('water'), 10)
        self.assertEqual(remainders('energy'), 10)

    def test_sub_0(self):
        """ Matters - dict """
        dictionary = self.delta_matters.amounts()
        remainders = self.matters_0 - dictionary
        self.assertEqual(self.matters_0('food'), 30 - 5)
        self.assertEqual(self.matters_0('water'), 40 - 6)
        self.assertEqual(self.matters_0('energy'), 50 - 7)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)

    def test_sub_1(self):
        """ Matters - DeltaMatter """
        remainder = self.matters_0 - self.delta_matter
        self.assertEqual(self.matters_0('food'), 30 - 5)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.delta_matter.amount, 5)
        self.assertEqual(remainder.amount, 0)

    def test_sub_2(self):
        """ Matters - DeltaMatters """
        remainders = self.matters_0 - self.delta_matters
        self.assertEqual(self.matters_0('food'), 30 - 5)
        self.assertEqual(self.matters_0('water'), 40 - 6)
        self.assertEqual(self.matters_0('energy'), 50 - 7)
        self.assertEqual(self.delta_matters('food'), 5)
        self.assertEqual(self.delta_matters('water'), 6)
        self.assertEqual(self.delta_matters('energy'), 7)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)

    def test_sub_3(self):
        """ Matters - Matter """
        remainder = self.matters_0 - self.matter
        self.assertEqual(self.matters_0('food'), 30 - 30)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.matter.amount, 30)
        self.assertEqual(remainder.amount, 0)

    def test_sub_4(self):
        """ Matters + Matters """
        remainders = self.matters_0 - self.matters_1
        self.assertEqual(self.matters_0('food'), 0)
        self.assertEqual(self.matters_0('water'), 0)
        self.assertEqual(self.matters_0('energy'), 0)
        self.assertEqual(self.matters_1('food'), 80)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 60)
        self.assertEqual(remainders('food'), 50)
        self.assertEqual(remainders('water'), 30)
        self.assertEqual(remainders('energy'), 10)

    def test_mul(self):
        """ Matters * dict """
        dictionary = self.delta_matters.amounts()
        self.matters_0 * dictionary
        self.assertEqual(self.matters_0('food'), 30 * 5)
        self.assertEqual(self.matters_0('water'), 40 * 6)
        self.assertEqual(self.matters_0('energy'), 50 * 7)

    def test_truediv_0(self):
        """ Matters / dict """
        dictionary = self.delta_matters.amounts()
        result = self.matters_0 / dictionary
        self.assertEqual(self.matters_0('food'), 30)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(result['food'], 30 / 5)
        self.assertEqual(result['water'], 40 / 6)
        self.assertEqual(result['energy'], 50 / 7)

    def test_truediv_1(self):
        """ Matters / DeltaMatter """
        result = self.matters_0 / self.delta_matter
        self.assertEqual(self.matters_0('food'), 30)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.delta_matter.amount, 5)
        self.assertEqual(result['food'], 30 / 5)

    def test_truediv_2(self):
        """ Matters / DeltaMatters """
        result = self.matters_0 / self.delta_matters
        self.assertEqual(self.matters_0('food'), 30)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.delta_matter.amount, 5)
        self.assertEqual(result['food'], 30 / 5)
        self.assertEqual(result['water'], 40 / 6)
        self.assertEqual(result['energy'], 50 / 7)

    def test_truediv_3(self):
        """ Matters / Matter """
        result = self.matters_0 / self.matter
        self.assertEqual(self.matters_0('food'), 30)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.matter.amount, 30)
        self.assertEqual(result['food'], 30 / 30)

    def test_truediv_4(self):
        """ Matters / Matters """
        result = self.matters_0 / self.matters_1
        self.assertEqual(self.matters_0('food'), 30)
        self.assertEqual(self.matters_0('water'), 40)
        self.assertEqual(self.matters_0('energy'), 50)
        self.assertEqual(self.matters_1('food'), 80)
        self.assertEqual(self.matters_1('water'), 70)
        self.assertEqual(self.matters_1('energy'), 60)
        self.assertEqual(result['food'], 30 / 80)
        self.assertEqual(result['water'], 40 / 70)
        self.assertEqual(result['energy'], 50 / 60)


if __name__ == '__main__':
    unittest.main()