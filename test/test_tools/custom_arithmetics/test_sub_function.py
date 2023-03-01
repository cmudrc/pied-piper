import unittest

from piperabm.tools.custom_arithmetics import sub_function


class TestSubFunction(unittest.TestCase):

    def test_0(self):
        result, remaining = sub_function(
            amount=2,
            current_amount=6
        )
        self.assertEqual(result, 4)
        self.assertEqual(remaining, 0)

    def test_1(self):
        """
        With overflow
        """
        result, remaining = sub_function(
            amount=8,
            current_amount=6
        )
        self.assertEqual(result, 0)
        self.assertEqual(remaining, 2)

    def test_2(self):
        """
        With overflow and *min_amount*
        """
        result, remaining = sub_function(
            amount=8,
            current_amount=6,
            min_amount=2
        )
        self.assertEqual(result, 2)
        self.assertEqual(remaining, 4)


if __name__ == "__main__":
    unittest.main()