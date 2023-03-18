import unittest
from copy import deepcopy

from piperabm import Environment
from piperabm import Society, Agent
from piperabm.economy import Exchange
from piperabm.resource import Resource
from piperabm.unit import Date, DT
from piperabm.environment.sample import env_1 as env


class TestSocietyClass(unittest.TestCase):

    def setUp(self):
        '''
        env = Environment(links_unit_length=10)
        env.add_settlement(name="Settlement 1", pos=[-60, 40])
        env.add_settlement(name="Settlement 2", pos=[200, 20])
        env.add_settlement(name="Settlement 3", pos=[100, -180])
        env.add_link(start="Settlement 1", end=[0, 0])
        env.add_link(start=[0.1, 0.1], end=[80, 60])
        env.add_link(start=[80, 60], end=[200, 20])
        env.add_link(start=[0, 0], end="Settlement 3")
        '''

        gini = 0.3
        exchange_rate = Exchange()
        exchange_rate.add('food', 'wealth', 10)
        exchange_rate.add('water', 'wealth', 2)
        exchange_rate.add('energy', 'wealth', 4)

        soc = Society(env, gini=gini, exchange_rate=exchange_rate)
        
        settlements = env.all_nodes(type='settlement')
        resource_0 = Resource(
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
        agent_0 = Agent(
            name='John',
            origin_node=settlements[0],
            resource=resource_0,
            balance=100
        )
        resource_1 = Resource(
            current_resource={
                'food': 40,
                'water': 80,
                'energy': 120,
            },
            max_resource={
                'food': 100,
                'water': 200,
                'energy': 300,
            }
        )
        agent_1 = Agent(
            name='Robert',
            origin_node=settlements[1],
            resource=resource_1,
            balance=200
        )
        soc.add([agent_0, agent_1])

        self.soc = soc

    def test_show_env(self):
        start_date = Date.today() - DT(days=1)
        end_date = start_date + DT(days=1)
        #self.soc.env.show(start_date, end_date)

    def test_find_agent_by_index(self):
        index = self.soc._find_agent_by_index(0)
        self.assertEqual(index, 0)

    def test_find_agent_by_name(self):
        index= self.soc._find_agent_by_name('John')
        self.assertEqual(index, 0)

    def test_add_agents(self):
        soc = deepcopy(self.soc)
        self.assertEqual(soc.G.number_of_nodes(), 2)
        average_income = 1000
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
        soc.generate_agents(3, average_resource, average_income)
        self.assertEqual(soc.G.number_of_nodes(), 5)

    def test_agent_info(self):
        soc = deepcopy(self.soc)
        name = soc.agent_info(0, 'name')
        self.assertEqual(name, 'John')
        current_settlement = soc.agent_info('John', 'current_node')
        print(current_settlement)
        name = soc.agent_info(1, 'name')
        self.assertEqual(name, 'Robert')
    
    def test_set_agent_info(self):
        soc = deepcopy(self.soc)
        settlement_previous = soc.agent_info(0, 'current_node')
        new_settlment = settlement_previous + 100
        soc.set_agent_info(0, 'settlement', new_settlment)
        settlement = soc.agent_info(0, 'settlement')
        self.assertEqual(new_settlment, settlement)
        
    def test_all_agents_from(self):
        soc = deepcopy(self.soc)
        settlements = soc.env.all_nodes("settlement")
        result = soc.all_agents_from(settlements[0])
        print(result)
        soc.all_agents_from(settlements[1])
        soc.all_agents_from(settlements[2])

    def test_all_agents_in(self):
        soc = deepcopy(self.soc)
        settlements = soc.env.all_nodes("settlement")
        soc.all_agents_in(settlements[0])
        soc.all_agents_in(settlements[1])
        soc.all_agents_in(settlements[2])

    def test_all_agents_available(self):
        soc = deepcopy(self.soc)
        settlements = soc.env.all_nodes("settlement")
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