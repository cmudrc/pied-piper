import unittest

from piperabm.resource.add import add_function


class TestAddFunction(unittest.TestCase):

    def test_add_0(self):
        new_current_amount, remaining = add_function(
            amount=5,
            current_amount=5,
            max_amount=10
        )
        self.assertEqual(new_current_amount, 10)
        self.assertEqual(remaining, 0)

    def test_add_1(self):
        new_current_amount, remaining = add_function(
            amount=6,
            current_amount=5,
            max_amount=10
        )
        self.assertEqual(new_current_amount, 10)
        self.assertEqual(remaining, 1)

    def test_add_2(self):
        new_current_amount, remaining = add_function(
            amount=6,
            current_amount=5,
            max_amount=None
        )
        self.assertEqual(new_current_amount, 11)
        self.assertEqual(remaining, 0)

    def test_add_3(self):
        new_current_amount, remaining = add_function(
            amount=-6,
            current_amount=5,
            max_amount=10
        )
        self.assertEqual(new_current_amount, 0)
        self.assertEqual(remaining, -1)

    def test_add_4(self):
        new_current_amount, remaining = add_function(
            amount=-6,
            current_amount=5,
            max_amount=None
        )
        self.assertEqual(new_current_amount, 0)
        self.assertEqual(remaining, -1)


if __name__ == "__main__":
    unittest.main()