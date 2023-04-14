import unittest

from piperabm.degradation.sudden.distributions import Gaussian
from piperabm.unit import DT


class TestGaussianClass(unittest.TestCase):
    
    def setUp(self):
        self.dist = Gaussian(
            mean=DT(days=70),
            sigma=DT(days=10)
        )

    def test_normal_distribution(self):
        time_start = DT(days=0)
        time_end = DT(days=70)
        p = self.dist.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be equal")


if __name__ == "__main__":
    unittest.main()