import unittest
from copy import deepcopy

from piperabm.resource.arithmetic import compare_val
from piperabm.resource.arithmetic.dict_compare import compare_keys


class TestCompareKeysFunction(unittest.TestCase):

    main = {
        'a': 1,
        'b': 2,
    }

    def test_0(self):
        main = self.main
        other = {
            'b': 3,
            'c': 4,
        }
        shared_keys, uncommon_keys = compare_keys(main, other)
        expected_result = ['b']
        self.assertListEqual(shared_keys, expected_result)
        expected_result = ['a']
        self.assertListEqual(uncommon_keys['main'], expected_result)
        expected_result = ['c']
        self.assertListEqual(uncommon_keys['other'], expected_result)


class TestCompareValFunction1(unittest.TestCase):

    main = {
        'c': 0,
    }

    def test_0(self):
        main = self.main
        other = {}
        result = compare_val(main, other)
        self.assertTrue(result)

    def test_1(self):
        main = self.main
        other = {
            'c': 0,
        }
        result = compare_val(main, other)
        self.assertTrue(result)


class TestCompareValFunction2(unittest.TestCase):

    main = {
        'a': 2,
        'b': 3,
        'c': 0,
    }

    def test_0(self):
        main = self.main
        other = {
            'a': 2,
        }
        result = compare_val(main, other)
        self.assertFalse(result)

    def test_1(self):
        main = self.main
        other = {
            'a': 2,
            'b': 3
        }
        result = compare_val(main, other)
        self.assertTrue(result)

    def test_2(self):
        main = self.main
        other = {
            'a': 2,
            'b': 3,
            'c': 0,
        }
        result = compare_val(main, other)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()