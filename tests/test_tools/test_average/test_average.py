import unittest
from piperabm.tools.average import average as avg


class TestAverage(unittest.TestCase):

    def test_arithmetic(self):
        values = [1, 2, 3]
        result_unweighted = avg.arithmetic(values=values)
        self.assertAlmostEqual(result_unweighted, 2, places=2)

        weights = [1, 1, 1]
        result_weighted = avg.arithmetic(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 2, places=2)

        weights = [100, 1, 1]
        result_weighted = avg.arithmetic(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 1.0294117647058822, places=2)

    def test_geometric(self):
        values = [1, 2, 3]
        result_unweighted = avg.geometric(values=values)
        self.assertAlmostEqual(result_unweighted, 1.8171205928321397, places=2)

        weights = [1, 1, 1]
        result_weighted = avg.geometric(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 1.8171205928321397, places=2)

        weights = [100, 1, 1]
        result_weighted = avg.geometric(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 1.0177214636113427, places=2)


if __name__ == "__main__":
    unittest.main()