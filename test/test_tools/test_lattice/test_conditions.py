import unittest

from piperabm.tools.lattice.conditions import condition_1


class TestLatticeConditionClass(unittest.TestCase):

    def setUp(self) -> None:
        self.condition = condition_1

    def test_0(self):
        input = [
            [0, 0, 0,],
            [0, 1, 0,],
            [0, 0, 0,],
        ]
        result = self.condition.check(input)
        self.assertFalse(result)

    def test_1(self):
        input = [
            [0, 0, 0,],
            [0, 1, 1,],
            [0, 0, 0,],
        ]
        result = self.condition.check(input)
        self.assertTrue(result)

    def test_2(self):
        input = [
            [0, 0, 0,],
            [0, 1, 1,],
            [0, 1, 0,],
        ]
        result = self.condition.check(input)
        self.assertFalse(result)

    def test_3(self):
        input = [
            [0, 0, 0,],
            [0, 1, 0,],
            [0, 1, 0,],
        ]
        result = self.condition.check(input)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()