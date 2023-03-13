import unittest

from piperabm.resource.dictionary_custom_arithmetic import dict_max


class TestDictMaxFunction(unittest.TestCase):

    def test_max_0(self):
        dictionary = {'a': 1, 'b': 2}
        result = dict_max(dictionary)
        self.assertEqual(result, 'b')

    def test_max_1(self):
        dictionary = {'a': 1, 'b': None}
        result = dict_max(dictionary)
        self.assertEqual(result, 'b')


if __name__ == "__main__":
    unittest.main()