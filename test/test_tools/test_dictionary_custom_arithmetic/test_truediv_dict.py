import unittest
from copy import deepcopy

from piperabm.tools.dictionary_custom_arithmetic import truediv


class TestSubDictFunction(unittest.TestCase):

    def test_float(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = 2
        result = truediv(main, other)
        expected_result = {
            'a': 0.5,
            'b': 1,
        }
        self.assertDictEqual(result, expected_result)

    def test_dict(self):
        main = {
            'a': 1,
            'b': 2,
        }
        other = {
            'b': 2,
            'c': 4,
        }
        result = truediv(main, other)
        expected_result = {
            'b': 1,
            'c': 0
        }
        self.assertDictEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()