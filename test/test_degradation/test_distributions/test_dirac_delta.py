import unittest

from piperabm.degradation.distributions import DiracDelta
from piperabm.unit import DT


class TestDiracDeltaClass(unittest.TestCase):

    d = DiracDelta(
        main=DT(days=35).total_seconds()
    )

    def test_dirac_distribution_0(self):
        time_start = DT(days=0).total_seconds()
        time_end = DT(days=70).total_seconds()
        p = self.d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 1, msg="Should be equal")

    def test_dirac_distribution_1(self):
        time_start = DT(days=0).total_seconds()
        time_end = DT(days=30).total_seconds()
        p = self.d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 0, msg="Should be equal")


if __name__ == "__main__":
    unittest.main()