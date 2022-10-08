import unittest


#################################### entity.py ####################################

from entity import Entity


class TestEntityClass(unittest.TestCase):
    def test_entity_distance(self):
        e_1 = Entity(pos=[0, 0])
        e_2 = Entity(pos=[0, 1])
        d = e_1.distance(e_2)
        self.assertAlmostEqual(d, 1, places=5, msg="Distance")


#################################### degradation.py ####################################

from datetime import date

from degradation import DegradationProperty
from utils import Unit


class TestDegradationPropertyClass(unittest.TestCase):
    def test_gaussian_degradation(self):
        d = DegradationProperty(
            initiation_date=date(2000, 1, 1),
            distribution={
                'type': 'gaussian',
                'sigma': Unit(20,'day'),
                'mean': Unit(100,'day'),
            },
            seed=202
        )
        p = d.probability_of_working(
            start_date=Unit(0, 'day')+date(2000, 1, 1),
            end_date=Unit(100, 'day')+date(2000, 1, 1)
        )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be 0.5")
    
    def test_dirac_degradation_0(self):
        d = DegradationProperty(
            initiation_date=date(2000, 1, 1),
            distribution={
                'type': 'dirac delta',
                'main': Unit(70,'day'),
            },
            seed=202
        )
        p = d.probability_of_working(
            start_date=Unit(0, 'day')+date(2000, 1, 1),
            end_date=Unit(100, 'day')+date(2000, 1, 1)
        )
        self.assertEqual(p, 0, msg="dirac_degradation_0")

    def test_dirac_degradation_1(self):
        d = DegradationProperty(
            initiation_date=date(2000, 1, 1),
            distribution={
                'type': 'dirac delta',
                'main': Unit(70,'day'),
            },
            seed=202
        )
        p = d.probability_of_working(
            start_date=Unit(0, 'day')+date(2000, 1, 1),
            end_date=Unit(50, 'day')+date(2000, 1, 1)
        )
        self.assertEqual(p, 1, msg="dirac_degradation_1")


if __name__ == '__main__':
    unittest.main()