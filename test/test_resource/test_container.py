import unittest
from copy import deepcopy

from piperabm.resource.container import Container
from piperabm.resource.container.samples import container_0


class TestContainerClass(unittest.TestCase):

    def setUp(self) -> None:
        self.container = deepcopy(container_0)
    
    def test_add(self):
        remainder = self.container + 6
        self.assertEqual(self.container(), 10)
        self.assertEqual(remainder, 2)

    def test_sub(self):
        remainder = self.container - 8
        self.assertEqual(self.container(), 0)
        self.assertEqual(remainder, 2)

    def test_mul(self):
        remainder = self.container * 2
        self.assertEqual(self.container(), 10)
        self.assertEqual(remainder, 2)

    def test_truediv(self):
        remainder = self.container / 0.5
        self.assertEqual(self.container(), 10)
        self.assertEqual(remainder, 2)

    def test_dict(self):
        dictionary = self.container.to_dict()
        expected_result = {
            'amount': 6,
            'min': 0,
            'max': 10,
        }
        self.assertEqual(dictionary, expected_result)
        container = Container()
        container.from_dict(dictionary)
        self.assertEqual(container, self.container)

    def test_delta(self):
        container_previous = deepcopy(self.container)
        self.container + 1
        delta = self.container - container_previous
        self.assertEqual(delta, 1)
        container_previous + delta
        self.assertEqual(container_previous, self.container)


if __name__ == "__main__":
    unittest.main()
