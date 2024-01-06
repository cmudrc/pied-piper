import unittest

from piperabm.object.delta.simple_variables.str import DeltaStr


class TestDeltaStrClass(unittest.TestCase):

    def test_create(self):
        old_variable = 'John'
        new_variable = 'Peter'
        delta = DeltaStr.create(old_variable, new_variable)
        self.assertEqual(delta, 'Peter')
        self.assertEqual(old_variable, 'John')
        self.assertEqual(new_variable, 'Peter')

        old_variable = 'John'
        new_variable = 'John'
        delta = DeltaStr.create(old_variable, new_variable)
        self.assertEqual(delta, None)
        self.assertEqual(old_variable, 'John')
        self.assertEqual(new_variable, 'John')

        old_variable = None
        new_variable = 'John'
        delta = DeltaStr.create(old_variable, new_variable)
        self.assertEqual(delta, 'John')
        self.assertEqual(old_variable, None)
        self.assertEqual(new_variable, 'John')

    def test_apply(self):
        old_variable = 'John'
        delta = 'Peter'
        new_variable = DeltaStr.apply(old_variable, delta)
        self.assertEqual(new_variable, 'Peter')
        self.assertEqual(old_variable, 'John')
        self.assertEqual(delta, 'Peter')

        old_variable = 'John'
        delta = None
        new_variable = DeltaStr.apply(old_variable, delta)
        self.assertEqual(new_variable, 'John')
        self.assertEqual(old_variable, 'John')
        self.assertEqual(delta, None)

        old_variable = None
        delta = 'John'
        new_variable = DeltaStr.apply(old_variable, delta)
        self.assertEqual(new_variable, 'John')
        self.assertEqual(old_variable, None)
        self.assertEqual(delta, 'John') 


if __name__ == '__main__':
    unittest.main()