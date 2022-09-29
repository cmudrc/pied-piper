from scipy.stats import norm
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt


class Gaussian():
    def __init__(self, mean=timedelta(days=0), sigma=timedelta(days=1)):
        self.mean = mean
        self.sigma = sigma

    def probability(self, time_start, time_end):
        point_start = (time_start - self.mean) / self.sigma
        point_end = (time_end - self.mean) / self.sigma
        probability = norm.cdf(point_end) - norm.cdf(point_start)
        return probability

    def show(self):
        x_array_normalized = np.arange(-5, 5, 0.1)
        x_array = (x_array_normalized * self.sigma.days) + self.mean.days
        y_pdf = norm.pdf(x_array_normalized)
        plt.plot(x_array, y_pdf)
        plt.show()


class Exponential():
    def __init__(self, coeff, degree):
        pass


if __name__ == "__main__":
    g = Gaussian(
        mean=timedelta(days=70),
        sigma=timedelta(days=10)
    )
    print(
        g.probability(
            time_start=timedelta(days=0),
            time_end=timedelta(days=70)
        )
    )
    g.show()
