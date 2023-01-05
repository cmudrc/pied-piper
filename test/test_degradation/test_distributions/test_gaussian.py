import unittest

from piperabm.degradation.distributions import Gaussian
from piperabm import Unit


class TestGaussianClass(unittest.TestCase):
    
    def test_normal_distribution(self):
        time_start = Unit(0, 'day').to_SI()
        time_end = Unit(70, 'day').to_SI()

        g = Gaussian(
            mean=time_end,
            sigma=Unit(10, 'day').to_SI()
        )
        p = g.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be equal")


if __name__ == "__main__":
    unittest.main()