import unittest
from copy import deepcopy

from piperabm.economy import Pool, Bid


class TestPoolClass1(unittest.TestCase):

    def setUp(self):
        b1 = Bid(1, 5)
        b2 = Bid(2, 8)
        b3 = Bid(3, 2)
        b4 = Bid(4, 1)

        p = Pool()
        p.add_source([b2, b4])
        p.add_demand([b1, b3])
        self.p = p

    def test_find_biggest(self):
        p = deepcopy(self.p)
        biggest_source_bid = p.find_biggest_bid(p.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        biggest_demand_bid = p.find_biggest_bid(p.demand_bids)
        self.assertEqual(biggest_demand_bid.agent, 1)

    def test_find(self):
        p = deepcopy(self.p)
        agent_index = 2
        bid, type = p.find_bid(agent_index)
        self.assertEqual(type, 'source')
        self.assertEqual(bid.agent, agent_index)
    
    def test_solve_step(self):
        p = deepcopy(self.p)
        #print(p)
        p.solve_step()
        #print(p)
        biggest_source = p.find_biggest_bid(p.source_bids)
        self.assertEqual(biggest_source.agent, 2)
        biggest_demand = p.find_biggest_bid(p.demand_bids)
        self.assertEqual(biggest_demand.agent, 3)
    
    def test_solve(self):
        p = deepcopy(self.p)
        #print(p)
        p.solve()
        #print(p)


class TestPoolClass2(unittest.TestCase):

    def setUp(self):
        b2 = Bid(2, 8)
        b4 = Bid(4, 1)

        p = Pool()
        p.add_source([b2, b4])
        p.add_demand([])
        self.p = p

    def test_solve_step(self):
        p = deepcopy(self.p)
        #print(p)
        p.solve_step()
        #print(p)
        biggest_source = p.find_biggest_bid(p.source_bids)
        self.assertEqual(biggest_source.agent, 2)
        biggest_demand = p.find_biggest_bid(p.demand_bids)
        self.assertEqual(biggest_demand.agent, 3)


if __name__ == "__main__":
    unittest.main()