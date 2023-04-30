import unittest

from piperabm.object.delta_var import DeltaFloat


class TestFloatDeltaClass(unittest.TestCase):

    def test_create_float_delta(self):
        var_old = 2
        new_var = 5
        delta = DeltaFloat.create_float_delta(var_old, new_var)
        self.assertEqual(delta, 3)

        var_old = None
        new_var = 3
        delta = DeltaFloat.create_float_delta(var_old, new_var)
        self.assertEqual(delta, 3)

        var_old = 3
        new_var = 3
        delta = DeltaFloat.create_float_delta(var_old, new_var)
        self.assertEqual(delta, None)

    def test_apply_float_delta(self):
        var_old = 2
        delta = 3
        new_var = DeltaFloat.apply_float_delta(var_old, delta)
        self.assertEqual(new_var, 5)

        var_old = None
        delta = 3
        new_var = DeltaFloat.apply_float_delta(var_old, delta)
        self.assertEqual(new_var, 3)

        var_old = 3
        delta = None
        new_var = DeltaFloat.apply_float_delta(var_old, delta)
        self.assertEqual(new_var, 3) 


if __name__ == "__main__":
    unittest.main()