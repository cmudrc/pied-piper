import unittest
from piperabm.tools.average.arithmetic import arithmetic


class TestArithmetic(unittest.TestCase):

    def test_arithmetic(self):
        values = [1, 2, 3]
        result_unweighted = arithmetic(values=values)
        self.assertAlmostEqual(result_unweighted, 2, places=2)

        weights = [1, 1, 1]
        result_weighted = arithmetic(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 2, places=2)

        weights = [100, 1, 1]
        result_weighted = arithmetic(values=values, weights=weights)
        self.assertAlmostEqual(result_weighted, 1.0294117647058822, places=2)


if __name__ == "__main__":
    unittest.main()