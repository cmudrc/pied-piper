import unittest

from piperabm.unit import Unit, Date


class TestUnitClass(unittest.TestCase):
    def test_conversion(self):
        v = Unit(2, 'km/hour')
        v_new = v.to('m/minute')
        v_new.convert('km/hour')
        self.assertAlmostEqual(
            v.val, v_new.val, places=10, msg="test_conversion")

    def test_conversion_angle(self):
        v = Unit(1, 'rad')
        v_new = v.to('degree')
        self.assertAlmostEqual(v_new.val, 57.29578, places=5)

    def test_sum(self):
        v_1 = Unit(1, 'km/hour')
        v_2 = Unit(1, 'km/hour')
        v = v_1 + v_2
        self.assertAlmostEqual(v.val, 2, places=10, msg="Should be equal")

    def test_sum_time(self):
        t_0 = Date(2020, 1, 1)
        t_1 = Unit(1, 'day')
        t = t_1 + t_0
        self.assertEqual(t, Date(2020, 1, 2), msg="Should be equal")

    def test_sub(self):
        v_1 = Unit(2, 'km/hour')
        v_2 = Unit(1, 'km/hour')
        v = v_1 - v_2
        self.assertAlmostEqual(v.val, 1, places=10, msg="Should be equal")

    def test_sub_time(self):
        t_0 = Date(2020, 1, 2)
        t_1 = Unit(1, 'day')
        t = t_1 - t_0
        self.assertEqual(t, Date(2020, 1, 1), msg="Should be equal")

    def test_mul(self):
        v = Unit(1, 'km/hour')
        v_new = v * 2
        self.assertAlmostEqual(v_new.val, 2, places=10, msg="Should be equal")

    def test_div(self):
        v = Unit(2.5, 'km/hour')
        v_new = v / 2
        self.assertAlmostEqual(v_new.val, 2.5/2, places=10, msg="Should be equal")

    def test_to_SI(self):
        v = Unit(2.5, 'km/hour')
        v_new = v.to_SI()
        self.assertAlmostEqual(v_new, 0.7, places=1, msg="Should be equal")


if __name__ == "__main__":
    unittest.main()