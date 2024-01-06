import unittest

from piperabm.object.delta import Delta
from piperabm.object.delta.delta import DeltaList, DeltaDict


class TestDeltaDictClass(unittest.TestCase):

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

class TestDeltaListClass_1(unittest.TestCase):

    def setUp(self) -> None:
        self.pos_old = [1, 1]
        self.pos_new = [2, 3]
        self.delta = [1, 2]
    
    def test_create_delta(self):
        delta = DeltaList.create(self.pos_old, self.pos_new)
        self.assertListEqual(delta, self.delta)

    def test_apply_delta(self):
        pos_new = DeltaList.apply(self.pos_old, self.delta)
        self.assertListEqual(pos_new, self.pos_new)


class TestDeltaListClass_2(unittest.TestCase):

    def setUp(self) -> None:
        self.list_old = [3, True, 'Peter']
        self.list_new = [2, False, 'John']
        #self.delta = {0: -1, 1: False, 2: 'John'}
        self.delta = [-1, False, 'John']
    
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
    