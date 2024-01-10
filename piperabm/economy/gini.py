"""
Source:
https://stats.stackexchange.com/questions/286141/lognormal-parameters-knowing-gdp-per-capita-gini-coefficient-and-quintile-share
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm
from scipy.special import erfinv


def gini_coefficient(x):
    """
    Compute Gini coefficient of array of values
    """
    if isinstance(x, list):
        x = np.array(x)
    diffsum = 0
    for i, xi in enumerate(x[:-1], 1):
        diffsum += np.sum(np.abs(xi - x[i:]))
    return diffsum / (len(x)**2 * np.mean(x))


class GiniGenerator:
    
    def __init__(self, gini_index: float = None, average: float = None):
        self.gini_index = 0.5  # default
        self.average = 100  # default
        if gini_index is not None and \
            average is not None:
            self.set_gini_index(gini_index)
            self.set_average(average)

    def set_gini_index(self, gini_index: float):
        if gini_index >= 0 and gini_index <= 1:
            self.gini_index = gini_index
        else:
            raise ValueError
        self.process()
        
    def set_average(self, average: float):
        if average > 0:
            self.average = average
        else:
            raise ValueError
        self.process()

    def process(self):
        self.sigma = self.calculate_sigma(gini=self.gini_index)
        self.mu = self.calculate_mu(mean=self.average, sigma=self.sigma)

    def calculate_sigma(self, gini):
        return 2 * erfinv(gini)
    
    def calculate_mu(self, mean, sigma):
        val_1 = np.log(mean)
        val_2 = (sigma ** 2) / 2
        return val_1 - val_2

    def generate(self, n: int=1, threashold=None):
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
        if threashold is not None:  # to ensure a sample having gini index within threashold
            while np.abs(gini_coefficient(result) - self.gini_index) > threashold:
                result = rvs()
        if n == 1:  # when asked for a single value, a single value is returned instead of a list
            result = result[0]
            if result < 0:
                result = 0
        else:
            for value in result:
                if value < 0:
                    value = 0
        return result

    def __str__(self):
        txt = ''
        txt += 'mean: ' + str(self.mu) + '\n'
        txt += 'sigma: ' + str(self.sigma)
        return txt

    def show(sel, sample):
        plt.hist(sample)
        plt.show()


if __name__ == "__main__":

    income = [100, 300, 500, 700, 900, 300, 500, 700, 500]

    gini = gini_coefficient(income)
    gini = 0.5
    average = sum(income) / len(income)
    g = GiniGenerator(
        gini_index=gini,
        average=average
    )
    sample = g.generate(1000)
    #filtered = [s for s in sample if s<0]
    #print(len(filtered))

    #g.show(income)
    #g.show(sample)
    print(">>> input: ")
    print(" " + "gini: " + str(gini) + ", " + "average: " + str(average))
    print(">>> sample: ")
    print(" " + "gini: " + str(gini_coefficient(sample)) + ", " + "average: " + str(sum(sample) / len(sample)))