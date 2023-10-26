import unittest
from copy import deepcopy

from piperabm.model.samples import model_3
from piperabm.economy import Market


class TestMarketClass(unittest.TestCase):

    def setUp(self):
        players = model_3.all_alive_agents
        self.market = Market(players, model_3)

    def test_find_biggest_demand_source(self):
        market = deepcopy(self.market)
        buyer_index, biggest_resource_name, buying_amount = market.find_biggest_demand()
        self.assertEqual(biggest_resource_name, "food")
        self.assertAlmostEqual(buying_amount, 15.79, places=2)
        seller_index, selling_amount = market.find_biggest_source(buyer_index, biggest_resource_name)
        self.assertNotEqual(buyer_index, seller_index)
        self.assertEqual(selling_amount, 20)
        
    def test_run_step(self):
        market = deepcopy(self.market)
        players = market.players
        player = players[0]
        agent = market.get(player)
        initial_resource_amount = deepcopy(agent.resources("food"))
        market.run_step()
        agent = market.get(player)
        final_resource_amount = agent.resources("food")
        self.assertNotEqual(initial_resource_amount, final_resource_amount)


if __name__ == "__main__":
    unittest.main()