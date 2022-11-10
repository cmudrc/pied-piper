import unittest

from piperabm.degradation.distributions import Eternal
from piperabm import Unit


class TestEternalClass(unittest.TestCase):

    d = Eternal()

    def test_eternal_distribution(self):
        time_start = Unit(0, 'day').to_SI()
        time_end = Unit(70, 'day').to_SI()
        p = self.d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 0)


if __name__ == "__main__":
    unittest.main()