import unittest
from copy import deepcopy

from piperabm.tools.dictionary_custom_arithmetic import mul


class TestSubDictFunction(unittest.TestCase):

    def test_float(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = 2
        result = mul(main, other)
        expected_result = {
            'a': 2,
            'b': 4,
        }
        self.assertDictEqual(result, expected_result)

    def test_dict(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = {
            'b': 3,
            'c': 4,
        }
        result = mul(main, other)
        expected_result = {
            'a': 1,
            'b': 6,
            'c': 0
        }
        self.assertDictEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()