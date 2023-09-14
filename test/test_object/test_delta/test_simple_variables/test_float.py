import unittest

from piperabm.object.delta.simple_variables.float import DeltaFloat


class TestDeltaFloatClass(unittest.TestCase):

    def test_create(self):
        var_old = 2
        new_var = 5
        delta = DeltaFloat.create(var_old, new_var)
        self.assertEqual(delta, 3)

        var_old = None
        new_var = 3
        delta = DeltaFloat.create(var_old, new_var)
        self.assertEqual(delta, 3)

        var_old = 3
        new_var = 3
        delta = DeltaFloat.create(var_old, new_var)
        self.assertEqual(delta, None)

    def test_apply(self):
        var_old = 2
        delta = 3
        new_var = DeltaFloat.apply(var_old, delta)
        self.assertEqual(new_var, 5)

        var_old = None
        delta = 3
        new_var = DeltaFloat.apply(var_old, delta)
        self.assertEqual(new_var, 3)

        var_old = 3
        delta = None
        new_var = DeltaFloat.apply(var_old, delta)
        self.assertEqual(new_var, 3) 


if __name__ == '__main__':
    unittest.main()