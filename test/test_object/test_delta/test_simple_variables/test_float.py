import unittest

from piperabm.object.delta.simple_variables.float import DeltaFloat


class TestDeltaFloatClass(unittest.TestCase):

    def test_create(self):
        old_variable = 2
        new_variable = 5
        delta = DeltaFloat.create(old_variable, new_variable)
        self.assertEqual(delta, 3)
        self.assertEqual(old_variable, 2)
        self.assertEqual(new_variable, 5)

        old_variable = None
        new_variable = 3
        delta = DeltaFloat.create(old_variable, new_variable)
        self.assertEqual(delta, 3)
        self.assertEqual(old_variable, None)
        self.assertEqual(new_variable, 3)

        old_variable = 3
        new_variable = 3
        delta = DeltaFloat.create(old_variable, new_variable)
        self.assertEqual(delta, None)
        self.assertEqual(old_variable, 3)
        self.assertEqual(new_variable, 3)

    def test_apply(self):
        old_variable = 2
        delta = 3
        new_variable = DeltaFloat.apply(old_variable, delta)
        self.assertEqual(new_variable, 5)
        self.assertEqual(old_variable, 2)
        self.assertEqual(delta, 3)

        old_variable = None
        delta = 3
        new_variable = DeltaFloat.apply(old_variable, delta)
        self.assertEqual(new_variable, 3)
        self.assertEqual(old_variable, None)
        self.assertEqual(delta, 3)

        old_variable = 3
        delta = None
        new_variable = DeltaFloat.apply(old_variable, delta)
        self.assertEqual(new_variable, 3)
        self.assertEqual(old_variable, 3)
        self.assertEqual(delta, None) 


if __name__ == '__main__':
    unittest.main()