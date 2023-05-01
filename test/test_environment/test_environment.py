import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.samples import environment_0, environment_1
from piperabm.unit import Date
from piperabm.tools.symbols import SYMBOLS


class TestEnvironmentClass_0(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_0)

    def test_dict(self):
        dictionary = self.env.to_dict()
        expected_result = {
            'edges': {},
            'nodes': {0: {'pos': [-2, -2],
                          'structure': {'active': True,
                                        'boundary': {'shape': {'radius': 2.220446049250313e-16,
                                                               'type': 'dot'}},
                                        'end_date': None,
                                        'name': "John's Home",
                                        'progressive_degradation': {'formula_name': 'formula_01',
                                                                    'usage_current': 0,
                                                                    'usage_max': SYMBOLS['inf']},
                                        'start_date': {'day': 2,
                                                       'hour': 0,
                                                       'minute': 0,
                                                       'month': 1,
                                                       'second': 0,
                                                       'year': 2020},
                                        'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                'type': 'dirac '
                                                                                'delta'},
                                                               'unit_size': None},
                                        'type': 'settlement'}}},
            'type': 'environment'}
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        new_env = Environment()
        new_env.from_dict(dictionary)
        new_dictionary = new_env.to_dict()
        self.assertDictEqual(dictionary, new_dictionary)

    def test_delta(self):
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 15)
        self.env.update(start_date, end_date)
        env_old = deepcopy(environment_0)
        delta = self.env - env_old
        expected_delta = {'nodes': {0: {'structure': {'active': True}}}}
        self.assertDictEqual(delta, expected_delta)


class TestEnvironmentClass_1(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_shape(self):
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 2)
        self.assertListEqual(list(edges), [(0, 2), (1, 2)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 3)
        self.assertListEqual(list(nodes), [0, 1, 2])

    def test_delta(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 15)
        env.update(start_date, end_date)
        env_old = deepcopy(self.env)
        delta = env - env_old
        expected_delta = {
            'nodes': {
                0: {'structure': {'active': True}},
                1: {'structure': {'active': True}}
            },
            'edges': {
                0: {'structure': {'active': True}},
                1: {'structure': {'active': True}}
            }
        }
        self.assertDictEqual(delta, expected_delta)

    def test_dict(self):
        dictionary = self.env.to_dict()
        self.env.print()
        expected_result = {'edges': {0: {'index_end': 2,
                                         'structure': {'active': True,
                                                       'actual_length': None,
                                                       'boundary': {'shape': {'angle': 0.090659887200745,
                                                                              'height': 2.220446049250313e-16,
                                                                              'type': 'rectangle',
                                                                              'width': 22.090722034374522}},
                                                       'difficulty': 1,
                                                       'end_date': None,
                                                       'name': 'Halfway 0',
                                                       'progressive_degradation': {'formula_name': 'formula_01',
                                                                                   'usage_current': 0,
                                                                                   'usage_max': SYMBOLS['inf']},
                                                       'start_date': {'day': 2,
                                                                      'hour': 0,
                                                                      'minute': 0,
                                                                      'month': 1,
                                                                      'second': 0,
                                                                      'year': 2020},
                                                       'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                               'type': 'dirac '
                                                                                               'delta'},
                                                                              'unit_size': None},
                                                       'type': 'road'}},
                                     1: {'index_end': 2,
                                         'structure': {'active': True,
                                                       'actual_length': None,
                                                       'boundary': {'shape': {'angle': 1.5707963267948966,
                                                                              'height': 2,
                                                                              'type': 'rectangle',
                                                                              'width': 20.0}},
                                                       'difficulty': 1.5,
                                                       'end_date': None,
                                                       'name': 'Halfway 1',
                                                       'progressive_degradation': {'formula_name': 'formula_01',
                                                                                   'usage_current': 0,
                                                                                   'usage_max': SYMBOLS['inf']},
                                                       'start_date': {'day': 4,
                                                                      'hour': 0,
                                                                      'minute': 0,
                                                                      'month': 1,
                                                                      'second': 0,
                                                                      'year': 2020},
                                                       'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                               'type': 'dirac '
                                                                                               'delta'},
                                                                              'unit_size': None},
                                                       'type': 'road'}}},
                           'nodes': {0: {'pos': [-2, -2],
                                         'structure': {'active': True,
                                                       'boundary': {'shape': {'radius': 2.220446049250313e-16,
                                                                              'type': 'dot'}},
                                                       'end_date': None,
                                                       'name': "John's Home",
                                                       'progressive_degradation': {'formula_name': 'formula_01',
                                                                                   'usage_current': 0,
                                                                                   'usage_max': SYMBOLS['inf']},
                                                       'start_date': {'day': 2,
                                                                      'hour': 0,
                                                                      'minute': 0,
                                                                      'month': 1,
                                                                      'second': 0,
                                                                      'year': 2020},
                                                       'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                               'type': 'dirac '
                                                                                               'delta'},
                                                                              'unit_size': None},
                                                       'type': 'settlement'}},
                                     1: {'pos': [20, 20],
                                         'structure': {'active': True,
                                                       'boundary': {'shape': {'radius': 5,
                                                                              'type': 'circle'}},
                                                       'end_date': None,
                                                       'name': "Peter's Home",
                                                       'progressive_degradation': {'formula_name': 'formula_01',
                                                                                   'usage_current': 0,
                                                                                   'usage_max': SYMBOLS['inf']},
                                                       'start_date': {'day': 4,
                                                                      'hour': 0,
                                                                      'minute': 0,
                                                                      'month': 1,
                                                                      'second': 0,
                                                                      'year': 2020},
                                                       'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                               'type': 'dirac '
                                                                                               'delta'},
                                                                              'unit_size': None},
                                                       'type': 'settlement'}},
                                     2: {'pos': [20, 0], 'structure': None}},
                           'type': 'environment'}
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        new_env = Environment()
        new_env.from_dict(dictionary)
        new_dictionary = new_env.to_dict()
        self.assertDictEqual(dictionary, new_dictionary)
        # print(dictionary)


if __name__ == "__main__":
    unittest.main()
