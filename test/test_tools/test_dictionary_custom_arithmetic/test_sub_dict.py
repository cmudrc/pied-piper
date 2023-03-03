import unittest
from copy import deepcopy

from piperabm.tools.dictionary_custom_arithmetic import sub


class TestSubDictFunction(unittest.TestCase):

    def test_0(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = {
            'b': 3,
            'c': 4,
        }
        result, remaining = sub(main, other)
        expected_result = {
            'a': 1,
            'b': 0,
            'c': 0
        }
        self.assertDictEqual(result, expected_result)
        expected_remaining = {
            'a': 0,
            'b': 1,
            'c': 4,
        }
        self.assertDictEqual(remaining, expected_remaining)


if __name__ == "__main__":
    unittest.main()