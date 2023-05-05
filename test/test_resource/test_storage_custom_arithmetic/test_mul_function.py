import unittest

from piperabm.resource.dictionary_custom_arithmetic.storage_arithmetic import mul_function


class TestMulFunction(unittest.TestCase):

    def test_0(self):
        result, remaining = mul_function(
            current_amount=6,
            mul_val=2
        )
        self.assertEqual(result, 12)
        self.assertEqual(remaining, 0)

    def test_1(self):
        result, remaining = mul_function(
            current_amount=6,
            mul_val=2,
            max_amount=10
        )
        self.assertEqual(result, 10)
        self.assertEqual(remaining, 2)

    def test_2(self):
        result, remaining = mul_function(
            current_amount=6,
            mul_val=0.2,
            min_amount=2
        )
        self.assertEqual(result, 2)
        self.assertAlmostEqual(remaining, 0.8)

    def test_none_0(self):
        result, remaining = mul_function(
            current_amount=6,
            mul_val=None,
            max_amount=10
        )
        self.assertEqual(result, 10)
        self.assertEqual(remaining, None)

    def test_none_1(self):
        result, remaining = mul_function(
            current_amount=None,
            mul_val=2
        )
        self.assertEqual(result, None)
        self.assertEqual(remaining, 0)


if __name__ == "__main__":
    unittest.main()