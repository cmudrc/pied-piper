import unittest
from copy import deepcopy

from piperabm.resource import ResourceDelta
from piperabm.resource.samples import resource_delta_0
from piperabm.economy.exchange_rate.samples import exchange_rate_0


class TestResourceDeltaClass(unittest.TestCase):
    
    def setUp(self) -> None:
        self.rate = deepcopy(resource_delta_0)

    def test_call(self):
        rate = self.rate('food')
        self.assertEqual(rate, 6)

    def test_all_names(self):
        names = self.rate.all_names()
        expected_result = ['food', 'water', 'energy']
        self.assertListEqual(names, expected_result)

    def test_set_get(self):
        self.rate.set_amount('food', 0)
        self.assertEqual(self.rate.get_amount('food'), 0)

    def test_zeros(self):
        resource_delta = ResourceDelta()
        resource_delta.create_zeros(['food', 'water', 'energy'])
        expected_result = {'energy': 0, 'food': 0, 'water': 0}
        self.assertDictEqual(resource_delta.to_dict(), expected_result)
        self.assertTrue(resource_delta.is_all_zero())

    def test_is_all_zero(self):
        self.assertFalse(self.rate.is_all_zero())

    def test_value(self):
        value = self.rate.value(exchange_rate_0)
        expected_result = {'food': 60.0, 'water': 8.0, 'energy': 12.0}
        self.assertDictEqual(value, expected_result)

    def test_gt(self):
        delta = ResourceDelta({'energy': 2, 'food': 5, 'water': 3})
        self.assertTrue(self.rate > delta)
        self.assertFalse(delta > self.rate)
        delta = ResourceDelta({'energy': 2, 'food': 7, 'water': 3})
        self.assertFalse(self.rate > delta)
        self.assertFalse(delta > self.rate)
        delta = ResourceDelta({'energy': 2, 'food': 5})
        self.assertTrue(self.rate > delta)
        self.assertFalse(delta > self.rate)
        delta = ResourceDelta({'energy': 2, 'food': 6, 'water': 3, 'other': 1})
        self.assertFalse(self.rate > delta)
        self.assertFalse(delta > self.rate)    

    def test_lt(self):
        delta = ResourceDelta({'energy': 2, 'food': 5, 'water': 3})
        self.assertTrue(delta < self.rate)
        self.assertFalse(self.rate < delta)
        delta = ResourceDelta({'energy': 2, 'food': 7, 'water': 3})
        self.assertFalse(self.rate < delta)
        self.assertFalse(delta < self.rate)
        delta = ResourceDelta({'energy': 2, 'food': 5})
        self.assertFalse(self.rate < delta)
        self.assertTrue(delta < self.rate)
        delta = ResourceDelta({'energy': 2, 'food': 6, 'water': 3, 'other': 1})
        self.assertFalse(self.rate < delta)
        #self.assertFalse(delta < self.rate)

    def test_mul(self):
        self.rate * 2
        expected_result = {'energy': 6, 'food': 12, 'water': 8}
        self.assertDictEqual(self.rate.to_dict(), expected_result)

    def test_div(self):
        self.rate / 0.5
        expected_result = {'energy': 6, 'food': 12, 'water': 8}
        self.assertDictEqual(self.rate.to_dict(), expected_result)

    def test_dict(self):
        dictionary = self.rate.to_dict()
        expected_result = {'food': 6, 'water': 4, 'energy': 3}
        self.assertEqual(dictionary, expected_result)
        rate = ResourceDelta()
        rate.from_dict(dictionary)
        self.assertEqual(rate, self.rate)

    def test_delta(self):
        rate_previous = deepcopy(self.rate)
        self.rate.db['food'].amount = 8
        delta = self.rate - rate_previous
        expected_delta = {'food': 2}
        self.assertDictEqual(delta, expected_delta)
        rate_previous + delta
        self.assertEqual(rate_previous, self.rate)


if __name__ == "__main__":
    unittest.main()
