import unittest
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

from piperabm.tools import KDE


class TestKDEClass(unittest.TestCase):

    def test_1D_data(self):
        SIZE = 100
        mean = 2
        max = mean+1
        min = mean-1
        data = np.arange(min, max, (max-min)/SIZE)
        #print(data[:10])
        #plt.hist(data)
        data = data.T
        kde = KDE(data)
        sample = kde.generate(n=SIZE, seed=100)
        sample = kde.generate(n=SIZE, seed=100)
        #print(sample[:10])
        #plt.hist(sample)
        plt.show()
        self.assertEqual(len(sample), SIZE)
        sample_mean = (sum(sample.T[0]) / SIZE)
        result = (sample_mean - mean) / mean
        self.assertAlmostEqual(result, 0, places=1)

    def test_2D_data(self):
        SIZE = 100
        x_mean = 2
        y_mean = 0
        data = np.append(
            stats.norm.rvs(loc=x_mean, scale=1, size=(SIZE, 1)),
            stats.norm.rvs(loc=y_mean, scale=3, size=(SIZE, 1)),
            axis=1
        )
        data = data.T
        #print(data[:10])
        kde = KDE(data)
        sample = kde.generate(n=SIZE, seed=100)
        #print(sample[:10])
        self.assertEqual(len(sample), SIZE)


if __name__ == "__main__":
    unittest.main()