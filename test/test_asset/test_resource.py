import unittest
from copy import deepcopy

from piperabm.asset import Storage, Deficiency, Use, Produce
from piperabm.asset import Resource
from piperabm.unit import Unit


class TestResourceClass(unittest.TestCase):

    r = Resource(
        name='food',
        use=Use(rate=1),
        storage=Storage(current_amount=5, max_amount=10),
        deficiency=Deficiency(current_amount=0, max_amount=10)
    )
    r.refill(1)

    def test_source_demand(self):
        r = deepcopy(self.r)
        self.assertEqual(r.source(), 5)
        self.assertEqual(r.demand(), 6)

    def test_solve(self):
        r = deepcopy(self.r)
        r.solve()
        self.assertEqual(r.source(), 4)
        self.assertEqual(r.demand(), 6)
    
    def test_finalize(self):
        r = deepcopy(self.r)
        r.use=Use(rate=20)
        r.refill(1)
        #print(r)
        r.solve()
        #print(r)
        r.finalize()
        #print(r)
        self.assertFalse(r.is_alive())


if __name__ == "__main__":
    unittest.main()