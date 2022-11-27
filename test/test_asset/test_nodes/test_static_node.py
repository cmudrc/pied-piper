import unittest
from copy import deepcopy

from piperabm.asset import Storage, Deficiency


class TestStorage(unittest.TestCase):
    
    s = Storage(
        current_amount=1,
        max_amount=5
    )

    def test_sub_0_remaining(self):
        storage = deepcopy(self.s)
        remaining = storage.sub(1)
        self.assertEqual(remaining, 0)
    
    def test_sub_0_current_amount(self):
        storage = deepcopy(self.s)
        storage.sub(1)
        self.assertEqual(storage.current_amount, 0)

    def test_sub_1_remaining(self):
        storage = deepcopy(self.s)
        remaining = storage.sub(2)
        self.assertEqual(remaining, 1)

    def test_sub_1_current_amount(self):
        storage = deepcopy(self.s)
        storage.sub(2)
        self.assertEqual(storage.current_amount, 0)

    def test_add_none(self):
        storage = Storage(current_amount=2)
        storage.add(1000)
        self.assertEqual(storage.current_amount, 1002)


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

    def test_add_remaining_0(self):
        self.assertEqual(self.remaning, 0)

    def test_add_max(self):
        d = deepcopy(self.d)
        d.add(5)
        self.assertEqual(d.current_amount, 5, msg='add')

    def test_add_remaining_1(self):
        d = deepcopy(self.d)
        remaining = d.add(5)
        self.assertEqual(remaining, 2, msg='remaining')

    def test_add_max_alive(self):
        d = deepcopy(self.d)
        d.add(5)
        self.assertFalse(d.is_alive(), msg='not alive')


if __name__ == "__main__":
    unittest.main()