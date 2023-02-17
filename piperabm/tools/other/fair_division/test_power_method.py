import unittest
from copy import deepcopy
import numpy as np

from piperabm.tools import PowerMethod


class TestExistanceFunction(unittest.TestCase):

    matrix = [
        [0.8, 0.6],
        [0.2, 0.4]
        ]
    threashold = 0.05
    pm = PowerMethod(matrix, threashold)

    def test_default_weight(self):
        result = list(self.pm.default_weight)
        expected_result = [0.5, 0.5]
        self.assertListEqual(result, expected_result)

    def test_average_distance(self):
        matrix = np.array(deepcopy(self.matrix))
        result = self.pm.average_distance(matrix)
        expected_result = [0.1, 0.1]
        self.assertAlmostEqual(result[0], expected_result[0])
        self.assertAlmostEqual(result[1], expected_result[1])

    def test_overall_distance(self):
        matrix = np.array(deepcopy(self.matrix))
        average = self.pm.average_distance(matrix)
        result = self.pm.overall_distance(average)
        self.assertAlmostEqual(result, 0.1)

    def test_is_converged(self):
        pm = deepcopy(self.pm)
        matrix = pm.last_matrix()
        result = self.pm.is_converged(matrix)
        self.assertFalse(result)

    def test_run_step(self):
        pm = deepcopy(self.pm)
        pm.run_step()
        expected_result = [
            [0.76, 0.72],
            [0.24, 0.28]    
        ]
        #print(pm.result_dict[1]['matrix'])
        expected_result = [[0.7, 0.3]]
        #print(pm.result_dict[1]['weight'])

    def test_run(self):
        pm = deepcopy(self.pm)
        pm.run()
        #print(pm.last_matrix())



if __name__ == "__main__":
    unittest.main()