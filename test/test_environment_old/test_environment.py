import unittest
from copy import deepcopy

from piperabm.environment_old import Environment
from piperabm.environment_old.samples import environment_0, environment_1
from piperabm.agent.config import Walk
from piperabm.unit import Date

try:
    from .test_environment_results import environment_0_serialized, environment_1_serialized
except:
    from test_environment_results import environment_0_serialized, environment_1_serialized


class TestEnvironmentClass_0(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_0)

    def test_dict(self):
        dictionary = self.env.to_dict()
        expected_result = environment_0_serialized
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
        self.transportation = Walk()

    def test_shape(self):
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 2)
        self.assertListEqual(list(edges), [(0, 2), (1, 2)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 3)
        self.assertListEqual(list(nodes), [0, 1, 2])

    def test_duration(self):
        object = self.env.get_edge_object(0, 2)
        duration = object.duration(self.transportation)
        self.assertAlmostEqual(duration.total_seconds(), 15.90, places=1)

    def test_fuel(self):
        object = self.env.get_edge_object(0, 2)
        fuel = object.fuel(self.transportation)
        expected_result = {
            'food': 0.0003681787037037037,
            'water': 0.00018408935185185185,
            'energy': 0.0
        }
        self.assertDictEqual(expected_result, fuel.to_dict())

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
        expected_result = environment_1_serialized
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        new_env = Environment()
        new_env.from_dict(dictionary)
        new_dictionary = new_env.to_dict()
        self.assertDictEqual(dictionary, new_dictionary)


if __name__ == "__main__":
    unittest.main()
