import unittest

from piperabm.degradation.sudden.distributions import Gaussian
from piperabm.unit import DT


class TestGaussianClass(unittest.TestCase):
    
    def setUp(self):
        self.distribution = Gaussian(
            mean=DT(days=70),
            sigma=DT(days=10)
        )

    def test_normal_distribution(self):
        time_start = DT(days=0)
        time_end = DT(days=70)
        p = self.distribution.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be equal")

    def test_to_dict(self):
        dictionary = self.distribution.to_dict()
        expected_result = {
            'type': 'gaussian',
            'mean': DT(days=70).total_seconds(),
            'sigma': DT(days=10).total_seconds()
        }
        self.assertDictEqual(dictionary, expected_result)

    def test_from_dict(self):
        dictionary = self.distribution.to_dict()
        new_distribution = Gaussian()
        new_distribution.from_dict(dictionary)
        self.assertEqual(self.distribution, new_distribution)


if __name__ == "__main__":
    unittest.main()