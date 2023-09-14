import unittest

from piperabm.object.delta.simple_variables.bool import DeltaBool


class TestDeltaBoolClass(unittest.TestCase):
    
    def test_create(self):
        var_old = True
        var_new = True
        delta = DeltaBool.create(var_old, var_new)
        self.assertEqual(delta, None)

        var_old = True
        var_new = False
        delta = DeltaBool.create(var_old, var_new)
        self.assertFalse(delta)

        var_old = False
        var_new = True
        delta = DeltaBool.create(var_old, var_new)
        self.assertTrue(delta)

        var_old = False
        var_new = False
        delta = DeltaBool.create(var_old, var_new)
        self.assertEqual(delta, None)

        var_old = None
        var_new = True
        delta = DeltaBool.create(var_old, var_new)
        self.assertTrue(delta)

        var_old = None
        var_new = False
        delta = DeltaBool.create(var_old, var_new)
        self.assertFalse(delta)

        var_old = True
        var_new = None
        delta = DeltaBool.create(var_old, var_new)
        self.assertEqual(delta, None)

        var_old = False
        var_new = None
        delta = DeltaBool.create(var_old, var_new)
        self.assertEqual(delta, None)

    def test_apply(self):
        var_old = True
        delta = True
        var_new = DeltaBool.apply(var_old, delta)
        self.assertTrue(var_new)

        var_old = True
        delta = False
        var_new = DeltaBool.apply(var_old, delta)
        self.assertFalse(var_new)

        var_old = False
        delta = True
        var_new = DeltaBool.apply(var_old, delta)
        self.assertTrue(var_new)

        var_old = False
        delta = False
        var_new = DeltaBool.apply(var_old, delta)
        self.assertFalse(var_new)

        var_old = True
        delta = None
        var_new = DeltaBool.apply(var_old, delta)
        self.assertEqual(var_new, var_old)

        var_old = False
        delta = None
        var_new = DeltaBool.apply(var_old, delta)
        self.assertEqual(var_new, var_old)

        var_old = None
        delta = True
        var_new = DeltaBool.apply(var_old, delta)
        self.assertTrue(var_new)

        var_old = None
        delta = False
        var_new = DeltaBool.apply(var_old, delta)
        self.assertFalse(var_new)


if __name__ == '__main__':
    unittest.main()