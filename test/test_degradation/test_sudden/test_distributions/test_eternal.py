import unittest

from piperabm.degradation.sudden.distributions import Eternal
from piperabm.unit import DT


class TestEternalClass(unittest.TestCase):

    def setUp(self):
        dist = Eternal()
        self.distribution = dist

    def test_eternal_distribution(self):
        time_start = DT(days=0)
        time_end = DT(days=70)
        p = self.distribution.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 0)

    def test_dict(self):
        dictionary = self.distribution.to_dict()
        expected_result = {
            'type': 'eternal',
        }
        self.assertDictEqual(dictionary, expected_result)
        new_distribution = Eternal()
        new_distribution.from_dict(dictionary)
        self.assertEqual(self.distribution, new_distribution)


if __name__ == "__main__":
    unittest.main()