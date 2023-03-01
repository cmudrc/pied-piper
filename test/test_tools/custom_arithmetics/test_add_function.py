import unittest

from piperabm.tools.custom_arithmetics import add_function


class TestAddFunction(unittest.TestCase):

    def test_0(self):
        result, remaining = add_function(
            amount=5,
            current_amount=6
        )
        self.assertEqual(result, 11)
        self.assertEqual(remaining, 0)

    def test_1(self):
        """
        With *max_amount*
        """
        result, remaining = add_function(
            amount=2,
            current_amount=6,
            max_amount=10
        )
        self.assertEqual(result, 8)
        self.assertEqual(remaining, 0)

    def test_2(self):
        """
        With overflow and *max_amount*
        """
        result, remaining = add_function(
            amount=5,
            current_amount=6,
            max_amount=10
        )
        self.assertEqual(result, 10)
        self.assertEqual(remaining, 1)


if __name__ == "__main__":
    unittest.main()