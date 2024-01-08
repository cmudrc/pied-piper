import unittest

from piperabm.object.delta import Delta
from piperabm.object.delta.delta import DeltaList, DeltaDict


class TestDeltaDictClass_Simple(unittest.TestCase):

    def test_create(self):
        old_variable = {'a': 2, 'b': 'sample'}
        new_variable = {'a': 3, 'b': 'sample'}
        delta = DeltaDict.create(old_variable, new_variable)
        self.assertDictEqual(delta, {'a': 1})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(new_variable, {'a': 3, 'b': 'sample'})

        old_variable = {'a': 2, 'b': 'sample'}
        new_variable = {'a': 2, 'b': 'sample'}
        delta = DeltaDict.create(old_variable, new_variable)
        self.assertDictEqual(delta, {})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})

        old_variable = None
        new_variable = {'a': 2, 'b': 'sample'}
        delta = DeltaDict.create(old_variable, new_variable)
        self.assertDictEqual(delta, {'a': 2, 'b': 'sample'})
        self.assertEqual(old_variable, None)
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})

        old_variable = {'a': 2, 'b': 'sample'}
        new_variable = None
        delta = DeltaDict.create(old_variable, new_variable)
        self.assertEqual(delta, None)
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertEqual(new_variable, None)

        old_variable = {}
        new_variable = {'a': 2, 'b': 'sample'}
        delta = DeltaDict.create(old_variable, new_variable)
        self.assertDictEqual(delta, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(old_variable, {})
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})

        old_variable = {'a': 2, 'b': 'sample'}
        new_variable = {}
        delta = DeltaDict.create(old_variable, new_variable)
        self.assertDictEqual(delta, {})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(new_variable, {})

        old_variable = {'a': 2, 'b': 'sample'}
        new_variable = {'a': 2, 'c': 3, 'b': 'sample'}
        delta = DeltaDict.create(old_variable, new_variable)
        self.assertEqual(delta, {'c': 3})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(new_variable, {'a': 2, 'c': 3, 'b': 'sample'})

    def test_apply(self):
        old_variable = {'a': 2, 'b': 'sample'}
        delta = {'a': 1}
        new_variable = DeltaDict.apply(old_variable, delta)
        self.assertDictEqual(new_variable, {'a': 3, 'b': 'sample'})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(delta, {'a': 1})

        old_variable = {'a': 2, 'b': 'sample'}
        delta = {}
        new_variable = DeltaDict.apply(old_variable, delta)
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(delta, {})

        old_variable = None
        delta = {'a': 2, 'b': 'sample'}
        new_variable = DeltaDict.apply(old_variable, delta)
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})
        self.assertEqual(old_variable, None)
        self.assertDictEqual(delta, {'a': 2, 'b': 'sample'})  

        old_variable = {'a': 2, 'b': 'sample'}
        delta = None
        new_variable = DeltaDict.apply(old_variable, delta)
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertEqual(delta, None)

        old_variable = {}
        delta = {'a': 2, 'b': 'sample'}
        new_variable = DeltaDict.apply(old_variable, delta)
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(old_variable, {})
        self.assertDictEqual(delta, {'a': 2, 'b': 'sample'})

        old_variable = {'a': 2, 'b': 'sample'}
        delta = {}
        new_variable = DeltaDict.apply(old_variable, delta)
        self.assertDictEqual(new_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertDictEqual(delta, {})

        old_variable = {'a': 2, 'b': 'sample'}
        delta = {'c': 3, 'b': 'sample'}
        new_variable = DeltaDict.apply(old_variable, delta)
        self.assertDictEqual(new_variable, {'c': 3, 'a': 2, 'b': 'sample'})
        self.assertDictEqual(old_variable, {'a': 2, 'b': 'sample'})
        self.assertEqual(delta, {'c': 3, 'b': 'sample'})
        

class TestDeltaDictClass(unittest.TestCase):

    def test_1(self):
        var_old = {}
        delta = {
            'a': 'b',
            'b': 1,
            'c': True,
            'd': {
                'a': 'b',
                'b': 1,
                'c': True,
            },
            'e': [{'b': 3}]
        }
        var_new = Delta.apply(var_old, delta)
        self.assertDictEqual(var_new, delta)
        created_delta = Delta.create({}, var_new)
        self.assertDictEqual(delta, created_delta)

    def test_2(self):
        """
        Only one entry has changed in the depth of dictionary
        """
        var_old = {
            'float': 1,
            'bool': False,
            'str': 'John',
            'dict': {
                'float': 1,
                'bool': False,
                'str': 'John',
                'dict': {
                    'float': 1,
                    'bool': False,
                    'str': 'John',
                }
            }
        }
        var_new = {
            'float': 1,
            'bool': False,
            'str': 'John',
            'dict': {
                'float': 1,
                'bool': False,
                'str': 'John',
                'dict': {
                    'float': 2,
                    'bool': False,
                    'str': 'John',
                }
            }
        }
        delta = DeltaDict.create(var_old, var_new)
        expected_result = {'dict': {'dict': {'float': 1}}}
        self.assertDictEqual(delta, expected_result)

    def test_create_delta(self):
        var_old = {
            'float': 1,
            'bool': False,
            'str': 'John',
            'dict': {
                'float': 1,
                'bool': False,
                'str': 'John',
                'dict': {
                    'float': 1,
                    'bool': False,
                    'str': 'John',
                }
            }
        }
        var_new = {
            'float': 3,
            'bool': True,
            'str': 'Peter',
            'dict': {
                'float': 3,
                'bool': True,
                'str': 'Peter',
                'dict': {
                    'float': 3,
                    'bool': True,
                    'str': 'Peter',
                }
            }
        }
        delta = Delta.create(var_old, var_new)
        expected_result = {
            'float': 2,
            'bool': True,
            'str': 'Peter',
            'dict': {
                'float': 2,
                'bool': True,
                'str': 'Peter',
                'dict': {
                    'float': 2,
                    'bool': True,
                    'str': 'Peter',
                }
            }
        }
        self.maxDiff = None
        self.assertDictEqual(delta, expected_result)

    def test_apply_delta(self):
        var_old = {
            'float': 1,
            'bool': False,
            'str': 'John',
            'dict': {
                'float': 1,
                'bool': False,
                'str': 'John',
                'dict': {
                    'float': 1,
                    'bool': False,
                    'str': 'John',
                }
            }
        }
        delta = {
            'float': 2,
            'bool': True,
            'str': 'Peter',
            'dict': {
                'float': 2,
                'bool': True,
                'str': 'Peter',
                'dict': {
                    'float': 2,
                    'bool': True,
                    'str': 'Peter',
                }
            }
        }
        var_new = DeltaDict.apply(var_old, delta)
        expected_result = {
            'float': 3,
            'bool': True,
            'str': 'Peter',
            'dict': {
                'float': 3,
                'bool': True,
                'str': 'Peter',
                'dict': {
                    'float': 3,
                    'bool': True,
                    'str': 'Peter',
                }
            }
        }
        self.maxDiff = None
        self.assertDictEqual(var_new, expected_result)

    def test_apply_delta_none(self):
        var_old = None
        delta = {
            'float': 3,
            'bool': True,
            'str': 'Peter',
            'dict': {
                'float': 3,
                'bool': True,
                'str': 'Peter',
            }
        }
        var_new = Delta.apply(var_old, delta)
        self.assertDictEqual(var_new, delta)

        var_old = {
            'float': 3,
            'bool': True,
            'str': 'Peter',
            'dict': {
                'float': 3,
                'bool': True,
                'str': 'Peter',
            }
        }
        delta = None
        var_new = Delta.apply(var_old, delta)
        self.assertDictEqual(var_new, var_old)

    def test_delta_new(self):
        var_old = {'a': 1}
        var_new = {'a': 3, 'b': 4}
        delta = Delta.create(var_old, var_new)
        expected_result = {'a': 2, 'b':4}
        self.assertDictEqual(delta, expected_result)
        updated_var = Delta.apply(var_old, delta)
        self.assertDictEqual(var_new, updated_var)


class TestDeltaListClass(unittest.TestCase):

    def setUp(self) -> None:
        self.list_old = [3, True, 'Peter']
        self.list_new = [2, False, 'John', 'New']
        self.delta = [-1, False, 'John', 'New']
    
    def test_create_delta(self):
        delta = DeltaList.create(self.list_old, self.list_new)
        self.assertListEqual(delta, self.delta)

    def test_apply_delta(self):
        list_new = DeltaList.apply(self.list_old, self.delta)
        self.assertListEqual(list_new, self.list_new)


class TestListDictConversion(unittest.TestCase):

    def setUp(self) -> None:
        self.list = [3, True, 'Peter']
        self.dict = {0: 3, 1: True, 2: 'Peter'}
    
    def test_list_to_dict(self):
        dict = DeltaList.list_to_dict(self.list)
        self.assertDictEqual(dict, self.dict)

    def test_dict_to_list(self):
        list = DeltaList.dict_to_list(self.dict)
        self.assertListEqual(list, self.list)


if __name__ == '__main__':
    unittest.main()
    