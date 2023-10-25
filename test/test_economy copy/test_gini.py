import unittest

from piperabm.economy import GiniGenerator, gini_coefficient


class TestGiniGen(unittest.TestCase):

    def setUp(self):
        incomes = [100, 300, 500, 700, 900, 300, 500, 700, 500]
        gini = gini_coefficient(incomes)
        gdp_per_capita = sum(incomes) / len(incomes)

        self.gini_generator = GiniGenerator(
            gini_index=gini,
            average=gdp_per_capita
        )

    def test_generate(self):
        gg = self.gini_generator
        sample = gg.generate(1000, threashold=0.01)
        sample_gini = gini_coefficient(sample)
        result = sample_gini / gg.gini
        self.assertAlmostEqual(result, 1, places=0)
        sample_mean = sum(sample) / len(sample)
        result = sample_mean / gg.average
        result = abs(1 - result)
        self.assertAlmostEqual(result, 0, places=1)

    def test_generate_single(self):
        gg = self.gini_generator
        sample = []
        for _ in range(1000):
            single_sample = gg.generate(1)
            sample.append(single_sample)
        #print(sample[:50])
        sample_gini = gini_coefficient(sample)
        result = sample_gini / gg.gini
        self.assertAlmostEqual(result, 1, places=0)
        sample_mean = sum(sample) / len(sample)
        result = sample_mean / gg.average
        result = abs(1 - result)
        self.assertAlmostEqual(result, 0, places=1)


if __name__ == "__main__":
    unittest.main()