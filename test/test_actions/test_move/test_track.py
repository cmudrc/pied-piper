import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.society import Agent
from piperabm.actions import Move
from piperabm.matter import Containers, Matter


class TestTrackClass(unittest.TestCase):

    def setUp(self):
        """ Model """
        food = Matter('food', 5)
        water = Matter('water', 5)
        energy = Matter('energy', 5)
        average_resources = Containers(food, water, energy)
        self.step_size = 100  # Seconds
        self.model = Model(
            proximity_radius=1,  # Meters
            step_size=self.step_size,  # Seconds
            average_income=100,  # Dollars per month
            average_resources=average_resources,
            gini_index=0,
            name="Sample Model"
        )

        self.pos_start = [0, 0]
        self.pos_end = [5000, 0]
        road = Road(
            pos_1=self.pos_start,
            pos_2=self.pos_end,
            roughness=2
        )
        settlement_1 = Settlement(pos=self.pos_start)
        settlement_2 = Settlement(pos=self.pos_end)
        self.model.add(road, settlement_1, settlement_2)
        self.model.apply_grammars()

        """ Create action """
        infrastructure = self.model.infrastructure
        nodes = infrastructure.all_nodes(type='settlement')
        self.index_start, _ = infrastructure.find_nearest_node(self.pos_start, items=nodes)
        self.index_end, _ = infrastructure.find_nearest_node(self.pos_end, items=nodes)
        path = infrastructure.find_path(self.index_start, self.index_end)
        action = Move(path)

        """ Create agent """
        agent = Agent(name="Mr. Sample")
        agent.home = self.index_start
        self.model.add(agent)
        
        self.model_idle = deepcopy(self.model)  # Agent won't move

        """ Add action to agent """
        agents = self.model.all_agents
        agent = self.model.get(agents[0])
        agent.queue.add(action)

    def test_update(self):
        agents_index = self.model.all_agents
        agent_index = agents_index[0]
        edges_index = self.model.all_environment_edges
        edge_index = edges_index[0]
        
        agent = self.model.get(agent_index)
        agent_idle = self.model_idle.get(agent_index)
        road = self.model.get(edge_index)
        road_idle = self.model_idle.get(edge_index)

        # Tests before run
        self.assertListEqual(agent.pos, self.pos_start)
        self.assertAlmostEqual(agent.balance, 200, places=2)
        self.assertEqual(agent.resources('food'), agent_idle.resources('food'))
        self.assertEqual(agent.time_outside.total_seconds(), 0)
        self.assertEqual(agent.current_node, self.index_start)
        self.assertEqual(road.degradation.current, 0)

        # Run the model
        steps = 100
        self.model.run(steps, report=False)
        self.model_idle.run(steps, report=False)

        # Tests after run
        self.assertListEqual(agent.pos, self.pos_end)
        self.assertLess(200, agent.balance)
        self.assertLess(agent.resources('food'), agent_idle.resources('food'))
        self.assertEqual(agent.time_outside.total_seconds(), steps * self.step_size)
        self.assertEqual(agent.current_node, self.index_end)
        self.assertLess(road_idle.degradation.current, road.degradation.current)

        #self.model.show()
        #self.model_idle.show()
    
    
if __name__ == '__main__':
    unittest.main()