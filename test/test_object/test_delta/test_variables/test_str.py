import unittest

from piperabm.object.variables import DeltaStr


class TestFloatDeltaClass(unittest.TestCase):

    def test_create(self):
        var_old = 'John'
        var_new = 'Peter'
        delta = DeltaStr.create(var_old, var_new)
        self.assertEqual(delta, 'Peter')

        var_old = 'John'
        var_new = 'John'
        delta = DeltaStr.create(var_old, var_new)
        self.assertEqual(delta, None)

        var_old = None
        var_new = 'John'
        delta = DeltaStr.create(var_old, var_new)
        self.assertEqual(delta, 'John')

    def test_apply(self):
        var_old = 'John'
        delta = 'Peter'
        delta = DeltaStr.apply(var_old, delta)
        self.assertEqual(delta, 'Peter')

        var_old = 'John'
        delta = None
        delta = DeltaStr.apply(var_old, delta)
        self.assertEqual(delta, 'John')

        var_old = None
        delta = 'John'
        delta = DeltaStr.apply(var_old, delta)
        self.assertEqual(delta, 'John')    


if __name__ == "__main__":
    unittest.main()