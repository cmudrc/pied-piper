from scipy.stats import norm

from piperabm.degradation.sudden.distributions.distribution import Distribution


class Gaussian(Distribution):
    """
    Gaussian distribution.
    """

    def __init__(self, mean=0, sigma=0):
        super().__init__()
        self.type = 'gaussian'
        self.mean = self.refine_input(mean)
        self.sigma = self.refine_input(sigma)

    def normalize(self, time) -> float:
        return (time - self.mean) / self.sigma

    def CDF(self, time) -> float:
        time = self.refine_input(time)
        point = self.normalize(time)
        return norm.cdf(point)

    '''
    def show(self):
        import numpy as np
        import matplotlib.pyplot as plt
        x_array_normalized = np.arange(-5, 5, 0.1)
        x_array = (x_array_normalized * self.sigma.days) + self.mean.days
        y_pdf = norm.pdf(x_array_normalized)
        plt.plot(x_array, y_pdf)
        plt.show()
    '''

    def to_dict(self) -> dict:
        dictionary = {
            'type': self.type,
            'mean': self.mean,
            'sigma': self.sigma,
        }
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        self.mean = dictionary['mean']
        self.sigma = dictionary['sigma']


if __name__ == "__main__":
    time_start=0
    time_end=90

    distribution = Gaussian(
        mean=100,
        sigma=20
    )
    print(
        distribution.probability(
            time_start=time_start,
            time_end=time_end
        )
    )