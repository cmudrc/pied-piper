import unittest
from copy import deepcopy

from piperabm.resource.matter import Matter
from piperabm.resource.matter.samples import matter_0


class TestObjectClass(unittest.TestCase):

    def setUp(self) -> None:
        self.matter = deepcopy(matter_0)
    
    def test_add(self):
        self.matter + 1
        self.assertEqual(self.matter(), 7)

    def test_sub_0(self):
        self.matter - 1
        self.assertEqual(self.matter(), 5)

    def test_sub_1(self):
        self.matter - 7
        self.assertEqual(self.matter(), -1)

    def test_mul(self):
        self.matter * 2
        self.assertEqual(self.matter(), 12)

    def test_truediv(self):
        self.matter / 0.5
        self.assertEqual(self.matter(), 12)

    def test_dict(self):
        dictionary = self.matter.to_dict()
        self.assertEqual(dictionary, 6)
        matter = Matter()
        matter.from_dict(dictionary)
        self.assertEqual(matter, self.matter)

    def test_delta(self):
        matter_previous = deepcopy(self.matter)
        self.matter + 1
        delta = self.matter - matter_previous
        self.assertEqual(delta, 1)
        matter_previous + delta
        self.assertEqual(matter_previous, self.matter)


if __name__ == "__main__":
    unittest.main()
