import unittest

from piperabm.resource.sub import sub_function


class TestAddFunction(unittest.TestCase):
   
    def test_sub_0(self):
        new_current_amount, remaining = sub_function(
            amount=6,
            current_amount=5
        )
        self.assertEqual(new_current_amount, 0)
        self.assertEqual(remaining, 1)

    def test_sub_1(self):
        new_current_amount, remaining = sub_function(
            amount=6,
            current_amount=5
        )
        self.assertEqual(new_current_amount, 0)
        self.assertEqual(remaining, 1)


if __name__ == "__main__":
    unittest.main()