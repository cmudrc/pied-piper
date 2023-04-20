import unittest

from piperabm.tools.coordinate.inverse_function import inverse_function


class TestInverseFunction(unittest.TestCase):
    
    def test_0(self):
        factor = inverse_function(True)
        expected_result = -1
        self.assertEqual(factor, expected_result)

    def test_1(self):
        factor = inverse_function(False)
        expected_result = 1
        self.assertEqual(factor, expected_result)


if __name__ == "__main__":
    unittest.main()