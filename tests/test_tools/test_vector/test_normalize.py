import unittest
from piperabm.tools.vector.normalize import normalize


class TestNormalize(unittest.TestCase):

    def test_normalize(self):
        vector = [5, 0]
        norm = normalize(vector)
        self.assertEqual(norm, [1, 0])


if __name__ == "__main__":
    unittest.main()
