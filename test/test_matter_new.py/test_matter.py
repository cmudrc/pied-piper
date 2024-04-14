import unittest

from piperabm.matter_new import Matter
from piperabm.economy.exchange_rate.samples import exchange_rate_1 as exchange_rate


class TestMatterClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.resource_1 = Matter({
            'food': 3,
            'water': 2,
            'energy': 1,
        })
        self.resource_2 = Matter({
            'food': 1,
            'water': 1,
            'energy': 1,
        })

    def test_serialization(self):
        dictionary = self.resource_1.serialize()
        matter = Matter()
        matter.deserialize(dictionary)
        self.assertEqual(self.resource_1, matter)

    def test_value(self):
        value = self.resource_1.value(prices=exchange_rate.prices)
        self.assertEqual(value, 38)

    def test_of_value(self):
        matter = Matter()
        #matter.from_value(600, exchange_rate)
        #self.assertEqual(matter.amount, 60)
    
    def test_check_empty(self):
        result = self.resource_2.check_empty(names=['energy'])
        self.assertListEqual(result, [])
        resource = self.resource_1 - self.resource_2
        result = resource.check_empty(names=['energy'])
        self.assertListEqual(result, ['energy'])


if __name__ == '__main__':
    unittest.main()