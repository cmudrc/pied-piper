import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.model.samples import model_0, model_3


class TestModelClass_0(unittest.TestCase):

    def setUp(self):
        self.model = deepcopy(model_0)
        nodes = self.model.all_environment_nodes
        self.node = nodes[0]

    def test_serialization(self):
        dictionary = self.model.serialize()
        model_new = Model()
        model_new.deserialize(dictionary)
        dictionary_new = model_new.serialize()
        self.assertDictEqual(dictionary, dictionary_new)

    def test_apply_delta(self):
        model = deepcopy(self.model)

        settlement = model.get(self.node)
        self.assertEqual(settlement.degradation.current, 0)

        delta = {'library': {str(self.node): {'degradation': {'current': 10}}}}
        model.apply_delta(delta)

        settlement = model.get(self.node)
        self.assertEqual(settlement.degradation.current, 10)

    def test_create_delta(self):
        self.maxDiff = None
        model = deepcopy(self.model)
        deltas = []

        delta = {}
        deltas.append(delta)

        delta = model.create_delta(deltas[-1])
        expected_result = {
            'proximity radius': 0.1,
            'library': {str(self.node): {'pos': [0, 0], 'name': 'Sample Settlement', 'degradation': {'current': 0, 'total': 'inf'}, 'section': 'infrastructure', 'category': 'node', 'type': 'settlement'}},
            'step_size': 3600.0,
            'current_date': {'year': 2000, 'month': 1, 'day': 1, 'hour': 0, 'minute': 0, 'second': 0},
            'exchange_rate': {'food': 1, 'water': 1, 'energy': 1},
            'name': 'Sample Model 00'
        }
        self.assertDictEqual(delta, expected_result)
        deltas.append(delta)

        settlement = model.get(self.node)
        settlement.degradation.add(10)

        delta = model.create_delta(deltas[-1])
        expected_result = {
            'library': {str(self.node): {'degradation': {'current': 10}}}
        }
        self.assertDictEqual(delta, expected_result)
        deltas.append(delta)


'''
class TestModelClass_3(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model_3)

    def test_find_nearest_node(self):
        items = self.model.all_environment_nodes
        pos = [0, 1]
        index, distance = self.model.find_nearest_node(pos, items)
        item = self.model.get(index)
        self.assertListEqual(item.pos, [0, 0])
        self.assertEqual(distance, 1)

    def test_run(self):
        self.model.run(100)
        self.assertEqual(len(self.model.all_alive_agents), 2)
        self.model.run(900)
        self.assertEqual(len(self.model.all_alive_agents), 0)
'''


if __name__ == '__main__':
    unittest.main()