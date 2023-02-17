import unittest

from piperabm.tools import GiniGen, gini_coefficient


class TestGiniGen(unittest.TestCase):

    income = [100, 300, 500, 700, 900, 300, 500, 700, 500]
    gini = gini_coefficient(income)
    gdp_per_capita = sum(income) / len(income)
    gg = GiniGen(
        gini_index=gini,
        gdp_per_capita=gdp_per_capita
    )

    def test_generate(self):
        gg = self.gg
        sample = gg.generate(1000, threashold=0.01)
        result = gini_coefficient(sample)
        self.assertAlmostEqual(result, gg.gini, places=2)


if __name__ == "__main__":
    unittest.main()