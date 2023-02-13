import unittest
from copy import deepcopy

from piperabm.resource import Storage, Deficiency, Use, Produce
from piperabm.resource import Resource


class TestResourceClass(unittest.TestCase):

    r = Resource(
        name='food',
        use=Use(rate=1),
        storage=Storage(current_amount=5, max_amount=10),
        deficiency=Deficiency(current_amount=0, max_amount=10)
    )

    def test_source_demand(self):
        r = deepcopy(self.r)
        r.refill(1)
        self.assertEqual(r.source(), 5)
        self.assertEqual(r.demand(), 6)

    def test_allocate_internal(self):
        r = deepcopy(self.r)
        r.refill(1)
        r.allocate_internal()
        self.assertEqual(r.source(), 4)
        self.assertEqual(r.demand(), 6)

    def test_add(self):
        r = deepcopy(self.r)
        r.refill(1)
        r.allocate_internal()
        amount = 10
        remaining = r.add(amount)
        self.assertEqual(remaining, 4)

    def test_sub(self):
        r = deepcopy(self.r)
        r.refill(1)
        r.allocate_internal()
        amount = 10
        remaining = r.sub(amount)
        self.assertEqual(remaining, 6)
    
    def test_finalize(self):
        r = deepcopy(self.r)
        r.use=Use(rate=20)
        r.refill(1)
        r.allocate_internal()
        r.finalize()
        self.assertFalse(r.is_alive())


if __name__ == "__main__":
    unittest.main()