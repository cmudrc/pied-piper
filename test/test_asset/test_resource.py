import unittest
from copy import deepcopy

from pr.asset import Storage, Deficiency
from pr.asset import Use, Produce
from pr.tools import Unit


class TestUseProduceClass(unittest.TestCase):
    """
    Use and Produce classes behave the same, so testing one is enough.
    """

    p = Produce(rate=Unit(5, 'ton/day').to_SI())
    p.refill(delta_t=Unit(1, 'day').to_SI())

    def test_refill(self):
        self.assertEqual(self.p.current_amount, Unit(5, 'ton').to('kg').to_SI(), msg="refill")

    def test_sub(self):
        self.p.sub(Unit(10, 'ton').to('kg').to_SI())
        self.assertEqual(self.p.current_amount, 0, msg="refill")


class TestStorage(unittest.TestCase):
    
    s = Storage(
        current_amount=1,
        max_amount=5
    )

    def test_sub(self):
        storage = deepcopy(self.s)
        remaining = storage.sub(2)
        self.assertEqual(remaining, 0)


class TestDeficiencyClass(unittest.TestCase):
    """
    Storage and Deficiency classes behave (almost) the same, so testing one is enough.
    """

    d = Deficiency(
        current_amount=1,
        max_amount=5
    )
    remaning = d.add(1)

    def test_add(self):
        self.assertEqual(self.d.current_amount, 2, msg='add')

    def test_add_remaining(self):
        self.assertEqual(self.remaning, 0)

    def test_add_max(self):
        d = deepcopy(self.d)
        d.add(5)
        self.assertEqual(d.current_amount, 5, msg='add')

    def test_add_remaining(self):
        d = deepcopy(self.d)
        remaining = d.add(5)
        self.assertEqual(remaining, 2, msg='remaining')

    def test_add_max_alive(self):
        d = deepcopy(self.d)
        d.add(5)
        self.assertFalse(d.is_alive(), msg='not alive')


if __name__ == "__main__":
    unittest.main()