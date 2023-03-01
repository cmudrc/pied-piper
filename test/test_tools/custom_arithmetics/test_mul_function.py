import unittest

from piperabm.tools.custom_arithmetics import mul_function


class TestMulFunction(unittest.TestCase):

    def test_0(self):
        result, remaining = mul_function(
            mul_val=2,
            current_amount=6
        )
        self.assertEqual(result, 12)
        self.assertEqual(remaining, 0)

    def test_1(self):
        result, remaining = mul_function(
            mul_val=2,
            current_amount=6,
            max_amount=10
        )
        self.assertEqual(result, 10)
        self.assertEqual(remaining, 2)


if __name__ == "__main__":
    unittest.main()