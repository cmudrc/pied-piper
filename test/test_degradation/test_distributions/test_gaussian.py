import unittest

from piperabm.degradation.distributions import Gaussian
from piperabm.unit import DT


class TestGaussianClass(unittest.TestCase):
    
    def test_normal_distribution(self):
        time_start = DT(days=0).total_seconds()
        time_end = DT(days=70).total_seconds()

        g = Gaussian(
            mean=time_end,
            sigma=DT(days=10).total_seconds()
        )
        p = g.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be equal")


if __name__ == "__main__":
    unittest.main()