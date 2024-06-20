import unittest

from piperabm.model import Model


class TestSingleResourceSolver(unittest.TestCase):

    def setUp(self):
        model = Model()
        point_1 = [0, 0]
        point_2 = [1000, 0]
        self.home_id = 0
        self.market_id = 1
        model.infrastructure.add_home(pos=point_1, id=self.home_id)
        model.infrastructure.add_market(
            pos=point_2,
            id=self.market_id,
            food=100,
            water=100,
            energy=100
        )
        model.infrastructure.add_street(pos_1=point_1, pos_2=point_2)
        model.bake()
        self.model = model
        self.model.society.generate_agents(num=2, gini_index=0)
        self.agents = self.model.society.agents
        val = self.model.society.food( self.agents[0])
        self.model.society.food( self.agents[0], new_val=val/10)
        #print(self.model.infrastructure.stat)
        #self.model.infrastructure.show()

    def test_run(self):
        self.model.step_size = 100

        market_initial = self.model.infrastructure.food(self.market_id)
        agent_initial = self.model.society.food(self.agents[0])
        #print(self.model.society.pos(self.agents[0]))
        self.assertListEqual(self.model.society.actions[self.agents[0]].library, [])
        self.assertAlmostEqual(self.model.society.pos(self.agents[0])[0], 0, places=1)
        self.assertEqual(self.model.society.get_current_node(self.agents[0]), self.home_id)
        print(self.model.society.food(self.agents[1]))

        # Decide to go to market
        self.model.run(n=1)
        #print(self.model.society.actions[self.agents[0]])
        #total_duration = self.model.society.actions[self.agents[0]].total_duration
        #print(total_duration) # = 85680
        market_mid = self.model.infrastructure.food(self.market_id)
        agent_mid = self.model.society.food(self.agents[0])
        self.assertNotAlmostEqual(self.model.society.pos(self.agents[0])[0], 1000, places=1)
        self.assertEqual(self.model.society.get_current_node(self.agents[0]), None)
        self.assertEqual(market_initial, market_mid)
        self.assertLess(agent_mid, agent_initial)

        # Reached market
        self.model.run(n=10)

        market_final = self.model.infrastructure.food(self.market_id)
        agent_final = self.model.society.food(self.agents[0])
        self.assertAlmostEqual(self.model.society.pos(self.agents[0])[0], 1000, places=1)
        self.assertEqual(self.model.society.get_current_node(self.agents[0]), self.market_id)
        self.assertLess(market_final, market_mid)
        self.assertLess(agent_mid, agent_final)

        # Get back home
        self.model.step_size = 10000
        self.model.run(n=9)

        self.assertEqual(self.model.society.actions[self.agents[0]].remaining, 0)

        # Here we go again!
        self.model.run(n=1)
        remaining = self.model.society.actions[self.agents[0]].remaining
        self.assertLess(0, remaining)


if __name__ == "__main__":
    unittest.main()