import unittest
from copy import deepcopy

from piperabm.tools.dictionary_custom_arithmetic import compare_common_vals, compare_vals, compare_keys


class TestCompareKeysFunction(unittest.TestCase):

    def test_0(self):
        main = {
            'a': 1,
            'b': 2,
        }
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
    
    def test_1(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = {
            'a': 3,
            'b': 2,
            'c': 0
        }
        shared_keys, uncommon_keys = compare_keys(main, other)
        expected_result = ['a', 'b']
        self.assertListEqual(shared_keys, expected_result)
        expected_result = []
        self.assertListEqual(uncommon_keys['main'], expected_result)
        expected_result = []
        self.assertListEqual(uncommon_keys['other'], expected_result)

    def test_2(self):
        main = {
            'b': 2,
            'c': 0
        }
        other = {
            'a': 3,
            'b': 2,
            'c': 0
        }
        shared_keys, uncommon_keys = compare_keys(main, other)
        expected_result = ['b']
        self.assertListEqual(shared_keys, expected_result)
        expected_result = []
        self.assertListEqual(uncommon_keys['main'], expected_result)
        expected_result = ['a']
        self.assertListEqual(uncommon_keys['other'], expected_result)

    def test_3(self):
        main = {
            'a': 1,
            'b': 2,
            'c': 0
        }
        other = {
            'a': 3,
        }
        shared_keys, uncommon_keys = compare_keys(main, other)
        expected_result = ['a']
        self.assertListEqual(shared_keys, expected_result)
        expected_result = ['b']
        self.assertListEqual(uncommon_keys['main'], expected_result)
        expected_result = []
        self.assertListEqual(uncommon_keys['other'], expected_result)


class TestCompareValFunction1(unittest.TestCase):

    def test_0(self):
        main = {
            'c': 0,
        }
        other = {}
        result = compare_common_vals(main, other)
        self.assertTrue(result)
        result = compare_vals(main, other)
        self.assertTrue(result)

    def test_1(self):
        main = {}
        other = {
            'c': 0,
        }
        result = compare_common_vals(main, other)
        self.assertTrue(result)
        result = compare_vals(main, other)
        self.assertTrue(result)

    def test_2(self):
        main = {
            'c': 0,
        }
        other = {
            'c': 0,
        }
        result = compare_common_vals(main, other)
        self.assertTrue(result)
        result = compare_vals(main, other)
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
            'd': 0
        }
        result = compare_common_vals(main, other)
        self.assertTrue(result)
        result = compare_vals(main, other)
        self.assertFalse(result)

    def test_1(self):
        main = self.main
        other = {
            'a': 2,
            'b': 3
        }
        result = compare_common_vals(main, other)
        self.assertTrue(result)
        result = compare_vals(main, other)
        self.assertTrue(result)

    def test_2(self):
        main = self.main
        other = {
            'a': 2,
            'b': 3,
            'c': 0,
        }
        result = compare_common_vals(main, other)
        self.assertTrue(result)
        result = compare_vals(main, other)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()