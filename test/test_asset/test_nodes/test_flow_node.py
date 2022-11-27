import unittest
from copy import deepcopy

from piperabm.asset import Use, Produce


class TestProduceClass(unittest.TestCase):

    p = Produce(rate=5)
    p.refill(delta_t=1)

    def test_refill(self):
        current_amount = self.p.current_amount
        val = 5
        self.assertEqual(current_amount, val, msg="refill")

    def test_sub(self):
        self.p.sub(10)
        val = 0
        current_amount = self.p.current_amount
        self.assertEqual(current_amount, val, msg="sub")


if __name__ == "__main__":
    unittest.main()