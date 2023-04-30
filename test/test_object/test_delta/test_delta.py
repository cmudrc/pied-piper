import unittest

from piperabm.object.delta import Delta
from piperabm.object.delta import list_to_dict, dict_to_list


class TestDictDeltaClass(unittest.TestCase):

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
        delta = Delta.create_delta(var_old, var_new)
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
        var_new = Delta.apply_delta(var_old, delta)
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
        var_new = Delta.apply_delta(var_old, delta)
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
        var_new = Delta.apply_delta(var_old, delta)
        self.assertDictEqual(var_new, var_old)


class TestListDeltaClass(unittest.TestCase):

    def setUp(self) -> None:
        self.list_old = [3, True, 'Peter']
        self.list_new = [2, False, 'John']
        self.delta = {0: -1, 1: True, 2: 'John'}
    
    def test_create_delta(self):
        delta = Delta.create_list_delta(self.list_old, self.list_new)
        self.assertDictEqual(delta, self.delta)

    def test_apply_delta(self):
        list_new = Delta.apply_list_delta(self.list_old, self.delta)
        print(list_new)


class TestListDictConversion(unittest.TestCase):

    def setUp(self) -> None:
        self.list = [3, True, 'Peter']
        self.dict = {0: 3, 1: True, 2: 'Peter'}
    
    def test_list_to_dict(self):
        dict = list_to_dict(self.list)
        self.assertDictEqual(dict, self.dict)

    def test_dict_to_list(self):
        list = dict_to_list(self.dict)
        self.assertListEqual(list, self.list)


if __name__ == "__main__":
    unittest.main()
    