import unittest

from piperabm.unit import Date, Unit
from piperabm.degradation import DegradationProperty


class TestDegradationPropertyClass(unittest.TestCase):
    def test_gaussian_degradation(self):
        d = DegradationProperty(
            initiation_date=Date(2000, 1, 1),
            distribution={
                'type': 'gaussian',
                'sigma': Unit(20, 'day').to_SI(),
                'mean': Unit(100, 'day').to_SI(),
            },
            seed=202
        )
        p = d.probability_of_working(
            start_date=Unit(0, 'day')+Date(2000, 1, 1),
            end_date=Unit(100, 'day')+Date(2000, 1, 1)
        )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be 0.5")

    def test_dirac_degradation_0(self):
        d = DegradationProperty(
            initiation_date=Date(2000, 1, 1),
            distribution={
                'type': 'dirac delta',
                'main': Unit(70, 'day').to_SI(),
            },
            seed=202
        )
        p = d.probability_of_working(
            start_date=Unit(0, 'day')+Date(2000, 1, 1),
            end_date=Unit(100, 'day')+Date(2000, 1, 1)
        )
        self.assertEqual(p, 0, msg="dirac_degradation_0")

    def test_dirac_degradation_1(self):
        d = DegradationProperty(
            initiation_date=Date(2000, 1, 1),
            distribution={
                'type': 'dirac delta',
                'main': Unit(70, 'day').to_SI(),
            },
            seed=202
        )
        p = d.probability_of_working(
            start_date=Unit(0, 'day')+Date(2000, 1, 1),
            end_date=Unit(50, 'day')+Date(2000, 1, 1)
        )
        self.assertEqual(p, 1, msg="dirac_degradation_1")


if __name__ == "__main__":
    unittest.main()