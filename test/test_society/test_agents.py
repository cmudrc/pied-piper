import unittest
from copy import deepcopy

from piperabm import Environment
from piperabm import Society
from piperabm.unit import Date, DT


class TestAddFunction(unittest.TestCase):

    env = Environment(links_unit_length=10)
    env.add_settlement(name="Settlement 1", pos=[-60, 40])
    env.add_settlement(name="Settlement 2", pos=[200, 20])
    env.add_settlement(name="Settlement 3", pos=[100, -180])
    env.add_link(start="Settlement 1", end=[0, 0])
    env.add_link(start=[0.1, 0.1], end=[80, 60])
    env.add_link(start=[80, 60], end=[200, 20])
    env.add_link(start=[0, 0], end="Settlement 3")

    soc = Society(env)
    soc.add_agents(5)

    def test_show_env(self):
        soc = deepcopy(self.soc)
        start_date = Date.today() - DT(days=1)
        end_date = start_date + DT(days=1)
        #soc.env.show(start_date, end_date)

    def test_add_agents_0(self):
        soc = deepcopy(self.soc)
        self.assertEqual(soc.G.number_of_nodes(), 5)

    def test_agent_info(self):
        soc = deepcopy(self.soc)
        soc.agent_info(0, 'name') # test function
        soc.agent_info(0, 'settlement') # test function
        soc.agent_info(0, 'queue') # test function
        soc.agent_info(0, 'resource') # test function
        soc.agent_info(0, 'idle_fuel_rate') # test function
        soc.agent_info(0, 'wealth') # test function

    def test_all_agents_from(self):
        soc = deepcopy(self.soc)
        settlements = self.env.all_settlements()
        soc.all_agents_from(settlements[0])
        soc.all_agents_from(settlements[1])
        soc.all_agents_from(settlements[2])

    def test_all_agents_in(self):
        soc = deepcopy(self.soc)
        settlements = self.env.all_settlements()
        soc.all_agents_in(settlements[0])
        soc.all_agents_in(settlements[1])
        soc.all_agents_in(settlements[2])

    def test_all_agents_available(self):
        soc = deepcopy(self.soc)
        settlements = self.env.all_settlements()
        soc.all_agents_available(settlements[0])
        soc.all_agents_available(settlements[1])
        soc.all_agents_available(settlements[2])

    def test_all_resources_from(self):
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        soc.all_resource_from(agents)
    
    def test_all_demand_from(self):
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        soc.all_demand_from(agents)

    def test_possible_routes(self):
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        start_date = Date.today() + DT(days=1)
        end_date = start_date + DT(days=1)
        routes = soc.possible_routes(agents[0], start_date, end_date)
        for i, _ in enumerate(routes):
            if i > 0:
                start_0 = routes[0][0]
                start_other = routes[i][0]
                self.assertEqual(start_0, start_other)

    def test_select_best_route(self):
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        start_date = Date.today() + DT(days=1)
        end_date = start_date + DT(days=1)
        route = soc.select_best_route(agents[0], start_date, end_date)
        self.assertEqual(len(route), 2)


if __name__ == "__main__":
    unittest.main()