import unittest

from piperabm.tools import Delta


class TestDeltaClass_Bool(unittest.TestCase):

    def test_0(self):
        old_variable = True
        new_variable = True
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertTrue(old_variable)
        self.assertTrue(new_variable)
        self.assertTrue(updated_variable)

    def test_1(self):
        old_variable = False
        new_variable = True
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertFalse(old_variable)
        self.assertTrue(new_variable)
        self.assertTrue(updated_variable)

    def test_2(self):
        old_variable = None
        new_variable = True
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, None)
        self.assertTrue(new_variable)
        self.assertTrue(updated_variable)

    def test_3(self):
        old_variable = True
        new_variable = None
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertTrue(old_variable)
        self.assertEqual(new_variable, None)
        self.assertEqual(updated_variable, None)
        

if __name__ == '__main__':
    unittest.main()