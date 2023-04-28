import unittest

from piperabm.object.delta.delta import Delta


class TestDeltaClass(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
    