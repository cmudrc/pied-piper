import unittest

from piperabm.object.delta_var import DeltaBool


class TestBoolDeltaClass(unittest.TestCase):
    
    def test_create_bool_delta(self):
        var_old = True
        var_new = False
        delta = DeltaBool.create_bool_delta(var_old, var_new)
        self.assertTrue(delta)

        var_old = True
        var_new = True
        delta = DeltaBool.create_bool_delta(var_old, var_new)
        self.assertEqual(delta, None)

        var_old = False
        var_new = False
        delta = DeltaBool.create_bool_delta(var_old, var_new)
        self.assertEqual(delta, None)

        var_old = False
        var_new = True
        delta = DeltaBool.create_bool_delta(var_old, var_new)
        self.assertTrue(delta)

    def test_apply_bool_delta(self):
        var_old = True
        delta = None
        var_new = DeltaBool.apply_bool_delta(var_old, delta)
        self.assertTrue(var_new)

        var_old = True
        delta = True
        var_new = DeltaBool.apply_bool_delta(var_old, delta)
        self.assertFalse(var_new)

        var_old = False
        delta = None
        var_new = DeltaBool.apply_bool_delta(var_old, delta)
        self.assertFalse(var_new)

        var_old = False
        delta = True
        var_new = DeltaBool.apply_bool_delta(var_old, delta)
        self.assertTrue(var_new)


if __name__ == "__main__":
    unittest.main()