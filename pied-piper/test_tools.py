from tools import Gaussian, DiracDelta
from tools import Storage, Deficiency
from tools import Use, Produce
from tools import Entity

import unittest


#################################### boundery.py ####################################

from tools import Circular


class Other():
    """ Only a helper class """

    def __init__(self, pos):
        self.pos = pos


class TestCircularClass(unittest.TestCase):
    def test_circular_boundery_in(self):
        other = Other(pos=[1, 1])
        boundery = Circular(center=[0, 0], radius=2)
        self.assertTrue(boundery.is_in(other), msg="Should be equal")

    def test_circular_boundery_out(self):
        other = Other(pos=[1, 2])
        boundery = Circular(center=[0, 0], radius=2)
        self.assertFalse(boundery.is_in(other), msg="Should be equal")


#################################### degradation.py ####################################

from datetime import date
from tools import Unit
from tools import DegradationProperty


class TestDegradationPropertyClass(unittest.TestCase):
    def test_gaussian_degradation(self):
        d = DegradationProperty(
            initiation_date=date(2000, 1, 1),
            distribution={
                'type': 'gaussian',
                'sigma': Unit(20, 'day').to('second').val,
                'mean': Unit(100, 'day').to('second').val,
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
                'main': Unit(70, 'day').to('second').val,
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
                'main': Unit(70, 'day').to('second').val,
            },
            seed=202
        )
        p = d.probability_of_working(
            start_date=Unit(0, 'day')+date(2000, 1, 1),
            end_date=Unit(50, 'day')+date(2000, 1, 1)
        )
        self.assertEqual(p, 1, msg="dirac_degradation_1")


#################################### entity.py ####################################


class TestEntityClass(unittest.TestCase):
    def test_entity_distance(self):
        e_1 = Entity(pos=[0, 0])
        e_2 = Entity(pos=[0, 1])
        d = e_1.distance(e_2)
        self.assertAlmostEqual(d, 1, places=5, msg="distance")


#################################### source.py ####################################


class TestUseProduceClass(unittest.TestCase):
    def test_refill(self):
        p = Produce(rate=Unit(5, 'ton/day'))
        p.refill(delta_t=Unit(1, 'day'))
        self.assertEqual(p.current_amount.to('ton/day').val, 5, msg="refill")

    def test_sub(self):
        p = Produce(rate=Unit(5, 'ton/day'))
        p.refill(delta_t=Unit(1, 'day'))
        p.sub(Unit(10, 'ton'))
        self.assertEqual(p.current_amount.to('ton/day').val, 0, msg="refill")


class TestDeficiencyClass(unittest.TestCase):
    def test_add(self):
        d = Deficiency(
            current_amount=Unit(1, 'kg'),
            max_amount=Unit(5, 'kg')
        )
        d.add(Unit(1, 'kg'))
        val = d.current_amount.to('kg').val
        self.assertEqual(val, 2, msg='add')

    def test_add_max(self):
        d = Deficiency(
            current_amount=Unit(1, 'kg'),
            max_amount=Unit(5, 'kg')
        )
        d.add(Unit(5, 'kg'))
        val = d.current_amount.to('kg').val
        self.assertEqual(val, 5, msg='add')

    def test_add_max_alive(self):
        d = Deficiency(
            current_amount=Unit(1, 'kg'),
            max_amount=Unit(5, 'kg')
        )
        d.add(Unit(5, 'kg'))
        self.assertFalse(d.is_alive(), msg='not alive')


#################################### statistical_distribtuion.py ####################################


class TestGaussianClass(unittest.TestCase):
    def test_normal_distribution(self):
        time_start = Unit(0, 'day').to('second').val
        time_end = Unit(70, 'day').to('second').val

        g = Gaussian(
            mean=time_end,
            sigma=Unit(10, 'day').to('second').val
        )
        p = g.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be equal")


class TestDiracDeltaClass(unittest.TestCase):
    def test_dirac_distribution_0(self):
        time_start = Unit(0, 'day').to('second').val
        time_end = Unit(70, 'day').to('second').val

        d = DiracDelta(
            main=Unit(35, 'day').to('second').val
        )
        p = d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 1, msg="Should be equal")

    def test_dirac_distribution_1(self):
        time_start = Unit(0, 'day').to('second').val
        time_end = Unit(30, 'day').to('second').val

        d = DiracDelta(
            main=Unit(35, 'day').to('second').val
        )
        p = d.probability(
            time_start=time_start,
            time_end=time_end
        )
        self.assertEqual(p, 0, msg="Should be equal")


#################################### unit.py ####################################


class TestUnitClass(unittest.TestCase):
    def test_conversion(self):
        v = Unit(2, 'km/hour')
        v_new = v.to('m/minute')
        v_new.convert('km/hour')
        self.assertAlmostEqual(
            v.val, v_new.val, places=10, msg="test_conversion")

    def test_sum(self):
        v_1 = Unit(1, 'km/hour')
        v_2 = Unit(1, 'km/hour')
        v = v_1 + v_2
        self.assertAlmostEqual(v.val, 2, places=10, msg="Should be equal")

    def test_sum_time(self):
        t_0 = date(2020, 1, 1)
        t_1 = Unit(1, 'day')
        t = t_1 + t_0
        self.assertEqual(t, date(2020, 1, 2), msg="Should be equal")

    def test_sub(self):
        v_1 = Unit(2, 'km/hour')
        v_2 = Unit(1, 'km/hour')
        v = v_1 - v_2
        self.assertAlmostEqual(v.val, 1, places=10, msg="Should be equal")

    def test_sub_time(self):
        t_0 = date(2020, 1, 2)
        t_1 = Unit(1, 'day')
        t = t_1 - t_0
        self.assertEqual(t, date(2020, 1, 1), msg="Should be equal")

    def test_mul(self):
        v = Unit(1, 'km/hour')
        v_new = v * 2
        self.assertAlmostEqual(v_new.val, 2, places=10, msg="Should be equal")

    def test_div(self):
        v = Unit(2.5, 'km/hour')
        v_new = v / 2
        self.assertAlmostEqual(v_new.val, 2.5/2, places=10, msg="Should be equal")


if __name__ == '__main__':
    unittest.main()
