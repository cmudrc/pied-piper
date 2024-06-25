import unittest
from copy import deepcopy

from piperabm.infrastructure.samples import model_1 as model


class TestActions_0(unittest.TestCase):
    """
    Normal run
    """
    def setUp(self):
        self.id_agent = 0
        self.id_start = 1
        self.id_end = 2
        self.model = deepcopy(model)
        self.model.society.add_agent(
            socioeconomic_status=1,
            id=self.id_agent,
            home_id=self.id_start,
            food=100,
            water=100,
            energy=100,
            enough_food=100,
            enough_water=100,
            enough_energy=100,
            balance=100
        )
        self.model.society.go_and_comeback_and_stay(agent_id=self.id_agent, destination_id=self.id_end)

    def test_update(self):
        street = self.model.infrastructure.streets[0]
        pos_start = self.model.infrastructure.get_pos(id=self.id_start)
        pos_end = self.model.infrastructure.get_pos(id=self.id_end)
        queue = self.model.society.actions[self.id_agent]
        #print(queue.total_duration) # total_duration = 86400.0 seconds

        # Beginning (home)
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 4) # queue undones
        self.assertListEqual(
            self.model.society.get_pos(id=self.id_agent),
            pos_start
        ) # pos
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            self.id_start
        ) # current_node
        food_0 = self.model.society.get_resource(id=self.id_agent, name='food')
        self.assertEqual(food_0, 100) # resources food
        water_0 = self.model.society.get_resource(id=self.id_agent, name='water')
        self.assertEqual(water_0, 100) # resources water
        energy_0 = self.model.society.get_resource(id=self.id_agent, name='energy')
        self.assertAlmostEqual(energy_0, 100) # resources energy
        self.assertEqual(self.model.infrastructure.get_usage_impact(ids=street), 0) # usage impact
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_0 = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertNotEqual(acc_0, 0) # accessibility

        # On the way to the destination
        self.model.run(n=1, report=False, step_size=50) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 4) # queue undones
        #print(self.model.society.get_pos(id=self.id_agent)) # pos
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            None
        ) # current_node
        food_1 = self.model.society.get_resource(id=self.id_agent, name='food')
        self.assertLess(food_1, food_0) # resources food
        water_1 = self.model.society.get_resource(id=self.id_agent, name='water')
        self.assertLess(water_1, water_0) # resources water
        energy_1 = self.model.society.get_resource(id=self.id_agent, name='energy')
        self.assertLess(energy_1, energy_0) # resources energy
        self.assertEqual(
            self.model.infrastructure.get_usage_impact(ids=street),
            0
        ) # usage impact
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_1 = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertLess(acc_1, acc_0) # accessibility

        # Waiting in the destination
        self.model.run(n=1, report=False, step_size=50) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 3) # queue undones
        #print(self.model.society.get_pos(id=self.id_agent)) # pos
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            self.id_end
        ) # current_node
        food_2 = self.model.society.get_resource(id=self.id_agent, name='food')
        self.assertLess(food_2, food_1) # resources food
        water_2 = self.model.society.get_resource(id=self.id_agent, name='water')
        self.assertLess(water_2, water_1) # resources water
        energy_2 = self.model.society.get_resource(id=self.id_agent, name='energy')
        self.assertLess(energy_2, energy_1) # resources energy
        self.assertEqual(
            self.model.infrastructure.get_usage_impact(ids=street),
            1
        ) # usage impact
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_2 = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertLess(acc_2, acc_1) # accessibility
        
        # On the way to the home
        self.model.run(n=1, report=False, step_size=28650) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 2) # queue undones
        #print(self.model.society.get_pos(id=self.id_agent)) # pos
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            None
        ) # current_node
        food_3 = self.model.society.get_resource(id=self.id_agent, name='food')
        self.assertLess(food_3, food_2) # resources food
        water_3 = self.model.society.get_resource(id=self.id_agent, name='water')
        self.assertLess(water_3, water_2) # resources water
        energy_3 = self.model.society.get_resource(id=self.id_agent, name='energy')
        self.assertLess(energy_3, energy_2) # resources energy
        self.assertEqual(
            self.model.infrastructure.get_usage_impact(ids=street),
            1
        ) # usage impact
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_3 = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertLess(acc_3, acc_2) # accessibility

        # Ending (home)
        self.model.run(n=1, report=False, step_size=10000) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 1) # queue undones
        #print(self.model.society.get_pos(id=self.id_agent)) # pos
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            self.id_start
        ) # current_node
        food_4 = self.model.society.get_resource(id=self.id_agent, name='food')
        self.assertLess(food_4, food_3) # resources food
        water_4 = self.model.society.get_resource(id=self.id_agent, name='water')
        self.assertLess(water_4, water_3) # resources water
        energy_4 = self.model.society.get_resource(id=self.id_agent, name='energy')
        self.assertLess(energy_4, energy_3) # resources energy
        self.assertEqual(
            self.model.infrastructure.get_usage_impact(ids=street),
            2
        ) # usage impact
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_4 = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertLess(acc_4, acc_3) # accessibility


class TestActions_1(unittest.TestCase):
    """
    Agent dies along the way
    """
    def setUp(self):
        self.id_agent = 0
        self.id_start = 1
        self.id_end = 2
        self.model = deepcopy(model)
        self.model.society.add_agent(
            socioeconomic_status=1,
            id=self.id_agent,
            home_id=self.id_start,
            food=0.003,
            water=0.003,
            energy=0.003,
            enough_food=100,
            enough_water=100,
            enough_energy=100,
            balance=100
        )
        self.model.society.go_and_comeback_and_stay(agent_id=self.id_agent, destination_id=self.id_end)

    def test_update(self):
        street = self.model.infrastructure.streets[0]
        pos_start = self.model.infrastructure.get_pos(id=self.id_start)
        pos_end = self.model.infrastructure.get_pos(id=self.id_end)
        queue = self.model.society.actions[self.id_agent]

        # Alive
        self.model.run(n=1, report=False, step_size=50) # run
        self.assertEqual(len(queue.undones), 4) # queue undones
        self.assertTrue(self.model.society.get_alive(id=self.id_agent)) # agent alive
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            None
        ) # current_node
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_0 = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertNotEqual(acc_0, 0) # accessibility

        # Dead
        self.model.run(n=1, report=False, step_size=50) # run
        self.assertEqual(len(queue.undones), 4) # queue undones
        self.assertFalse(self.model.society.get_alive(id=self.id_agent)) # agent alive
        pos_dead = self.model.society.get_pos(id=self.id_agent) # pos
        self.assertNotEqual(pos_dead, pos_start) # pos
        self.assertNotEqual(pos_dead, pos_end) # pos
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            None
        ) # current_node
        food_dead = self.model.society.get_resource(id=self.id_agent, name='food')
        self.assertEqual(food_dead, 0) # resources food
        water_dead = self.model.society.get_resource(id=self.id_agent, name='water')
        self.assertNotEqual(water_dead, 0) # resources water
        energy_dead = self.model.society.get_resource(id=self.id_agent, name='energy')
        self.assertNotEqual(energy_dead, 0) # resources energy
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_dead = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertEqual(acc_dead, 0) # accessibility

        # Dead (continued)
        self.model.run(n=1, report=False, step_size=1000) # run
        self.assertEqual(len(queue.undones), 4) # queue undones
        self.assertFalse(self.model.society.get_alive(id=self.id_agent)) # agent alive
        self.assertListEqual(
            self.model.society.get_pos(id=self.id_agent),
            pos_dead
        ) # pos
        self.assertEqual(
            self.model.society.get_current_node(id=self.id_agent),
            None
        ) # current_node
        food_dead_continued = self.model.society.get_resource(id=self.id_agent, name='food')
        self.assertEqual(food_dead_continued, 0) # resources food
        water_dead_continued = self.model.society.get_resource(id=self.id_agent, name='water')
        self.assertEqual(water_dead_continued, water_dead) # resources water
        energy_dead_continued = self.model.society.get_resource(id=self.id_agent, name='energy')
        self.assertEqual(energy_dead_continued, energy_dead) # resources energy
        self.assertEqual(
            self.model.infrastructure.get_usage_impact(ids=street),
            0
        ) # usage impact
        acc = self.model.society.accessibility(id=self.id_agent)
        acc_dead_continued = (acc['food'] * acc['water'] * acc['energy']) ** (1 / 3)
        self.assertEqual(acc_dead, acc_dead_continued) # accessibility

if __name__ == "__main__":
    unittest.main()