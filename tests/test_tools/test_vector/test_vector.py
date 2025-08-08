import unittest
from piperabm.tools.vector import vector as vc


class TestVector(unittest.TestCase):

    def test_magnitude(self):
        vector = [3, 4]
        mag = vc.magnitude(vector)
        self.assertEqual(mag, 5)

    def test_normalize(self):
        vector = [5, 0]
        norm = vc.normalize(vector)
        self.assertEqual(norm, [1, 0])


if __name__ == "__main__":
    unittest.main()
