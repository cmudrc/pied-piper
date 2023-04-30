import unittest

from piperabm.tools.symbols import SYMBOLS, serialize_symbol, deserialize_symbol


class TestSymbols(unittest.TestCase):

    def test_serialize_inf(self):
        var = SYMBOLS['inf']
        result = serialize_symbol(var)
        expected_result = 'inf'
        self.assertEqual(result, expected_result)

    def test_deserialize_inf(self):
        var = 'inf'
        result = deserialize_symbol(var)
        expected_result = SYMBOLS['inf']
        self.assertEqual(result, expected_result)

    def test_serialize_eps(self):
        var = SYMBOLS['eps']
        result = serialize_symbol(var)
        expected_result = 'eps'
        self.assertEqual(result, expected_result)

    def test_deserialize_eps(self):
        var = 'eps'
        result = deserialize_symbol(var)
        expected_result = SYMBOLS['eps']
        self.assertEqual(result, expected_result)

    def test_serialize_other(self):
        var = 1000
        result = serialize_symbol(var)
        expected_result = 1000
        self.assertEqual(result, expected_result)

    def test_deserialize_other(self):
        var = 'number'
        result = deserialize_symbol(var)
        expected_result = 'number'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()