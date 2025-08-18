import unittest
from piperabm.tools.vector.magnitude import magnitude


class TestMagnitude(unittest.TestCase):

    def test_magnitude(self):
        vector = [3, 4]
        mag = magnitude(vector)
        self.assertEqual(mag, 5)


if __name__ == "__main__":
    unittest.main()
