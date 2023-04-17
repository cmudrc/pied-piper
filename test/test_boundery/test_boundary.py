import unittest

from piperabm.boundary import Boundary


class TestCircularClass(unittest.TestCase):
    
    def setUp(self):
        self.boundary = Boundary()

    def test_relative_pos(self):
        center = [10, 10]
        pos = [13, 14]
        relative_pos = self.boundary.relative_pos(pos, center)
        self.assertEqual(relative_pos, [3, 4])


if __name__ == "__main__":
    unittest.main()