import unittest
from copy import deepcopy

from piperabm.matter import Containers
from piperabm.matter.containers.samples import containers_0, containers_1
from piperabm.matter.container.samples import container_0
from piperabm.matter.matter.samples import matter_0
from piperabm.matter.matters.samples import matters_1
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestContainersClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.containers_1 = deepcopy(containers_0)
        self.containers_2 = deepcopy(containers_1)
        self.container = deepcopy(container_0)
        self.matter = deepcopy(matter_0)
        self.matters = deepcopy(matters_1)

    def test_value(self):
        """ total values """
        value = self.containers_1.value(exchange_rate)
        self.assertEqual(value, 60 * 10 + 70 * 2 + 80 * 4)

        """ value by name """
        values = self.containers_1.value(exchange_rate, total=False)
        expected_result = {
            'food': 60 * 10,
            'water': 70 * 2,
            'energy': 80 * 4,
        }
        self.assertDictEqual(values, expected_result)

    def test_to_matters(self):
        matters = self.containers_1.to_matters()
        self.assertEqual(matters.type, 'matters')
        self.assertEqual(matters('food'), 60)
        self.assertEqual(matters('water'), 70)
        self.assertEqual(matters('energy'), 80)

    def test_serialization(self):
        dictionary = self.containers_1.serialize()
        containers = Containers()
        containers.deserialize(dictionary)
        self.assertEqual(self.containers_1, containers)
    
    def test_add_dict(self):
        """ Matters = Containers + dict """
        dictionary = self.matters.amounts()
        remainders = self.containers_1 + dictionary
        self.assertEqual(self.containers_1('food'), 60 + 15)
        self.assertEqual(self.containers_1('water'), 70 + 10)
        self.assertEqual(self.containers_1('energy'), 80 + 5)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)

    def test_add_matter(self):
        """ Matter = Containers + Matter """
        remainder = self.containers_1 + self.matter
        self.assertEqual(self.containers_1('food'), 100)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.matter.amount, 60)
        self.assertEqual(remainder.amount, 20)
    
    def test_add_matters(self):
        """ Matters = Containers + Matters """
        remainders = self.containers_1 + self.matters
        self.assertEqual(self.containers_1('food'), 60 + 15)
        self.assertEqual(self.containers_1('water'), 70 + 10)
        self.assertEqual(self.containers_1('energy'), 80 + 5)
        self.assertEqual(self.matters('food'), 15)
        self.assertEqual(self.matters('water'), 10)
        self.assertEqual(self.matters('energy'), 5)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)
    
    def test_add_container(self):
        """ Containers = Containers + Container """
        new_containers = self.containers_1 + self.container
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.container.amount, 60)
        self.assertEqual(new_containers('food'), 60 + 60)
        self.assertEqual(new_containers('water'), 70)
        self.assertEqual(new_containers('energy'), 80)
    
    def test_add_containers(self):
        """ Containers = Containers + Containers """
        new_containers = self.containers_1 + self.containers_2
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.containers_2('food'), 15)
        self.assertEqual(self.containers_2('water'), 10)
        self.assertEqual(self.containers_2('energy'), 5)
        self.assertEqual(new_containers('food'), 60 + 15)
        self.assertEqual(new_containers('water'), 70 + 10)
        self.assertEqual(new_containers('energy'), 80 + 5)
    
    def test_sub_dict(self):
        """ Matters = Containers - dict """
        dictionary = self.matters.amounts()
        remainders = self.containers_1 - dictionary
        self.assertEqual(self.containers_1('food'), 60 - 15)
        self.assertEqual(self.containers_1('water'), 70 - 10)
        self.assertEqual(self.containers_1('energy'), 80 - 5)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)
    
    def test_sub_matter(self):
        """ Matter = Containers - Matter """
        remainder = self.containers_1 - self.matter
        self.assertEqual(self.containers_1('food'), 60 - 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.matter.amount, 60)
        self.assertEqual(remainder.amount, 0)
    
    def test_sub_matters(self):
        """ Matters = Containers - Matters """
        remainders = self.containers_1 - self.matters
        self.assertEqual(self.containers_1('food'), 60 - 15)
        self.assertEqual(self.containers_1('water'), 70 - 10)
        self.assertEqual(self.containers_1('energy'), 80 - 5)
        self.assertEqual(self.matters('food'), 15)
        self.assertEqual(self.matters('water'), 10)
        self.assertEqual(self.matters('energy'), 5)
        self.assertEqual(remainders('food'), 0)
        self.assertEqual(remainders('water'), 0)
        self.assertEqual(remainders('energy'), 0)
    
    def test_sub_container(self):
        """ Containers = Containers - Container """
        new_containers = self.containers_1 - self.container
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.container.amount, 60)
        self.assertEqual(new_containers('food'), 60 - 60)
        self.assertEqual(new_containers('water'), 70)
        self.assertEqual(new_containers('energy'), 80)

    def test_sub_containers(self):
        """ Containers = Containers - Containers """
        new_containers = self.containers_1 - self.containers_2
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.containers_2('food'), 15)
        self.assertEqual(self.containers_2('water'), 10)
        self.assertEqual(self.containers_2('energy'), 5)
        self.assertEqual(new_containers('food'), 60 - 15)
        self.assertEqual(new_containers('water'), 70 - 10)
        self.assertEqual(new_containers('energy'), 80 - 5)
    
    def test_mul_int_float(self):
        """ Containers = Containers * (int, float) """
        new_containers = self.containers_1 * 10
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(new_containers('food'), 60 * 10)
        self.assertEqual(new_containers('water'), 70 * 10)
        self.assertEqual(new_containers('energy'), 80 * 10)

    def test_mul_dict(self):
        """ Containers = Containers * dict """
        dictionary = self.matters.amounts()
        new_containers = self.containers_1 * dictionary
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(new_containers('food'), 60 * 15)
        self.assertEqual(new_containers('water'), 70 * 10)
        self.assertEqual(new_containers('energy'), 80 * 5)

    def test_truediv_int_float(self):
        """ Containers = Containers / (int, float) """
        new_containers = self.containers_1 / 10
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(new_containers('food'), 60 / 10)
        self.assertEqual(new_containers('water'), 70 / 10)
        self.assertEqual(new_containers('energy'), 80 / 10)

    def test_truediv_dict(self):
        """ Containers = Containers / dict """
        dictionary = self.matters.amounts()
        new_containers = self.containers_1 / dictionary
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(new_containers('food'), 60 / 15)
        self.assertEqual(new_containers('water'), 70 / 10)
        self.assertEqual(new_containers('energy'), 80 / 5)

    def test_truediv_matter(self):
        """ (int, float) = Containers / Matter """
        ratio = self.containers_1 / self.matter
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.matter.amount, 60)
        self.assertEqual(ratio, 60 / 60)
    
    def test_truediv_matters(self):
        """ dict = Containers / Matters """
        ratios = self.containers_1 / self.matters
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.matters('food'), 15)
        self.assertEqual(self.matters('water'), 10)
        self.assertEqual(self.matters('energy'), 5)
        self.assertEqual(ratios['food'], 60 / 15)
        self.assertEqual(ratios['water'], 70 / 10)
        self.assertEqual(ratios['energy'], 80 / 5)
    
    def test_truediv_container(self):
        """ (int, float) = Containers / Container """
        ratio = self.containers_1 / self.matter
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.matter.amount, 60)
        self.assertEqual(ratio, 60 / 60)
    
    def test_truediv_containers(self):
        """ dict = Containers / Containers """
        ratios = self.containers_1 / self.containers_2
        self.assertEqual(self.containers_1('food'), 60)
        self.assertEqual(self.containers_1('water'), 70)
        self.assertEqual(self.containers_1('energy'), 80)
        self.assertEqual(self.containers_2('food'), 15)
        self.assertEqual(self.containers_2('water'), 10)
        self.assertEqual(self.containers_2('energy'), 5)
        self.assertEqual(ratios['food'], 60 / 15)
        self.assertEqual(ratios['water'], 70 / 10)
        self.assertEqual(ratios['energy'], 80 / 5)


if __name__ == '__main__':
    unittest.main()