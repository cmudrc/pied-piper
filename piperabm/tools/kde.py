import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt


class KDE:

    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            data = np.array(data)
        self.kernel = self.create_kernel(data)

    def create_kernel(self, data, kernel_type=None):
        kernel = None
        if kernel_type == 'gaussian' or kernel_type is None:
            kernel = stats.gaussian_kde(
                dataset=data,
                bw_method=None,
                weights=None
            )
        return kernel

    def generate(self, n=1, seed=None):
        return self.kernel.resample(
            size=n,
            seed=seed
        ).T


if __name__ == "__main__":
    
    SIZE = 3
    rvs = np.append(
        stats.norm.rvs(loc=2, scale=1, size=(SIZE, 1)),
        stats.norm.rvs(loc=0, scale=3, size=(SIZE, 1)),
        axis=1
    )
    data = rvs.T
    
    kde = KDE(data)
    print(kde.generate(5))
    #sample = kde.generate(10)
