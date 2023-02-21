import unittest
from copy import deepcopy

from piperabm.economy import Pool, Bid


class TestPoolClass(unittest.TestCase):

    b1 = Bid(1, 5)
    b2 = Bid(2, 8)
    b3 = Bid(3, 2)
    b4 = Bid(4, 1)

    p = Pool()
    p.add_source([b2, b4])
    p.add_demand([b1, b3])

    def test_find_biggest(self):
        p = deepcopy(self.p)
        biggest_source = p.find_biggest(p.source_bids)
        self.assertEqual(biggest_source.agent, 2)
        biggest_demand = p.find_biggest(p.demand_bids)
        self.assertEqual(biggest_demand.agent, 1)

    def test_find(self):
        p = deepcopy(self.p)
        agent_index = 2
        bid = p.find_bid(agent_index)
        self.assertEqual(bid.agent, agent_index)

    def test_solve_step(self):
        p = deepcopy(self.p)
        #print(p)
        p.solve_step()
        #print(p)
        biggest_source = p.find_biggest(p.source_bids)
        self.assertEqual(biggest_source.agent, 2)
        biggest_demand = p.find_biggest(p.demand_bids)
        self.assertEqual(biggest_demand.agent, 3)

    def test_solve(self):
        p = deepcopy(self.p)
        #print(p)
        p.solve()
        #print(p)


if __name__ == "__main__":
    unittest.main()