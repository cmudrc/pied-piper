import unittest

from piperabm.tools import Delta


class TestDeltaClass_Dict(unittest.TestCase):

    def test_0(self):
        old_variable = {'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'}
        new_variable = {'main': {'b': 3, 'c': 4}, 'other': None}
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertDictEqual(old_variable, {'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'})
        self.assertDictEqual(new_variable, {'main': {'b': 3, 'c': 4}, 'other': None})
        self.assertDictEqual(updated_variable, new_variable)

    def test_1(self):
        old_variable = None
        new_variable = {'main': {'b': 3, 'c': 4}, 'other': None}
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, None)
        self.assertDictEqual(new_variable, {'main': {'b': 3, 'c': 4}, 'other': None})
        self.assertDictEqual(updated_variable, new_variable)

    def test_2(self):
        old_variable = {'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'}
        new_variable = None
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertDictEqual(old_variable, {'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'})
        self.assertEqual(new_variable, None)
        self.assertEqual(updated_variable, new_variable)


if __name__ == '__main__':
    unittest.main()
    