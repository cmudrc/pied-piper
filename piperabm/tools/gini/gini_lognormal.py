"""
Source:
https://stats.stackexchange.com/questions/286141/lognormal-parameters-knowing-gdp-per-capita-gini-coefficient-and-quintile-share
"""
import numpy as np
from scipy.special import erfinv
from scipy.stats import lognorm

from piperabm.tools.symbols import SYMBOLS


class GiniLogNormal:
    """
    Create a lognormal distribution by gini index and average
    """

    def __init__(self, gini_index: float = 0, average: float = 1):
        self.average = average
        if gini_index == 0:
            gini_index = SYMBOLS['eps']
        if gini_index < 0 or gini_index > 1:
            raise ValueError
        self.gini = gini_index

    @property
    def sigma(self):
        return 2 * erfinv(self.gini)
    
    @property
    def mu(self):
        return np.log(self.average) - (self.sigma ** 2) / 2
    
    @property
    def scale(self):
        return np.exp(self.mu)
    
    def rvs(self, sample_size: int = 1):
        """
        Generate random sample
        """
        result = lognorm(s=self.sigma, scale=self.scale).rvs(sample_size)
        result = [float(num) for num in result]  # Convert np.float64 to float explicitly
        if sample_size == 1:
            result = result[0]
        return result


if __name__ == "__main__":
    distribution = GiniLogNormal(
        gini_index=0.5,
        average=1
    )
    sample = distribution.rvs(10)
    print(sample)
