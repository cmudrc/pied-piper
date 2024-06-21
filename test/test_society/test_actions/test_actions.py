import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure.samples import model_1 as model
#from piperabm.infrastructure.paths import Paths
from piperabm.society.actions import Move, Stay


class TestActions_0(unittest.TestCase):
    """
    Normal run
    """
    def setUp(self):
        self.id_agent = 0
        self.id_start = 1
        self.id_end = 2

        # Model
        self.model = model
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
        self.model_idle = deepcopy(self.model)  # Agent won't move

        # Action
        #paths = Paths()
        #paths.create(infrastructure=self.model.infrastructure)
        #paths.update()
        path = self.model.infrastructure.path(self.id_start, self.id_end)
        action_1 = Stay(duration=DeltaTime(seconds=3))
        action_2 = Move(path)
        action_3 = Stay(duration=DeltaTime(seconds=3))
        agent = self.model.society.get(self.id_agent)
        agent.queue.add(action_1)
        agent.queue.add(action_2)
        agent.queue.add(action_3)

    def test_update(self):
        street_id = self.model.infrastructure.streets[0]
        street = self.model.infrastructure.get(street_id)
        object_start = self.model.infrastructure.get(id=self.id_start)
        pos_start = object_start.pos
        object_end = self.model.infrastructure.get(id=self.id_end)
        pos_end = object_end.pos
        agent = self.model.society.get(id=self.id_agent)
        queue = agent.queue

        # Beginning
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 3) # queue undones
        self.assertListEqual(agent.pos, pos_start) # pos
        self.assertEqual(agent.current_node, self.id_start) # current_node
        self.assertEqual(agent.time_outside.total_seconds(), 0) # time outside
        self.assertAlmostEqual(agent.resources('food'), 100, places=1) # resources food
        self.assertAlmostEqual(agent.resources('water'), 100, places=1) # resources water
        self.assertAlmostEqual(agent.resources('energy'), 100, places=1) # resources energy
        self.assertEqual(street.degradation, 0) # degradation

        # Middle
        self.model.run(n=40, report=False) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 2) # queue undones
        self.assertEqual(agent.time_outside.total_seconds(), 37) # time outside
        self.assertAlmostEqual(agent.resources('food'), 60, places=1) # resources food
        self.assertAlmostEqual(agent.resources('water'), 60, places=1) # resources water
        self.assertAlmostEqual(agent.resources('energy'), 60, places=1) # resources energy
        self.assertAlmostEqual(street.degradation, 0.4, places=2) # degradation
        #print(agent.pos)

        # Ending
        self.model.run(n=25, report=False) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 1) # queue undones
        self.assertListEqual(agent.pos, pos_end) # pos
        self.assertEqual(agent.current_node, self.id_end) # current_node
        self.assertEqual(agent.time_outside.total_seconds(), 62) # time outside
        self.assertAlmostEqual(agent.resources('food'), 35, places=1) # resources food ####################
        self.assertAlmostEqual(agent.resources('water'), 35, places=1) # resources water
        self.assertAlmostEqual(agent.resources('energy'), 35, places=1) # resources energy
        self.assertAlmostEqual(street.degradation, 1.65, places=2) # degradation
        

class TestActions_1(unittest.TestCase):
    """
    Agent dies along the way
    """
    def setUp(self):
        self.id_agent = 0
        self.id_start = 1
        self.id_end = 2

        # Model
        step_size = DeltaTime(seconds=1)  # Seconds
        self.model = Model(
            infrastructure=deepcopy(infrastructure),
            step_size=step_size,  # Seconds
        )
        agent = Agent(
            resources=Matter({
                'food': 20,
                'water': 20,
                'energy': 20
            }),
            enough_resources=Matter({
                'food': 20,
                'water': 20,
                'energy': 20
            })
        )
        agent.home = self.id_start
        self.model.society.add(agent, id=0)
        self.model_idle = deepcopy(self.model)  # Agent won't move

        # Action
        paths = Paths()
        paths.create(infrastructure=self.model.infrastructure)
        paths.update()
        path = paths.path(self.id_start, self.id_end)
        action_1 = Stay(duration=DeltaTime(seconds=3))
        action_2 = Move(path)
        action_3 = Stay(duration=DeltaTime(seconds=3))
        agent = self.model.society.get(self.id_agent)
        agent.queue.add(action_1)
        agent.queue.add(action_2)
        agent.queue.add(action_3)

    def test_update(self):
        street_id = self.model.infrastructure.streets[0]
        street = self.model.infrastructure.get(street_id)
        object_start = self.model.infrastructure.get(id=self.id_start)
        pos_start = object_start.pos
        object_end = self.model.infrastructure.get(id=self.id_end)
        pos_end = object_end.pos # Will never reach
        agent = self.model.society.get(id=self.id_agent)
        queue = agent.queue

        # Beginning
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 3) # queue undones
        self.assertListEqual(agent.pos, pos_start) # pos
        self.assertEqual(agent.current_node, self.id_start) # current_node
        self.assertEqual(agent.time_outside.total_seconds(), 0) # time outside
        self.assertAlmostEqual(agent.resources('food'), 20, places=1) # resources food
        self.assertAlmostEqual(agent.resources('water'), 20, places=1) # resources water
        self.assertAlmostEqual(agent.resources('energy'), 20, places=1) # resources energy
        self.assertTrue(agent.alive)
        self.assertEqual(street.degradation, 0) # degradation

        # Middle
        self.model.run(n=40, report=False) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 2) # queue undones
        pos_death = agent.pos
        self.assertEqual(agent.time_outside.total_seconds(), 17) # time outside
        self.assertAlmostEqual(agent.resources('food'), 0, places=1) # resources food
        self.assertAlmostEqual(agent.resources('water'), 0, places=1) # resources water
        self.assertAlmostEqual(agent.resources('energy'), 0, places=1) # resources energy
        self.assertFalse(agent.alive)
        self.assertAlmostEqual(street.degradation, 0.4, places=2) # degradation

        # Ending
        self.model.run(n=25, report=False) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 2) # queue undones
        self.assertListEqual(agent.pos, pos_death) # pos
        self.assertEqual(agent.current_node, None) # current_node
        self.assertEqual(agent.time_outside.total_seconds(), 17) # time outside
        self.assertAlmostEqual(agent.resources('food'), 0, places=1) # resources food
        self.assertAlmostEqual(agent.resources('water'), 0, places=1) # resources water
        self.assertAlmostEqual(agent.resources('energy'), 0, places=1) # resources energy
        self.assertFalse(agent.alive)
        self.assertAlmostEqual(street.degradation, 0.65, places=2) # degradation
    

if __name__ == "__main__":
    unittest.main()