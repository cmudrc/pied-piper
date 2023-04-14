import unittest

from piperabm.degradation.sudden.distributions import DiracDelta
from piperabm.unit import DT


class TestDiracDeltaClass(unittest.TestCase):

    def setUp(self):
        self.distribution = DiracDelta(
            main=DT(days=35)
        )

    def test_probability_0(self):
        time_start = DT(days=0)
        time_end = DT(days=70)
        probability = self.distribution.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(probability, 1)

    def test_probability_1(self):
        time_start = DT(days=0)
        time_end = DT(days=30)
        probability = self.distribution.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(probability, 0)

    def test_to_dict(self):
        dictionary = self.distribution.to_dict()
        expected_result = {
            'type': 'dirac delta',
            'main': DT(days=35).total_seconds()
        }
        self.assertDictEqual(dictionary, expected_result)

    def test_from_dict(self):
        dictionary = self.distribution.to_dict()
        new_distribution = DiracDelta()
        new_distribution.from_dict(dictionary)
        self.assertEqual(self.distribution, new_distribution)


if __name__ == "__main__":
    unittest.main()