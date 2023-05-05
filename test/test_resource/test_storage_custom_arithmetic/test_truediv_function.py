import unittest

from piperabm.resource.dictionary_custom_arithmetic.storage_arithmetic import truediv_function


class TestTrueDivFunction(unittest.TestCase):

    def test_0(self):
        result, remaining = truediv_function(
            current_amount=6,
            div_val=2
        )
        self.assertEqual(result, 3)
        self.assertEqual(remaining, 0)

    def test_1(self):
        result, remaining = truediv_function(
            current_amount=6,
            div_val=0.5,
            max_amount=10
        )
        self.assertEqual(result, 10)
        self.assertEqual(remaining, 2)

    def test_2(self):
        result, remaining = truediv_function(
            current_amount=6,
            div_val=3,
            min_amount=3
        )
        self.assertEqual(result, 3)
        self.assertAlmostEqual(remaining, 1)

    def test_none_0(self):
        result, remaining = truediv_function(
            current_amount=6,
            div_val=None
        )
        self.assertEqual(result, 0)
        self.assertEqual(remaining, 0)

    def test_none_1(self):
        result, remaining = truediv_function(
            current_amount=None,
            div_val=2
        )
        self.assertEqual(result, None)
        self.assertEqual(remaining, 0)

    def test_zero_0(self):
        result, remaining = truediv_function(
            current_amount=0,
            div_val=6
        )
        self.assertEqual(result, 0)
        self.assertEqual(remaining, 0)

    def test_zero_1(self):
        result, remaining = truediv_function(
            current_amount=6,
            div_val=0
        )
        self.assertEqual(result, None)
        self.assertEqual(remaining, 0)
    
    def test_zero_none(self):
        result, remaining = truediv_function(
            current_amount=0,
            div_val=None
        )
        self.assertEqual(result, 0)
        self.assertEqual(remaining, 0)

    def test_none_zero(self):
        result, remaining = truediv_function(
            current_amount=None,
            div_val=0
        )
        self.assertEqual(result, None)
        self.assertEqual(remaining, 0)


if __name__ == "__main__":
    unittest.main()