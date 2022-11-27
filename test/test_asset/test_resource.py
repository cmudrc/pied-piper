import unittest
from copy import deepcopy

from piperabm.asset import Storage, Deficiency, Use, Produce
from piperabm.asset import Resource
from piperabm.unit import Unit


class TestResourceClass(unittest.TestCase):

    r = Resource(
        name='food',
        use=Use(rate=1),
        storage=Storage(current_amount=5, max_amount=10)
    )
    r.refill(1)

    def test_source_demand(self):
        self.assertEqual(self.r.source(), 5)


if __name__ == "__main__":
    unittest.main()