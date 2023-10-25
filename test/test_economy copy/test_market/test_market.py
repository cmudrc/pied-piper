import unittest
from copy import deepcopy

from piperabm.economy.exchange_rate import ExchangeRate
from piperabm.economy.market import Player, Market

from piperabm.agent.samples import agent_0, agent_1
from piperabm.economy.exchange_rate.samples import exchange_rate_0 as exchange


class TestMarketClass_1Player(unittest.TestCase):
    """
    2 players, 1 resource each
    """

    def setUp(self):
        p1 = Player(
            1,
            source={'food': 4},
            demand={'food': 6},
            wallet=10
        )

        exchange = ExchangeRate()
        exchange.add('food', 'wealth', 5)

        market = Market(exchange)
        market.add([p1])
        #print(market)

        ''' pass objects to the tests '''
        self.market = market

    def test_create_pools(self):
        market = deepcopy(self.market)
        market.create_pools()
        pool = market.pools['food']
        source_bids = pool.source_bids
        self.assertEqual(source_bids[0].agent, 1)
        self.assertEqual(source_bids[0].initial_amount, 4)
        self.assertEqual(source_bids[0].amount, 4)
        demand_bids = pool.demand_bids
        self.assertListEqual(demand_bids, [])

    def test_solve_biggest_pool(self):
        market = deepcopy(self.market)
        market.solve_biggest_pool()
        pool = market.pools['food']
        #print(pool.stat)

        agent = 1
        bid, type = pool.find_bid(agent=agent)
        self.assertEqual(type, 'source')
        self.assertEqual(bid.initial_amount, 4)
        self.assertEqual(bid.amount, 4)
        seller = market.find_player(index=agent)
        self.assertEqual(seller.source['food'], 4)
        self.assertEqual(seller.new_source['food'], 4)
        self.assertEqual(seller.demand['food'], 6)
        self.assertEqual(seller.new_demand['food'], 6)

    def test_solve(self):
        market = deepcopy(self.market)
        stat = market.solve()
        #print(market)
        #print(stat)

        agent_index = 1
        agent = market.find_player(index=agent_index)
        self.assertEqual(agent.source['food'], 4)
        self.assertEqual(agent.new_source['food'], 4)
        self.assertEqual(agent.demand['food'], 6)
        self.assertEqual(agent.new_demand['food'], 6)


class TestMarketClass_2Players(unittest.TestCase):
    """
    2 players, 1 resource each
    """

    def setUp(self):
        p1 = Player(
            1,
            source={'food': 4},
            demand={'food': 6},
            wallet=10
        )
        p2 = Player(
            2,
            source={'food': 2},
            demand={'food': 8},
            wallet=20
            )

        exchange = ExchangeRate()
        exchange.add('food', 'wealth', 5)

        market = Market(exchange)
        market.add([p1, p2])
        #print(market)

        ''' pass objects to the tests '''
        self.market = market

    def test_create_pools(self):
        market = deepcopy(self.market)
        market.create_pools()
        pool = market.pools['food']
        source_bids = pool.source_bids
        self.assertEqual(source_bids[0].agent, 1)
        self.assertEqual(source_bids[0].initial_amount, 4)
        self.assertEqual(source_bids[0].amount, 4)
        demand_bids = pool.demand_bids
        self.assertEqual(demand_bids[0].agent, 2)
        self.assertEqual(demand_bids[0].initial_amount, 4)
        self.assertEqual(demand_bids[0].amount, 4)

    def test_solve_biggest_pool(self):
        market = deepcopy(self.market)
        market.solve_biggest_pool()
        pool = market.pools['food']
        #print(pool.stat)

        agent = 1
        bid, type = pool.find_bid(agent=agent)
        self.assertEqual(type, 'source')
        self.assertEqual(bid.initial_amount, 4)
        self.assertEqual(bid.amount, 0)
        seller = market.find_player(index=agent)
        self.assertEqual(seller.source['food'], 4)
        self.assertEqual(seller.new_source['food'], 0)
        self.assertEqual(seller.demand['food'], 6)
        self.assertEqual(seller.new_demand['food'], 6)

        agent = 2
        bid, type = pool.find_bid(agent=agent)
        self.assertEqual(type, 'demand')
        self.assertEqual(bid.initial_amount, 4)
        self.assertEqual(bid.amount, 0)
        buyer = market.find_player(index=agent)
        self.assertEqual(buyer.source['food'], 2)
        self.assertEqual(buyer.new_source['food'], 2)
        self.assertEqual(buyer.demand['food'], 8)
        self.assertEqual(buyer.new_demand['food'], 4)

    def test_solve(self):
        market = deepcopy(self.market)
        market.solve()
        #print(market)
        #print(market.stat)

        agent_index = 1
        agent = market.find_player(index=agent_index)
        self.assertEqual(agent.source['food'], 4)
        self.assertEqual(agent.new_source['food'], 0)
        self.assertEqual(agent.demand['food'], 6)
        self.assertEqual(agent.new_demand['food'], 4)

        agent_index = 2
        agent = market.find_player(index=agent_index)
        self.assertEqual(agent.source['food'], 2)
        self.assertEqual(agent.new_source['food'], 0)
        self.assertEqual(agent.demand['food'], 8)
        self.assertEqual(agent.new_demand['food'], 4)


class TestMarketClass_3Players(unittest.TestCase):
    """
    3 players, 2 resource each
    """

    def setUp(self):
        p1 = Player(
            1,
            source={'food': 4, 'water': 5},
            demand={'food': 6, 'water': 5 },
            wallet=10
        )
        p2 = Player(
            2,
            source={'food': 2, 'water': 5},
            demand={'food': 8, 'water': 5},
            wallet=20
            )
        p3 = Player(
            3,
            source={'food': 5, 'water': 5},
            demand={'food': 5, 'water': 5},
            wallet=20
            )

        exchange = ExchangeRate()
        exchange.add('food', 'wealth', 10)
        exchange.add('water', 'wealth', 2)

        market = Market(exchange)
        market.add([p1, p2, p3])
        #print(market)

        ''' pass objects to the tests '''
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

    def test_biggest_pool(self):
        market = deepcopy(self.market)
        market.create_pools()
        biggest_pool_name = market.biggest_pool()
        self.assertEqual(biggest_pool_name, 'food')

    def test_solve_pool(self): ###### change to test_biggest_pool
        market = deepcopy(self.market)
        market.create_pools()

        market.solve_pool('food')  # biggest pool
        #print(market.stat)
        pool = market.pools['food']
        #print(pool.stat) # >>> transaction from 3 ta 2, amount=2
        source_bids = pool.source_bids
        self.assertEqual(source_bids[1].agent, 3)
        self.assertEqual(source_bids[1].initial_amount, 5)
        self.assertEqual(source_bids[1].amount, 3)
        seller = market.find_player(index=source_bids[1].agent)
        self.assertEqual(seller.new_source['food'], 3)
        self.assertEqual(seller.new_demand['food'], 5)
        demand_bids = pool.demand_bids
        self.assertEqual(demand_bids[0].agent, 2)
        self.assertEqual(demand_bids[0].initial_amount, 2)
        self.assertEqual(demand_bids[0].amount, 0)
        buyer = market.find_player(index=demand_bids[0].agent)
        self.assertEqual(buyer.new_source['food'], 2)
        self.assertEqual(buyer.new_demand['food'], 6)

    def test_solve(self):
        market = deepcopy(self.market)
        market.create_pools()

        market.solve()
        #print(market)
        #print(market.stat['food'])


class TestMarketClass_0Players(unittest.TestCase):
    """
    No players
    """

    def setUp(self):
        market = Market(exchange)
        market.add([])
        #print(market)

        ''' pass objects to the tests '''
        self.market = market

    def test_create_pool(self):
        market = deepcopy(self.market)
        pool = market.create_pool('food')
        source_bids = pool.source_bids
        self.assertListEqual(source_bids, [])
        demand_bids = pool.demand_bids
        self.assertListEqual(demand_bids, [])

    def test_sort_pools(self):
        market = deepcopy(self.market)
        market.create_pools()
        self.assertDictEqual(market.pools, {})
        result = market.sort_pools()
        self.assertListEqual(result, [])

    def test_biggest_pool(self):
        market = deepcopy(self.market)
        market.create_pools()
        biggest_pool = market.biggest_pool()
        self.assertEqual(biggest_pool, None)

    def test_solve_biggest_pool(self):
        market = deepcopy(self.market)
        
        # step 1:
        market.create_pools()
        biggest_pool = market.biggest_pool()
        self.assertEqual(biggest_pool, None)
        stat = market.solve_biggest_pool()
        expected_result = {
            'food': {'transactions': [], 'total_volume': 0},
            'water': {'transactions': [], 'total_volume': 0},
            'energy': {'transactions': [], 'total_volume': 0},
            'size': []
        }
        self.assertDictEqual(stat, expected_result)
        #print(market)

    def test_solve(self):
        market = deepcopy(self.market)
        stat = market.solve()
        #print(stat)
        #print(market)


class TestMarketClass_Standard(unittest.TestCase):
    """
    2 players, 2 resource each, standard inputs
    """

    def setUp(self):
        p1 = Player(
            1,
            source=deepcopy(agent_0.source.to_dict()),
            demand=deepcopy(agent_0.demand.to_dict()),
            wallet=deepcopy(agent_0.balance)
        )
        p2 = Player(
            2,
            source=deepcopy(agent_1.source.to_dict()),
            demand=deepcopy(agent_1.demand.to_dict()),
            wallet=deepcopy(agent_1.balance)
            )

        market = Market(exchange)
        market.add([p1, p2])
        #print(market)

        ''' pass objects to the tests '''
        self.market = market

    def test_score(self):
        player_1 = self.market.find_player(1)
        buyer_score_1, seller_score_1 = self.market.score(player=player_1, resource_name='food')
        self.assertListEqual([buyer_score_1, seller_score_1], [700, 400])
        player_2 = self.market.find_player(2)
        buyer_score_2, seller_score_2 = self.market.score(player=player_2, resource_name='food')
        self.assertListEqual([buyer_score_2, seller_score_2], [400, 700])

    def test_create_pool(self):
        market = deepcopy(self.market)
        pool = market.create_pool('food')
        source_bids = pool.source_bids
        #print(source_bids[0])
        self.assertEqual(source_bids[0].initial_amount, 70)
        self.assertEqual(source_bids[0].amount, 70)
        demand_bids = pool.demand_bids
        #print(demand_bids[0])
        self.assertEqual(demand_bids[0].initial_amount, 10)
        self.assertEqual(demand_bids[0].amount, 10)

    def test_sort_pools(self):
        market = deepcopy(self.market)
        market.create_pools()
        #print(market.pools['food'].size(), market.pools['water'].size(), market.pools['energy'].size())
        result = market.sort_pools()
        expected_result = ['water', 'energy', 'food']
        self.assertListEqual(result, expected_result)

    def test_biggest_pool(self):
        market = deepcopy(self.market)
        market.create_pools()
        biggest_pool = market.biggest_pool()
        self.assertEqual(biggest_pool, 'water')

    def test_solve_biggest_pool(self):
        market = deepcopy(self.market)
        
        # step 1:
        market.create_pools()
        biggest_pool = market.biggest_pool()
        self.assertEqual(biggest_pool, 'water')
        stat = market.solve_biggest_pool()
        #print(len(stat[biggest_pool]['transactions']))
        volume = stat[biggest_pool]['transactions'][0]['volume']
        _from = stat[biggest_pool]['transactions'][0]['from']
        _to = stat[biggest_pool]['transactions'][0]['to']
        #print('volume: ' + str(volume) + ' [from ' + str(_from) + ' to ' + str(_to) + ']')
        seller = market.find_player(index=_from)
        buyer = market.find_player(index=_to)
        self.assertEqual(seller.source[biggest_pool] - seller.new_source[biggest_pool], volume)
        self.assertEqual(buyer.demand[biggest_pool] -  buyer.new_demand[biggest_pool], volume)
        self.assertEqual(seller.new_wallet - seller.wallet, volume*exchange.rate(biggest_pool, 'wealth'))
        self.assertEqual(buyer.wallet - buyer.new_wallet, volume*exchange.rate(biggest_pool, 'wealth'))
        #print(market)

        # step 2:
        market.create_pools()
        #print(market)
        biggest_pool = market.biggest_pool()
        self.assertEqual(biggest_pool, 'food')
        stat = market.solve_biggest_pool()
        #print(market)
        #print(len(stat[biggest_pool]['transactions']))
        volume = stat[biggest_pool]['transactions'][0]['volume']
        _from = stat[biggest_pool]['transactions'][0]['from']
        _to = stat[biggest_pool]['transactions'][0]['to']
        #print('volume: ' + str(volume) + ' [from ' + str(_from) + ' to ' + str(_to) + ']')
        seller = market.find_player(index=_from)
        buyer = market.find_player(index=_to)
        #print(buyer, seller)
        self.assertEqual(seller.source[biggest_pool] - seller.new_source[biggest_pool], volume)
        self.assertEqual(buyer.demand[biggest_pool] -  buyer.new_demand[biggest_pool], volume)
        self.assertEqual(seller.new_wallet - 0, volume*exchange.rate(biggest_pool, 'wealth'))
        self.assertEqual(300 - buyer.new_wallet, volume*exchange.rate(biggest_pool, 'wealth'))
        #print(stat)

        market.create_pools()
        #print(market)
        biggest_pool = market.biggest_pool()
        self.assertEqual(biggest_pool, 'energy')
        stat = market.solve_biggest_pool()
        #print(stat)

    def test_solve(self):
        market = deepcopy(self.market)
        stat = market.solve()
        #print(stat)
        #print(market)


if __name__ == "__main__":
    unittest.main()