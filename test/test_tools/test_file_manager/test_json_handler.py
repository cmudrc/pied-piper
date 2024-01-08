import unittest
from copy import deepcopy
import os

from piperabm.tools.file_manager import JsonHandler as jsh
from piperabm.model.samples import model_0 as model


class TestJsonHandlerClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model)
        nodes = self.model.all_environment_nodes
        self.node = nodes[0]

    def test_create_delta(self):
        self.maxDiff = None
        model = deepcopy(self.model)
        filename = model.name
        path = os.path.dirname(os.path.realpath(__file__))

        if jsh.exists(path, filename):
            jsh.remove(path, filename)
        
        delta = {}
        data = [delta]
        jsh.save(data, path, filename)
        data = jsh.load(path, filename)
        expected_result = {}
        self.assertDictEqual(data[-1], expected_result)
        
        delta = model.create_delta(data[-1])
        jsh.append(delta, path, filename)
        data = jsh.load(path, filename)
        expected_result = {
            'proximity radius': 0.1,
            'library': {str(self.node): {'pos': [0, 0], 'name': 'Sample Settlement', 'degradation': {'current': 0, 'total': 'inf'}, 'category': 'node', 'type': 'settlement'}},
            'step_size': 3600.0,
            'current_date': {'year': 2000, 'month': 1, 'day': 1, 'hour': 0, 'minute': 0, 'second': 0},
            'exchange_rate': {'food': 1, 'water': 1, 'energy': 1},
            'name': 'Sample Model 00'
        }
        self.assertDictEqual(data[-1], expected_result)
        
        settlement = model.get(self.node)
        settlement.degradation.add(10)

        delta = model.create_delta(data[-1])
        print(delta)



        jsh.remove(path, filename)
        





if __name__ == "__main__":
    unittest.main()