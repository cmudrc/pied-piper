import unittest

from piperabm.tools.linear_algebra.vector.magnitude import magnitude


class TestMagnitudeFunction(unittest.TestCase):

    def test_0(self):
        vector = [0, 0, 0]
        self.assertEqual(magnitude(vector), 0)

    def test_1(self):
        vector = [0, 3, 4]
        self.assertEqual(magnitude(vector), 5)


if __name__ == '__main__':
    unittest.main()