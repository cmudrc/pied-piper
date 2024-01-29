import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.society import Agent
from piperabm.actions import Move


class TestTrackClass(unittest.TestCase):

    def setUp(self):
        self.model = Model(
            proximity_radius=1,  # Meters
            step_size=100,  # Seconds
            average_income=100,  # Dollars per month
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

        infrastructure = self.model.infrastructure
        nodes = infrastructure.all_nodes(type='settlement')
        index_start, _ = infrastructure.find_nearest_node(self.pos_start, items=nodes)
        index_end, _ = infrastructure.find_nearest_node(self.pos_end, items=nodes)
        path = infrastructure.find_path(index_start, index_end)
        action = Move(path)

        agent = Agent(name="Mr. Sample", balance=100)
        agent.home = index_start
        self.model.add(agent)
        
        self.model_idle = deepcopy(self.model)  # Agent won't move

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
        self.assertEqual(agent.balance, 100)
        self.assertEqual(agent.resources('food'), agent_idle.resources('food'))
        self.assertEqual(road.degradation.current, 0)

        # Run the model
        self.model.run(100, report=False)
        self.model_idle.run(100, report=False)

        # Tests after run
        self.assertListEqual(agent.pos, self.pos_end)
        self.assertLess(100, agent.balance)
        self.assertLess(agent.resources('food'), agent_idle.resources('food'))
        self.assertLess(road_idle.degradation.current, road.degradation.current)

        #self.model.show()
        #self.model_idle.show()
    
    
if __name__ == '__main__':
    unittest.main()