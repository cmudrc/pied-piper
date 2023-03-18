import unittest

from piperabm import Environment
from piperabm import Society
from piperabm.economy import Exchange
from piperabm.resource import Resource
from piperabm.unit import Date, DT
from piperabm.society.decision import Decision


class TestDecisionClass(unittest.TestCase):

    def setUp(self):
        env = Environment(links_unit_length=10)
        env.add_settlement(name="Settlement 1", pos=[-60, 40])
        env.add_settlement(name="Settlement 2", pos=[200, 20])
        env.add_settlement(name="Settlement 3", pos=[100, -180])
        env.add_link(start="Settlement 1", end=[0, 0])
        env.add_link(start=[0.1, 0.1], end=[80, 60])
        env.add_link(start=[80, 60], end=[200, 20])
        env.add_link(start=[0, 0], end="Settlement 3")

        gini = 0.3
        
        exchange_rate = Exchange()
        exchange_rate.add('food', 'wealth', 10)
        exchange_rate.add('water', 'wealth', 2)
        exchange_rate.add('energy', 'wealth', 4)
        soc = Society(env, gini=gini, exchange_rate=exchange_rate)
        average_resource = Resource(
            current_resource={
                'food': 20,
                'water': 40,
                'energy': 60,
            },
            max_resource={
                'food': 100,
                'water': 200,
                'energy': 300,
            }
        )
        average_income = 1000
        soc.generate_agents(
            n=5,
            average_resource=average_resource,
            average_income=average_income
        )
        agents = soc.all_agents()
        start_date = Date.today() + DT(days=1)
        end_date = start_date + DT(days=1)
        path_graph = soc.env.to_path_graph(start_date, end_date)
        self.decision = Decision(path_graph, soc, agents[0])

    def test_possible_routes(self):
        routes = self.decision.possible_routes()
        for i, _ in enumerate(routes):
            if i > 0:
                start_0 = routes[0][0]
                start_other = routes[i][0]
                self.assertEqual(start_0, start_other) 

    def test_select_best_route(self):
        route = self.decision.select_best_route()
        #print(route)
        '''
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        start_date = Date.today() + DT(days=1)
        end_date = start_date + DT(days=1)
        decision = Decision(path, self, index)
        route = soc.select_best_route(agents[0], start_date, end_date)
        self.assertEqual(len(route), 2)
        '''
    

if __name__ == "__main__":
    unittest.main()