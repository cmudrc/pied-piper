import unittest

from piperabm.object.delta import DeltaStr


class TestFloatDeltaClass(unittest.TestCase):

    def test_create_str_delta(self):
        var_old = 'John'
        var_new = 'Peter'
        delta = DeltaStr.create_str_delta(var_old, var_new)
        self.assertEqual(delta, 'Peter')

        var_old = 'John'
        var_new = 'John'
        delta = DeltaStr.create_str_delta(var_old, var_new)
        self.assertEqual(delta, None)

    def test_apply_str_delta(self):
        var_old = 'John'
        delta = 'Peter'
        delta = DeltaStr.apply_str_delta(var_old, delta)
        self.assertEqual(delta, 'Peter')

        var_old = 'John'
        delta = None
        delta = DeltaStr.apply_str_delta(var_old, delta)
        self.assertEqual(delta, 'John')

        var_old = None
        delta = 'John'
        delta = DeltaStr.apply_str_delta(var_old, delta)
        self.assertEqual(delta, 'John')    


if __name__ == "__main__":
    unittest.main()