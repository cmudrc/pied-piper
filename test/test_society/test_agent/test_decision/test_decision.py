import unittest
from copy import deepcopy

from piperabm.society.sample import sample_society_0
from piperabm.unit import Date


class TestDecisionClass(unittest.TestCase):

    def setUp(self):
        society = deepcopy(sample_society_0)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 10)
        society.env.update_elements(start_date, end_date)
        
        agent_0 = society.find_agent(agent_info=0)
        agent_0.observe(society)
        agent_1 = society.find_agent(agent_info=1)
        agent_1.observe(society)

        self.society = society

    def test_routes(self):
        agent = self.society.find_agent(agent_info=0)
        #print(agent)
        routes = agent.possible_routes()
        route = agent.select_best_route()
        self.assertListEqual(routes, [route])
        #print(routes) # [(0, 1)]
        #print(route) # (0, 1)
        route_score = agent.calculate_route_score(route)
        #print(route_score)

        agent = self.society.find_agent(agent_info=1)
        #print(agent)
        routes = agent.possible_routes()
        route = agent.select_best_route()
        self.assertListEqual(routes, [route])
        #print(routes) # [(1, 0)]
        #print(route) # (1, 0)
        route_score = agent.calculate_route_score(route)
        #print(route_score)

    def test_decide_action(self):
        agent = self.society.find_agent(agent_info=0)
        #print(agent)
        self.assertTrue(agent.queue.is_empty())
        agent.decide_action()
        self.assertFalse(agent.queue.is_empty())

        agent = self.society.find_agent(agent_info=1)
        #print(agent)
        self.assertTrue(agent.queue.is_empty())
        agent.decide_action()
        self.assertFalse(agent.queue.is_empty())
    

if __name__ == "__main__":
    unittest.main()