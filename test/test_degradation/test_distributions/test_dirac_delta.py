import unittest

from piperabm.degradation.distributions import DiracDelta
from piperabm import Unit


class TestDiracDeltaClass(unittest.TestCase):

    d = DiracDelta(
        main=Unit(35, 'day').to_SI()
    )

    def test_dirac_distribution_0(self):
        time_start = Unit(0, 'day').to_SI()
        time_end = Unit(70, 'day').to_SI()
        p = self.d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 1, msg="Should be equal")

    def test_dirac_distribution_1(self):
        time_start = Unit(0, 'day').to_SI()
        time_end = Unit(30, 'day').to_SI()
        p = self.d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 0, msg="Should be equal")


if __name__ == "__main__":
    unittest.main()