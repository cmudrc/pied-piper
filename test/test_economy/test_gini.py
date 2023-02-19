import unittest

from piperabm.economy import GiniGenerator, gini_coefficient


class TestGiniGen(unittest.TestCase):

    income = [100, 300, 500, 700, 900, 300, 500, 700, 500]
    gini = gini_coefficient(income)
    gdp_per_capita = sum(income) / len(income)
    gg = GiniGenerator(
        gini_index=gini,
        gdp_per_capita=gdp_per_capita
    )

    def test_generate(self):
        gg = self.gg
        sample = gg.generate(1000, threashold=0.01)
        sample_gini = gini_coefficient(sample)
        result = sample_gini / gg.gini
        self.assertAlmostEqual(result, 1, places=1)
        sample_mean = sum(sample) / len(sample)
        result = sample_mean / gg.gdp_per_capita
        self.assertAlmostEqual(result, 1, places=1)


if __name__ == "__main__":
    unittest.main()