import unittest

from piperabm.tools import Delta


class TestDeltaClass_List(unittest.TestCase):

    def test_0(self):
        old_variable = [{'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'}, [1, 2]]
        new_variable = [{'main': {'b': 3, 'c': 4}, 'other': None}, [2, 3, 4]]
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertListEqual(old_variable, [{'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'}, [1, 2]])
        self.assertListEqual(new_variable, [{'main': {'b': 3, 'c': 4}, 'other': None}, [2, 3, 4]])
        self.assertListEqual(updated_variable, new_variable)

    def test_1(self):
        old_variable = None
        new_variable = [{'main': {'b': 3, 'c': 4}, 'other': None}, [2, 3, 4]]
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, None)
        self.assertListEqual(new_variable, [{'main': {'b': 3, 'c': 4}, 'other': None}, [2, 3, 4]])
        self.assertListEqual(updated_variable, new_variable)

    def test_2(self):
        old_variable = [{'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'}, [1, 2]]
        new_variable = None
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertListEqual(old_variable, [{'main': {'a': 1, 'b': 2}, 'extra': 'Aslan'}, [1, 2]])
        self.assertEqual(new_variable, None)
        self.assertEqual(updated_variable, new_variable)


if __name__ == '__main__':
    unittest.main()
    