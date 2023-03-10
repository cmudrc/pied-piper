import unittest
from copy import deepcopy

from piperabm import Environment
from piperabm import Society
from piperabm.economy import Exchange
from piperabm.resource import Resource
from piperabm.unit import Date, DT


class TestSocietyClass(unittest.TestCase):

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
        average_income = 1000
        exchange_rate = Exchange()
        exchange_rate.add('food', 'wealth', 10)
        exchange_rate.add('water', 'wealth', 2)
        exchange_rate.add('energy', 'wealth', 4)
        self.soc = Society(env, gini=gini, average_income=average_income, exchange_rate=exchange_rate)
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
        self.soc.add_agents(n=5, average_resource=average_resource)

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
    
    def test_set_agent_info(self):
        soc = deepcopy(self.soc)
        settlement_previous = soc.agent_info(0, 'settlement')
        new_settlment = settlement_previous + 100
        soc.set_agent_info(0, 'settlement', new_settlment)
        settlement = soc.agent_info(0, 'settlement')
        self.assertEqual(new_settlment, settlement)
        
    def test_all_agents_from(self):
        soc = deepcopy(self.soc)
        settlements = self.env.all_nodes("settlement")
        soc.all_agents_from(settlements[0])
        soc.all_agents_from(settlements[1])
        soc.all_agents_from(settlements[2])

    def test_all_agents_in(self):
        soc = deepcopy(self.soc)
        settlements = self.env.all_nodes("settlement")
        soc.all_agents_in(settlements[0])
        soc.all_agents_in(settlements[1])
        soc.all_agents_in(settlements[2])

    def test_all_agents_available(self):
        soc = deepcopy(self.soc)
        settlements = self.env.all_nodes("settlement")
        soc.all_agents_available(settlements[0])
        soc.all_agents_available(settlements[1])
        soc.all_agents_available(settlements[2])

    def test_all_resource_from(self):
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        soc.all_resource_from(agents)
    
    def test_all_max_resource_from(self):
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        soc.all_max_resource_from(agents)

    def test_all_demand_from(self):
        soc = deepcopy(self.soc)
        agents = soc.all_agents()
        soc.all_demand_from(agents)


if __name__ == "__main__":
    unittest.main()