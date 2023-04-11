import unittest

from piperabm.degradation.sudden.distributions import Eternal
from piperabm.unit import DT


class TestEternalClass(unittest.TestCase):

    def setUp(self):
        dist = Eternal()
        self.dist = dist

    def test_eternal_distribution(self):
        time_start = DT(days=0).total_seconds()
        time_end = DT(days=70).total_seconds()
        p = self.dist.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 0)


if __name__ == "__main__":
    unittest.main()