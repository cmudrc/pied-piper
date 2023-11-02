import unittest
import numpy as np
from copy import deepcopy

from piperabm.tools.lattice import Lattice
from piperabm.tools.lattice.samples import lattice_0


class TestLatticeClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.lattice = Lattice(2, 3)

    def test_shape(self):
        shape = self.lattice.shape
        expected_result = [
            [2, 4, 2],
            [2, 4, 2],
        ]
        self.assertListEqual(shape, expected_result)

    def test_total_length(self):
        self.assertEqual(self.lattice.total_length, 7)
        self.assertEqual(self.lattice.max_length, 7)
        self.assertEqual(self.lattice.length_ratio, 1)

    def test_not_edges(self):
        not_edges = self.lattice.not_edges
        self.assertEqual(len(not_edges), 0)

    def test_components(self):
        self.assertEqual(self.lattice.components, 1)
        self.assertTrue(self.lattice.is_connected)

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


class TestLatticeClass_1(unittest.TestCase):

    def setUp(self) -> None:
        self.lattice = deepcopy(lattice_0)

    def test_shape(self):
        shape = self.lattice.shape
        expected_result = [
            [0, 0, 2, 2],
            [0, 1, 5, 2],
            [1, 3, 4, 1],
        ]
        self.assertListEqual(shape, expected_result)

    def test_total_length(self):
        self.assertEqual(self.lattice.total_length, 9)
        self.assertEqual(self.lattice.max_length, 17)
        self.assertAlmostEqual(self.lattice.length_ratio, 9/17, places=2)

    def test_not_edges(self):
        not_edges = self.lattice.not_edges
        self.assertEqual(len(not_edges), 8)

    def test_components(self):
        self.assertEqual(self.lattice.components, 1)
        self.assertTrue(self.lattice.is_connected)

    def test_distribution(self):
        distribution = self.lattice.distribution
        expected_result = {
            0: 0.25,
            1: 0.25,
            2: 0.25,
            3: 0.25/3,
            4: 0.25/3,
            5: 0.25/3,
        }
        self.assertDictEqual(distribution, expected_result)

    def test_generate(self):
        threashold = 0.1
        new_lattice = self.lattice.generate(4, 5, threashold)
        error = new_lattice.RMSE(target=self.lattice.distribution)
        self.assertLess(error, threashold)


if __name__ == "__main__":
    unittest.main()