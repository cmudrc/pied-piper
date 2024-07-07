import unittest
from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_0 import model as model_0
from piperabm.infrastructure.samples.infrastructure_1 import model as model_1
from piperabm.infrastructure.samples.infrastructure_2 import model as model_2


class TestDecisionMakingClass_0(unittest.TestCase):
    """
    Normal run
    """
    def setUp(self):
        self.id_agent = 0
        self.id_home = 0
        self.model = deepcopy(model_0)
        self.model.society.add_agent(
            socioeconomic_status=1,
            id=self.id_agent,
            home_id=self.id_home,
            resources={
                'food': 100,
                'water': 100,
                'energy': 100,
            },
            balance=100
        )

    def test_decide(self):
        # Beginning
        queue = self.model.society.actions[self.id_agent]
        self.assertTrue(queue.done) # queue done
        self.assertEqual(len(queue.undones), 0) # queue undones

        # Decide
        self.model.run(n=1, report=False, step_size=50) # run
        self.assertTrue(queue.done) # queue done
        self.assertEqual(len(queue.undones), 0) # queue undones


class TestDecisionMakingClass_1(unittest.TestCase):
    """
    Normal run
    """
    def setUp(self):
        self.id_agent = 0
        self.id_start = 1
        self.id_end = 2
        self.model = deepcopy(model_1)
        self.model.society.add_agent(
            socioeconomic_status=1,
            id=self.id_agent,
            home_id=self.id_start,
            resources={
                'food': 100,
                'water': 100,
                'energy': 100,
            },
            balance=100
        )

    def test_decide(self):
        # Beginning
        queue = self.model.society.actions[self.id_agent]
        self.assertTrue(queue.done) # queue done
        self.assertEqual(len(queue.undones), 0) # queue undones

        # Decide
        self.model.run(n=1, report=False, step_size=50) # run
        self.assertFalse(queue.done) # queue done
        self.assertEqual(len(queue.undones), 4) # queue undones


class TestDecisionMakingClass_2(unittest.TestCase):
    """
    Normal run
    """
    def setUp(self):
        self.id_agents = [11, 12, 13]
        self.id_homes = [1, 2, 3]
        self.id_start = 1
        self.id_end = 2
        self.model = deepcopy(model_2)
        self.model.society.neighbor_radius = 270
        for i in range(len(self.id_agents)):
            self.model.society.add_agent(
                socioeconomic_status=1,
                id=self.id_agents[i],
                home_id=self.id_homes[i],
                resources={
                    'food': 100,
                    'water': 100,
                    'energy': 100,
                },
                balance=100
            )

    def test_possible_search_destinations(self):
        agents = self.model.society.agents
        id_agent = agents[0]
        destinations = self.model.society.possible_search_destinations(agent_id=id_agent)
        self.assertEqual(len(destinations), 1)


if __name__ == "__main__":
    unittest.main()