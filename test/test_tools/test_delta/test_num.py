import unittest

from piperabm.tools import Delta


class TestDeltaClass_Num(unittest.TestCase):

    def test_0(self):
        old_variable = 2
        new_variable = 2
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, 2)
        self.assertEqual(new_variable, 2)
        self.assertEqual(updated_variable, new_variable)

    def test_1(self):
        old_variable = 2
        new_variable = 5
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, 2)
        self.assertEqual(new_variable, 5)
        self.assertEqual(updated_variable, new_variable)

    def test_2(self):
        old_variable = 5
        new_variable = 2
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, 5)
        self.assertEqual(new_variable, 2)
        self.assertEqual(updated_variable, new_variable)

    def test_3(self):
        old_variable = 3
        new_variable = None
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, 3)
        self.assertEqual(new_variable, None)
        self.assertEqual(updated_variable, new_variable)

    def test_4(self):
        old_variable = None
        new_variable = 3
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, None)
        self.assertEqual(new_variable, 3)
        self.assertEqual(updated_variable, new_variable)
        

if __name__ == '__main__':
    unittest.main()