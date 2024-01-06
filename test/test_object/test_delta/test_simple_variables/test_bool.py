import unittest

from piperabm.object.delta.simple_variables.bool import DeltaBool


class TestDeltaBoolClass(unittest.TestCase):
    
    def test_create(self):
        old_variable = True
        new_variable = True
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertEqual(delta, None)
        self.assertTrue(old_variable)
        self.assertTrue(new_variable)

        old_variable = True
        new_variable = False
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertFalse(delta)
        self.assertTrue(old_variable)
        self.assertFalse(new_variable)

        old_variable = False
        new_variable = True
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertTrue(delta)
        self.assertFalse(old_variable)
        self.assertTrue(new_variable)

        old_variable = False
        new_variable = False
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertEqual(delta, None)
        self.assertFalse(old_variable)
        self.assertFalse(new_variable)

        old_variable = None
        new_variable = True
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertTrue(delta)
        self.assertEqual(old_variable, None)
        self.assertTrue(new_variable)

        old_variable = None
        new_variable = False
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertFalse(delta)
        self.assertEqual(old_variable, None)
        self.assertFalse(new_variable)

        old_variable = True
        new_variable = None
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertEqual(delta, None)
        self.assertTrue(old_variable)
        self.assertEqual(new_variable, None)

        old_variable = False
        new_variable = None
        delta = DeltaBool.create(old_variable, new_variable)
        self.assertEqual(delta, None)
        self.assertFalse(old_variable)
        self.assertEqual(new_variable, None)

    def test_apply(self):
        old_variable = True
        delta = True
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertTrue(new_variable)
        self.assertTrue(old_variable)
        self.assertTrue(delta)

        old_variable = True
        delta = False
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertFalse(new_variable)
        self.assertTrue(old_variable)
        self.assertFalse(delta)

        old_variable = False
        delta = True
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertTrue(new_variable)
        self.assertFalse(old_variable)
        self.assertTrue(delta)

        old_variable = False
        delta = False
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertFalse(new_variable)
        self.assertFalse(old_variable)
        self.assertFalse(delta)

        old_variable = True
        delta = None
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertEqual(new_variable, old_variable)
        self.assertTrue(old_variable)
        self.assertEqual(delta, None)

        old_variable = False
        delta = None
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertEqual(new_variable, old_variable)
        self.assertFalse(old_variable)
        self.assertEqual(delta, None)

        old_variable = None
        delta = True
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertTrue(new_variable)
        self.assertEqual(old_variable, None)
        self.assertTrue(delta)

        old_variable = None
        delta = False
        new_variable = DeltaBool.apply(old_variable, delta)
        self.assertFalse(new_variable)
        self.assertEqual(old_variable, None)
        self.assertFalse(delta)


if __name__ == '__main__':
    unittest.main()