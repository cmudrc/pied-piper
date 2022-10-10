from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


class Gaussian():
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


class DiracDelta():
    """
    Dirac Delta distribution.
    """
    
    def __init__(self, main):
        self.main = main

    def probability(self, time_start, time_end):
        return self.CDF(time_end) - self.CDF(time_start)

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
    from unit import Unit


    time_start=Unit(0, 'day').to('second').val
    time_end=Unit(90, 'day').to('second').val

    g = Gaussian(
        mean=Unit(100, 'day').to('second').val,
        sigma=Unit(10, 'day').to('second').val
    )
    print(
        g.probability(
            time_start=time_start,
            time_end=time_end
        )
    )
    
    d = DiracDelta(
        main=Unit(100, 'day').to('second').val
    )
    print(
        d.probability(
            time_start=time_start,
            time_end=time_end
        )
    )
