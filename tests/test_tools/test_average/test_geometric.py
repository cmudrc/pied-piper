import unittest
from piperabm.tools.average.geometric import geometric


class TestGeomteric(unittest.TestCase):

    def test_geometric(self):
        values = [1, 2, 3]
        result_unweighted = geometric(values=values)
        self.assertAlmostEqual(result_unweighted, 1.8171205928321397, places=2)

        weights = [1, 1, 1]
        result_weighted = geometric(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 1.8171205928321397, places=2)

        weights = [100, 1, 1]
        result_weighted = geometric(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 1.0177214636113427, places=2)


if __name__ == "__main__":
    unittest.main()