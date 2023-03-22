import unittest
from copy import deepcopy

from piperabm.economy import Exchange
from piperabm.economy.market import Player, Market


class TestMarketClass1(unittest.TestCase):

    def setUp(self):
        p1 = Player(
            1,
            source={
                'food': 4,
            },
            demand={
                'food': 6,
            },
            wallet=10
        )
        p2 = Player(
            2,
            source={
                'food': 2,
            },
            demand={
                'food': 8,
            },
            wallet=20
            )

        exchange = Exchange()
        exchange.add('food', 'wealth', 5)

        mkt = Market(exchange)
        mkt.add([p1, p2])
        self.mkt = mkt

    def test_solve(self):
        mkt = deepcopy(self.mkt)
        mkt.solve()
        #print(mkt)


class TestMarketClass(unittest.TestCase):

    def setUp(self):
        p1 = Player(
            1,
            source={
                'food': 4,
                'water': 5,
            },
            demand={
                'food': 6,
                'water': 5,
            },
            wallet=10
        )
        p2 = Player(
            2,
            source={
                'food': 2,
                'water': 5,
            },
            demand={
                'food': 8,
                'water': 5,
            },
            wallet=20
            )
        p3 = Player(
            3,
            source={
                'food': 5,
                'water': 5,
            },
            demand={
                'food': 5,
                'water': 5,
            },
            wallet=20
            )

        exchange = Exchange()
        exchange.add('food', 'wealth', 10)
        exchange.add('water', 'wealth', 2)

        market = Market(exchange)
        market.add([p1, p2, p3])
        #print(market)
        self.market = market

    def test_add(self):
        market = deepcopy(self.market)
        players = market.players
        self.assertEqual(len(players), 3)
    
    def test_find_player(self):
        self.assertEqual(self.market.find_player(3).index, 3)
        self.assertEqual(self.market.find_player(4), None)

    def test_all_resources(self):
        expected_result = ['food', 'water']
        self.assertListEqual(self.market.all_resources(), expected_result)

    def test_total_demand(self):
        self.assertEqual(self.market.total_demand('food'), 19)
        self.assertEqual(self.market.total_demand('water'), 15)

    def test_total_actual_demand(self):
        self.assertEqual(self.market.total_actual_demand('food'), 5)
        self.assertEqual(self.market.total_actual_demand('water'), 15)

    def test_total_source(self):
        self.assertEqual(self.market.total_source('food'), 11)
        self.assertEqual(self.market.total_source('water'), 15)

    def test_size(self):
        self.assertEqual(self.market.size(), 220)

    def test_extract_resource_info(self):
        player = self.market.find_player(1)
        player_source, player_demand, others_source, others_demand = \
        self.market.extract_resource_info(player, 'food')
        self.assertEqual(player_source, 4)
        self.assertEqual(player_demand, 1)
        self.assertEqual(others_source, 7)
        self.assertEqual(others_demand, 4)

    def test_score(self):
        player = self.market.find_player(1)
        buyer_score, seller_score = self.market.score(player, 'food')
        self.assertEqual(buyer_score, 7)
        self.assertEqual(seller_score, 16)

    def test_create_bid(self):
        player = self.market.find_player(1)
        bid, type = self.market.create_bid(player, 'food')
        self.assertEqual(type, 'source')
        self.assertEqual(bid.amount, 4)

    def test_create_pool(self):
        pool = self.market.create_pool('food')
        source_bids = pool.source_bids
        self.assertEqual(len(source_bids), 2)
        demand_bids = pool.demand_bids
        self.assertEqual(len(demand_bids), 1)

    def test_create_pools(self):
        market = deepcopy(self.market)
        market.create_pools()
        pool = market.pools['food']
        source_bids = pool.source_bids
        self.assertEqual(len(source_bids), 2)
        demand_bids = pool.demand_bids
        self.assertEqual(len(demand_bids), 1)

    def test_sort_pools(self):
        market = deepcopy(self.market)
        market.create_pools()
        #print(market.pools['food'].size(), market.pools['water'].size())
        result = market.sort_pools()
        expected_result = ['food', 'water']
        self.assertListEqual(result, expected_result)

    def test_solve(self):
        market = deepcopy(self.market)
        market.solve()
        #print(mkt)



if __name__ == "__main__":
    unittest.main()