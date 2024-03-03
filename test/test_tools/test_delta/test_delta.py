import unittest

from piperabm.tools import Delta


class TestDeltaClass(unittest.TestCase):

    def test_0(self):
        old_variable = None
        new_variable = None
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertEqual(old_variable, None)
        self.assertEqual(new_variable, None)
        self.assertEqual(updated_variable, new_variable)

    def test_1(self):
        old_variable = {
            'float': 1,
            'bool': True,
            'str': 'Peter',
            'dict': {
                'float': 1,
                'bool': True,
                'str': 'Peter',
                'dict': {
                    'float': 1,
                    'bool': True,
                    'str': 'Peter',
                }
            },
            'list': [
                3,
                True,
                'Peter',
                {
                    'float': 1,
                    'bool': True,
                    'str': 'Peter',
                },
                [
                    1,
                    True,
                    'Peter'
                ]
            ],
        }
        new_variable = {
            'float': 2,
            'bool': False,
            'str': 'John',
            'dict': {
                'float': 2,
                'bool': False,
                'str': 'John',
                'dict': {
                    'float': 2,
                    'bool': False,
                    'str': 'John',
                }
            },
            'list': [
                2,
                False,
                'John',
                {
                    'float': 2,
                    'bool': False,
                    'str': 'John',
                },
                [
                    2,
                    False,
                    'John'
                ]
            ],
        }
        delta = Delta.create(old_variable, new_variable)
        updated_variable = Delta.apply(old_variable, delta)
        self.assertDictEqual(updated_variable, new_variable)


if __name__ == '__main__':
    unittest.main()
    