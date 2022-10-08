from scipy.stats import norm
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt

from unit_manager import Unit


class Gaussian():
    def __init__(self, mean, sigma):
        self.mean = timedelta(days=mean.to('day').val)
        self.sigma = timedelta(days=sigma.to('day').val)

    def probability(self, time_start, time_end):
        time_start = timedelta(days=time_start.to('day').val)
        time_end = timedelta(days=time_end.to('day').val)
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


class DiracDelta():
    def __init__(self, main):
        self.main = timedelta(days=main.to('day').val)

    def probability(self, time_start, time_end):
        point_start = timedelta(days=time_start.to('day').val)
        point_end = timedelta(days=time_end.to('day').val)
        probability = self.CDF(point_end) - self.CDF(point_start)
        return probability

    def CDF(self, point):
        result = 0
        if self.main <= point:
            result = 1
        return result

    def show(self):
        pass


class Exponential():
    def __init__(self, coeff, degree):
        pass


if __name__ == "__main__":
    time_start=Unit(0, 'day')
    time_end=Unit(90, 'day')

    g = Gaussian(
        mean=Unit(100, 'day'),
        sigma=Unit(10, 'day')
    )
    print(
        g.probability(
            time_start=time_start,
            time_end=time_end
        )
    )
    
    d = DiracDelta(
        main=Unit(100, 'day')
    )
    print(
        d.probability(
            time_start=time_start,
            time_end=time_end
        )
    )
