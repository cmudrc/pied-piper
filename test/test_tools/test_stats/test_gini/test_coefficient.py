import unittest

from piperabm.tools.stats import gini


class TestGiniCoefficientFunction(unittest.TestCase):

    def test_0(self):
        """ All similar """
        data = [5, 5]
        gini_index = gini.coefficient(data)
        self.assertEqual(gini_index, 0)

    def test_1(self):
        data = [0, 10, 10, 10, 10]
        gini_index = gini.coefficient(data)
        self.assertEqual(gini_index, 0.2)

    def test_2(self):
        data = [0, 0, 10, 10, 10]
        gini_index = gini.coefficient(data)
        self.assertEqual(gini_index, 0.4)

    def test_3(self):
        data = [0, 10]
        gini_index = gini.coefficient(data)
        self.assertEqual(gini_index, 0.5)

    def test_4(self):
        data = [0, 0, 0, 10, 10]
        gini_index = gini.coefficient(data)
        self.assertEqual(gini_index, 0.6)

    def test_5(self):
        data = [0, 0, 0, 0, 10]
        gini_index = gini.coefficient(data)
        self.assertEqual(gini_index, 0.8)


if __name__ == '__main__':
    unittest.main()