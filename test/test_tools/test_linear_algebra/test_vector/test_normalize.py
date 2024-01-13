import unittest

from piperabm.tools.linear_algebra.vector.normalize import normalize


class TestNormalizeFunction(unittest.TestCase):

    def test_0(self):
        vector = [5, 0, 0]
        result = normalize(vector, ndarray=False)
        self.assertListEqual(result, [1, 0, 0])
        

if __name__ == '__main__':
    unittest.main()