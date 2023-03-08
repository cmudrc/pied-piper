import unittest
from copy import deepcopy

from piperabm.resource.dictionary_custom_arithmetic import dict_add


class TestAddDictFunction(unittest.TestCase):

    def test_0(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = {
            'b': 3,
            'c': 4,
        }
        result, remaining = dict_add(main, other)
        expected_result = {
            'a': 1,
            'b': 5,
            'c': 4
        }
        self.assertDictEqual(result, expected_result)
        expected_remaining = {
            'a': 0,
            'b': 0,
            'c': 0,
        }
        self.assertDictEqual(remaining, expected_remaining)

    def test_1(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = {
            'b': 3,
            'c': 4,
        }
        max = {
            'b': 4
        }
        result, remaining = dict_add(main, other, max)
        expected_result = {
            'a': 1,
            'b': 4,
            'c': 4
        }
        self.assertDictEqual(result, expected_result)
        expected_remaining = {
            'a': 0,
            'b': 1,
            'c': 0,
        }
        self.assertDictEqual(remaining, expected_remaining)


if __name__ == "__main__":
    unittest.main()