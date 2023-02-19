# https://stats.stackexchange.com/questions/286141/lognormal-parameters-knowing-gdp-per-capita-gini-coefficient-and-quintile-share

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm
from scipy.special import erfinv


def gini_coefficient(x):
    """
    Compute Gini coefficient of array of values
    """
    x = np.array(x)
    diffsum = 0
    for i, xi in enumerate(x[:-1], 1):
        diffsum += np.sum(np.abs(xi - x[i:]))
    return diffsum / (len(x)**2 * np.mean(x))


class GiniGenerator:
    
    def __init__(self, gini_index: float, gdp_per_capita: float):
        if gini_index >= 0 and gini_index <= 1:
            self.gini = gini_index
        else:
            raise ValueError
        if gdp_per_capita > 0:
            self.gdp_per_capita = gdp_per_capita
        else:
            raise ValueError
        self.sigma = self.sigma_calculate(gini=gini_index)
        self.mu = self.mu_calculate(mean=self.gdp_per_capita, sigma=self.sigma)

    def sigma_calculate(self, gini):
        return 2 * erfinv(gini)
    
    def mu_calculate(self, mean, sigma):
        val_1 = np.log(mean)
        val_2 = (sigma ** 2) / 2
        return val_1 - val_2

    def generate(self, n: int, threashold=0.5):
        """
        Generate a random array of size n which gini index is equal to *gini*
        """
        def rvs():
            return lognorm.rvs(
                loc=self.mu,
                scale=np.exp(self.mu),
                s=self.sigma,
                size=n
            )

        result = rvs()
        while np.abs(gini_coefficient(result) - self.gini) > threashold:
            result = rvs()
        return result

    def check_gini(self, x):
        return gini_coefficient(x)

    def __str__(self):
        txt = ''
        txt += 'mean: ' + str(self.mu) + '\n'
        txt += 'sigma: ' + str(self.sigma)
        return txt

    def show(self, sample):
        plt.hist(sample)
        plt.show()


if __name__ == "__main__":
    income = [100, 300, 500, 700, 900, 300, 500, 700, 500]
    gini = gini_coefficient(income)
    gdp_per_capita = sum(income) / len(income)
    g = GiniGen(
        gini_index=gini,
        gdp_per_capita=gdp_per_capita
    )
    sample = g.generate(1000)
    g.show(sample)