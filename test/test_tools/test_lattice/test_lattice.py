import unittest
import numpy as np
from copy import deepcopy

from piperabm.tools.lattice import Lattice


class TestLatticeClass(unittest.TestCase):

    def setUp(self) -> None:
        self.lattice = Lattice(2, 3)

    def test_shape(self):
        shape = self.lattice.shape
        expected_result = [
            [2, 4, 2], [2, 4, 2]
        ]
        self.assertListEqual(shape, expected_result)

    def test_distribution(self):
        distribution = self.lattice.distribution
        expected_result = {
            0: 0.0,
            1: 0.0,
            2: 0.6666666666666666,
            3: 0.0,
            4: 0.3333333333333333,
            5: 0.0
        }
        self.assertDictEqual(distribution, expected_result)

    def test_shape_matrix(self):
        nodes = self.lattice.nodes
        node = nodes[0]
        shape_matrix = self.lattice.shape_matrix(node)
        expected_result = [
            [0, 0, 0,],
            [0, 1, 1,],
            [0, 1, 0,],
        ]
        expected_result = np.array(expected_result)
        comparison = shape_matrix == expected_result
        self.assertTrue(comparison.all())

    def test_optimize(self):
        lattice = deepcopy(self.lattice)
        lattice.remove_node((0, 1))
        target = lattice.distribution
        new_lattice = Lattice(4, 6, target)
        new_lattice.optimize()
        error = new_lattice.MSE()
        self.assertLess(error, 0.05)


if __name__ == "__main__":
    unittest.main()