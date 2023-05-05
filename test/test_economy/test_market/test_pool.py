import unittest
from copy import deepcopy

from piperabm.economy.market.pool import Pool, Bid


class TestPoolClass_4Bids(unittest.TestCase):

    def setUp(self):
        b1 = Bid(agent=1, amount=5)
        b2 = Bid(agent=2, amount=8)
        b3 = Bid(agent=3, amount=2)
        b4 = Bid(agent=4, amount=1)

        pool = Pool()
        pool.add_source([b2, b4])
        pool.add_demand([b1, b3])
        self.pool = pool

    def test_find(self):
        pool = deepcopy(self.pool)
        agent_index = 2
        bid, type = pool.find_bid(agent_index)
        self.assertEqual(type, 'source')
        self.assertEqual(bid.agent, agent_index)

    def test_size(self):
        pool = deepcopy(self.pool)
        size_source, size_demand = pool.size()
        self.assertEqual(size_source, 9)
        self.assertEqual(size_demand, 7)

    def test_find_biggest(self):
        pool = deepcopy(self.pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid.agent, 1)
    
    def test_solve_step_by_step(self):
        pool = deepcopy(self.pool)
        #print(pool)
        ''' step 1 '''
        pool.solve_step()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        self.assertEqual(biggest_source_bid.amount, 8)
        self.assertEqual(biggest_source_bid.new_amount, 3)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid.agent, 3)
        self.assertEqual(biggest_demand_bid.amount, 2)
        self.assertEqual(biggest_demand_bid.new_amount, 2)
        ''' step 2 '''
        pool.solve_step()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        self.assertEqual(biggest_source_bid.amount, 8)
        self.assertEqual(biggest_source_bid.new_amount, 1)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid.agent, 1)
        self.assertEqual(biggest_demand_bid.amount, 5)
        self.assertEqual(biggest_demand_bid.new_amount, 0)
    
    def test_solve(self):
        pool = deepcopy(self.pool)
        #print(pool)
        pool.solve()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        self.assertEqual(biggest_source_bid.amount, 8)
        self.assertEqual(biggest_source_bid.new_amount, 1)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid.agent, 1)
        self.assertEqual(biggest_demand_bid.amount, 5)
        self.assertEqual(biggest_demand_bid.new_amount, 0)
        #print(pool.stat)


class TestPoolClass_1Bid(unittest.TestCase):
    
    def setUp(self):
        b2 = Bid(agent=2, amount=8)

        pool = Pool()
        pool.add_source([b2])
        pool.add_demand([])
        self.pool = pool

    def test_solve_step(self):
        pool = deepcopy(self.pool)
        #print(pool)
        stat = pool.solve_step()
        self.assertDictEqual(stat, {'volume': 0})
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        self.assertEqual(biggest_source_bid.amount, 8)
        self.assertEqual(biggest_source_bid.new_amount, 8)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid, None)

    def test_solve(self):
        pool = deepcopy(self.pool)
        #print(pool)
        stat = pool.solve()
        expected_result = {'transactions': [], 'total_volume': 0}
        self.assertDictEqual(stat, expected_result)
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        self.assertEqual(biggest_source_bid.amount, 8)
        self.assertEqual(biggest_source_bid.new_amount, 8)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid, None)
        #print(pool.stat)


class TestPoolClass_2Bids_Source(unittest.TestCase):

    def setUp(self):
        b2 = Bid(agent=2, amount=8)
        b4 = Bid(agent=4, amount=1)

        pool = Pool()
        pool.add_source([b2, b4])
        pool.add_demand([])
        self.pool = pool

    def test_solve_step(self):
        pool = deepcopy(self.pool)
        #print(pool)
        pool.solve_step()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        self.assertEqual(biggest_source_bid.amount, 8)
        self.assertEqual(biggest_source_bid.new_amount, 8)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid, None)

    def test_solve(self):
        pool = deepcopy(self.pool)
        #print(pool)
        pool.solve()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid.agent, 2)
        self.assertEqual(biggest_source_bid.amount, 8)
        self.assertEqual(biggest_source_bid.new_amount, 8)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid, None)
        #print(pool.stat)


class TestPoolClass_2Bids_Demand(unittest.TestCase):

    def setUp(self):
        b2 = Bid(agent=2, amount=8)
        b4 = Bid(agent=4, amount=1)

        pool = Pool()
        pool.add_source([])
        pool.add_demand([b2, b4])
        self.pool = pool

    def test_solve_step(self):
        pool = deepcopy(self.pool)
        #print(pool)
        pool.solve_step()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid, None)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid.agent, 2)
        self.assertEqual(biggest_demand_bid.amount, 8)
        self.assertEqual(biggest_demand_bid.new_amount, 8)

    def test_solve(self):
        pool = deepcopy(self.pool)
        #print(pool)
        pool.solve()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid, None)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid.agent, 2)
        self.assertEqual(biggest_demand_bid.amount, 8)
        self.assertEqual(biggest_demand_bid.new_amount, 8)
        #print(pool.stat)


class TestPoolClass_0Bids(unittest.TestCase):

    def setUp(self):
        self.pool = Pool()

    def test_solve_step(self):
        pool = deepcopy(self.pool)
        #print(pool)
        pool.solve_step()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid, None)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid, None)

    def test_solve(self):
        pool = deepcopy(self.pool)
        #print(pool)
        pool.solve()
        #print(pool)
        biggest_source_bid = pool.find_biggest_bid(pool.source_bids)
        self.assertEqual(biggest_source_bid, None)
        biggest_demand_bid = pool.find_biggest_bid(pool.demand_bids)
        self.assertEqual(biggest_demand_bid, None)
        #print(pool.stat)


class TestPoolClass_Standard(unittest.TestCase):
    """
    Test based on standard samples
    """

    def setUp(self):
        from piperabm.society.agent.samples import sample_agent_0, sample_agent_1
        from piperabm.economy.exchange.sample import exchange_0 as exchange

        agent_0 = deepcopy(sample_agent_0)
        agent_1 = deepcopy(sample_agent_1)
        amount = agent_0.resource.max_resource['food'] - agent_0.resource.current_resource['food']
        max_amount = agent_0.balance / exchange.rate('food', 'wealth')
        if amount > max_amount:
            amount = max_amount
        b1 = Bid(agent=agent_0.index, amount=amount)

        amount = agent_1.resource.current_resource['food']
        b2 = Bid(agent=agent_1.index, amount=amount)

        pool = Pool()
        pool.add_source([b2])
        pool.add_demand([b1])
        self.pool = pool

    def test_solve(self):
        pool = deepcopy(self.pool)
        pool.solve()
        #print(pool.stat)
        #print(pool)
    

if __name__ == "__main__":
    unittest.main()