import unittest


#################################### statistic.py ####################################

from datetime import date

from unit_manager import Unit


class TestUnitClass(unittest.TestCase):
    def test_conversion(self):
        v = Unit(2, 'km/hour')
        v_new = v.to('m/minute')
        v_new.convert('km/hour')
        self.assertAlmostEqual(v.val, v_new.val, places=10, msg="test_conversion")

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
        v = Unit(2, 'km/hour')
        v_new = v // 2
        self.assertAlmostEqual(v_new.val, 1, places=10, msg="Should be equal")


#################################### statistic.py ####################################

from statistic import Gaussian, DiracDelta


class TestGaussianClass(unittest.TestCase):
    def test_normal_distribution(self):
        time_start=Unit(0, 'day')
        time_end=Unit(70, 'day')

        g = Gaussian(
            mean=time_end,
            sigma=Unit(10, 'day')
        )
        p = g.probability(
                time_start=time_start,
                time_end=time_end
            )
        self.assertAlmostEqual(p, 0.5, places=5, msg="Should be equal")


class TestDiracDeltaClass(unittest.TestCase):
    def test_dirac_distribution_0(self):
        time_start=Unit(0, 'day')
        time_end=Unit(70, 'day')
        
        d = DiracDelta(
            main=Unit(35, 'day')
        )
        p = d.probability(
                time_start=time_start,
                time_end=time_end
            )
        self.assertEqual(p, 1, msg="Should be equal")

    def test_dirac_distribution_1(self):
        time_start=Unit(0, 'day')
        time_end=Unit(30, 'day')
        
        d = DiracDelta(
            main=Unit(35, 'day')
        )
        p = d.probability(
                time_start=time_start,
                time_end=time_end
            )
        self.assertEqual(p, 0, msg="Should be equal")


#################################### boundery.py ####################################

from boundery import Circular


class Other():
    """ Only a helper class """
    def __init__(self, pos):
        self.pos = pos


class TestCircularClass(unittest.TestCase):
    def test_circular_boundery_in(self):
        other = Other(pos=[1, 1])
        boundery = Circular(center=[0, 0], radius=2)
        self.assertTrue(boundery.is_in(other) , msg="Should be equal")

    def test_circular_boundery_out(self):
        other = Other(pos=[1, 2])
        boundery = Circular(center=[0, 0], radius=2)
        self.assertFalse(boundery.is_in(other) , msg="Should be equal")


if __name__ == '__main__':
    unittest.main()