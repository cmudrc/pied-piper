import unittest

from piperabm.tools.stats import gini


class TestGiniLogNormalClass_0(unittest.TestCase):

    def setUp(self):
        self.distribution = gini.lognorm(
            gini_index=0,
            average=1
        )

    def test_generate(self):
        size = 10
        sample = self.distribution.rvs(size)
        self.assertAlmostEqual(sum(sample), size, places=5)


class TestGiniLogNormalClass_1(unittest.TestCase):

    def setUp(self):
        self.data = [100, 300, 500, 700, 900, 300, 500, 700, 500]
        self.gini_index = gini.coefficient(self.data)

        self.distribution = gini.lognorm(
            gini_index=self.gini_index,
            average=1
        )

    def test_generate_batch(self):
        sample = self.distribution.rvs(1000)

        ratio = gini.coefficient(sample) / self.gini_index
        self.assertAlmostEqual(ratio, 1, places=1)

        sample_mean = sum(sample) / len(sample)
        self.assertAlmostEqual(sample_mean, 1, places=1)

    def test_generate_single(self):
        sample = []
        for _ in range(1000):
            single_sample_value = self.distribution.rvs()
            sample.append(single_sample_value)

        ratio = gini.coefficient(sample) / self.gini_index
        self.assertAlmostEqual(ratio, 1, places=1)

        sample_mean = sum(sample) / len(sample)
        self.assertAlmostEqual(sample_mean, 1, places=1)


if __name__ == '__main__':
    unittest.main()