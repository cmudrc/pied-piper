import unittest

from piperabm.tools import Delta


class TestDeltaClass_Str(unittest.TestCase):

    def test_0(self):
        old_variable = 'Chris'
        new_variable = 'Chris'
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, 'Chris')
        self.assertEqual(new_variable, 'Chris')
        self.assertEqual(updated_variable, new_variable)

    def test_1(self):
        old_variable = 'Chris'
        new_variable = 'Aslan'
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, 'Chris')
        self.assertEqual(new_variable, 'Aslan')
        self.assertEqual(updated_variable, new_variable)

    def test_2(self):
        old_variable = None
        new_variable = 'Aslan'
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, None)
        self.assertEqual(new_variable, 'Aslan')
        self.assertEqual(updated_variable, new_variable)

    def test_3(self):
        old_variable = 'Chris'
        new_variable = None
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, 'Chris')
        self.assertEqual(new_variable, None)
        self.assertEqual(updated_variable, new_variable)


if __name__ == '__main__':
    unittest.main()