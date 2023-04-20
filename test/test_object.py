import unittest

from piperabm.object import Object
from piperabm.tools.symbols import SYMBOLS


class TestUnitClass(unittest.TestCase):

    def setUp(self) -> None:
        
        class A(Object):

            def __init__(self, val=None):
                super().__init__()
                self.val = val
            
            def to_dict(self) -> dict:
                dictionary = {}
                dictionary['val'] = self.val
                return dictionary

            def from_dict(self, dictionary: dict) -> None:
                self.val = dictionary['val']
        
        self.A = A(val=5)
        self.ClassA = A
    
    def test_str(self):
        txt = self.A.__str__()
        expected_result = "{'val': 5}"
        self.assertEqual(txt, expected_result)

    def test_dict(self):
        dictionary = self.A.to_dict()
        expected_result = {'val': 5}
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        new_A = self.ClassA()
        new_A.from_dict(dictionary)
        new_dictionary = new_A.to_dict()
        expected_result = {'val': 5}
        self.assertDictEqual(new_dictionary, expected_result)
        self.assertEqual(self.A, new_A)

    def test_add_0(self):
        delta = {'val': 2}
        self.A + delta
        self.assertEqual(self.A.val, 7)

    def test_add_1(self):
        delta = {'val': 0}
        self.A + delta
        self.assertEqual(self.A.val, 5)

    def test_add_2(self):
        delta = {'val': -2}
        self.A + delta
        self.assertEqual(self.A.val, 3)

    def test_sub_0(self):
        delta = {'val': 2}
        self.A - delta
        self.assertEqual(self.A.val, 3)

    def test_sub_1(self):
        delta = {'val': 0}
        self.A - delta
        self.assertEqual(self.A.val, 5)

    def test_sub_2(self):
        delta = {'val': -2}
        self.A - delta
        self.assertEqual(self.A.val, 7)

    def test_mul_0(self):
        delta = {'val': 2}
        self.A * delta
        self.assertEqual(self.A.val, 10)

    def test_mul_1(self):
        delta = {'val': 0}
        self.A * delta
        self.assertEqual(self.A.val, 0)

    def test_mul_2(self):
        delta = {'val': -2}
        self.A * delta
        self.assertEqual(self.A.val, -10)

    def test_truediv_0(self):
        delta = {'val': 2}
        self.A / delta
        self.assertEqual(self.A.val, 2.5)

    def test_truediv_1(self):
        delta = {'val': 0}
        self.A / delta
        self.assertEqual(self.A.val, SYMBOLS['inf'])

    def test_truediv_2(self):
        delta = {'val': -2}
        self.A / delta
        self.assertEqual(self.A.val, -2.5)


if __name__ == "__main__":
    unittest.main()
      