import unittest
from copy import deepcopy

from piperabm.society.samples.society_0 import model as model_0
from piperabm.society.samples.society_1 import model as model_1


class TestTrade_0(unittest.TestCase):
    """
    Two agents
    """

    def setUp(self) -> None:
        self.model = deepcopy(model_0)
        self.model.society.average_income = 0
        agents = self.model.society.agents
        wealth_0 = self.model.society.wealth(id=agents[0])
        wealth_1 = self.model.society.wealth(id=agents[1])
        if wealth_0 < wealth_1:
            self.id_low = agents[0]  # Agent with lower food
            self.id_high = agents[1]  # Agent with higher food
        food = self.model.society.get_resource(self.id_low, 'food')
        self.model.society.set_resource(self.id_low, 'food', value=food/10)
        water = self.model.society.get_resource(self.id_low, 'water')
        self.model.society.set_resource(self.id_low, 'water', value=water/5)

    def test_trade(self):
        balance_low_initial = self.model.society.get_balance(self.id_low)
        balance_high_initial = self.model.society.get_balance(self.id_high)
        food_low_initial = self.model.society.get_resource(self.id_low, 'food')
        food_high_initial = self.model.society.get_resource(self.id_high, 'food')
        
        transactions = self.model.update(duration=1)
        
        balance_low_final = self.model.society.get_balance(self.id_low)
        balance_high_final = self.model.society.get_balance(self.id_high)
        food_low_final = self.model.society.get_resource(self.id_low, 'food')
        food_high_final = self.model.society.get_resource(self.id_high, 'food')

        total_food_initial = food_low_initial + food_high_initial
        total_food_final = food_low_final + food_high_final
        self.assertAlmostEqual(total_food_initial, total_food_final, places=4)

        self.assertLess(balance_low_final, balance_low_initial)
        self.assertLess(food_low_initial, food_low_final)
        self.assertLess(balance_high_initial, balance_high_final)
        self.assertLess(food_high_final, food_high_initial)


class TestTrade_1(unittest.TestCase):
    """
    An agent in market
    """

    def setUp(self):
        self.model = deepcopy(model_1)
        self.agent_id = 1
        self.home_id = 1
        self.market_id = 2
        #self.model
        '''
        self.agents = self.model.society.agents
        '''
        val = self.model.society.get_resource(
            id=self.agent_id,
            name='food'
        )
        self.model.society.set_resource(
            id=self.agent_id,
            name='food',
            value=val/10
        )
        self.model.prices = {
            'food': 100,
            'water': 100,
            'energy': 100
        }
        self.model.society.idle_resource_rates = {
            'food': 0.0001,
            'water': 0.0001,
            'energy': 0.0001
        }
        self.model.society.transportation_resource_rates = {
            'food': 0.0002,
            'water': 0.0002,
            'energy': 0.0002,
        }
        self.model.society.activity_cycle = 900
        self.model.society.max_time_outside = 300
        #print(self.model.infrastructure.stat)
        #self.model.infrastructure.show()

    
    def test_run(self):
        #estimated_duration = self.model.society.estimated_duration(self.agent_id, destination_id=self.market_id)
        #print(estimated_duration)

        balances = []
        foods = []

        # Agent decides to go to market
        current_node = self.model.society.get_current_node(id=self.agent_id)
        self.assertEqual(current_node, 1)
        balance = self.model.society.get_balance(self.agent_id)
        balances.append(balance)
        food = self.model.society.get_resource(self.agent_id, 'food')
        foods.append(food)

        self.model.update(duration=50) # Update

        # Still on his way
        current_node = self.model.society.get_current_node(id=self.agent_id)
        self.assertEqual(current_node, None)
        balance = self.model.society.get_balance(self.agent_id)
        balances.append(balance)
        food = self.model.society.get_resource(self.agent_id, 'food')
        foods.append(food)

        self.model.update(duration=50) # Update

        # In the market
        current_node = self.model.society.get_current_node(id=self.agent_id)
        self.assertEqual(current_node, 2)
        balance = self.model.society.get_balance(self.agent_id)
        balances.append(balance)
        food = self.model.society.get_resource(self.agent_id, 'food')
        foods.append(food)

        self.model.update(duration=50) # Update

        # In the market
        current_node = self.model.society.get_current_node(id=self.agent_id)
        self.assertEqual(current_node, 2)
        balance = self.model.society.get_balance(self.agent_id)
        balances.append(balance)
        food = self.model.society.get_resource(self.agent_id, 'food')
        foods.append(food)

        self.model.update(duration=100) # Update

        # In the way to home
        current_node = self.model.society.get_current_node(id=self.agent_id)
        self.assertEqual(current_node, None)
        balance = self.model.society.get_balance(self.agent_id)
        balances.append(balance)
        food = self.model.society.get_resource(self.agent_id, 'food')
        foods.append(food)

        self.model.update(duration=100) # Update

        # At home
        current_node = self.model.society.get_current_node(id=self.agent_id)
        self.assertEqual(current_node, 1)
        balance = self.model.society.get_balance(self.agent_id)
        balances.append(balance)
        food = self.model.society.get_resource(self.agent_id, 'food')
        foods.append(food)

        self.model.update(duration=553)

        '''    
        max_depth = 10000
        i = 0
        while i < max_depth:
            self.model.update(duration=1) # Update
            i += 1
            if self.model.society.get_current_node(id=self.agent_id) != 1:
                break
        print(i)
        '''

        # In market
        current_node = self.model.society.get_current_node(id=self.agent_id)
        self.assertEqual(current_node, 1)
        balance = self.model.society.get_balance(self.agent_id)
        balances.append(balance)
        food = self.model.society.get_resource(self.agent_id, 'food')
        foods.append(food)

        self.model.update(duration=553)

        current_node = self.model.society.get_current_node(id=self.agent_id)
        #self.assertEqual(current_node, None)

        #print(balances)
        #print(foods)
        #print(self.model.society.get_enough_resource(self.agent_id, 'food'))
        '''
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
        '''


if __name__ == "__main__":
    unittest.main()