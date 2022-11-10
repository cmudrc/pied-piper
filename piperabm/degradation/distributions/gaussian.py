from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


class Gaussian:
    """
    Gaussian distribution.
    """

    def __init__(self, mean, sigma):
        self.mean = mean
        self.sigma = sigma

    def probability(self, time_start, time_end):
        def normalize(value, mean, sigma):
            return (value - mean) / sigma
        point_start = normalize(time_start, self.mean, self.sigma)
        point_end = normalize(time_end, self.mean, self.sigma)
        probability = norm.cdf(point_end) - norm.cdf(point_start)
        return probability

    def show(self):
        x_array_normalized = np.arange(-5, 5, 0.1)
        x_array = (x_array_normalized * self.sigma.days) + self.mean.days
        y_pdf = norm.pdf(x_array_normalized)
        plt.plot(x_array, y_pdf)
        plt.show()

    def to_dict(self) -> dict:
        dictionary = {
            'type': 'gaussian',
            'mean': self.mean,
            'sigma': self.sigma,
        }
        return dictionary
    
    def from_dict(self, dictionary: dict):
        d = dictionary
        self.mean = d['mean']
        self.sigma = d['sigma']


if __name__ == "__main__":
    time_start=0
    time_end=90

    g = Gaussian(
        mean=100,
        sigma=10
    )
    print(
        g.probability(
            time_start=time_start,
            time_end=time_end
        )
    )