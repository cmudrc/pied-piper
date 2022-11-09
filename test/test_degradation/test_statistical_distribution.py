import unittest

from piperabm.degradation.distributions import Gaussian, DiracDelta
from piperabm.unit import Unit


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


class TestDiracDeltaClass(unittest.TestCase):
    def test_dirac_distribution_0(self):
        time_start = Unit(0, 'day').to_SI()
        time_end = Unit(70, 'day').to_SI()

        d = DiracDelta(
            main=Unit(35, 'day').to_SI()
        )
        p = d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 1, msg="Should be equal")

    def test_dirac_distribution_1(self):
        time_start = Unit(0, 'day').to_SI()
        time_end = Unit(30, 'day').to_SI()

        d = DiracDelta(
            main=Unit(35, 'day').to_SI()
        )
        p = d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 0, msg="Should be equal")


if __name__ == "__main__":
    unittest.main()