import unittest
from copy import deepcopy

from piperabm import Environment
from piperabm import Society


class TestAddFunction(unittest.TestCase):

    env = Environment(links_unit_length=10)
    env.add_settlement(name="Settlement 1", pos=[-60, 40])
    env.add_settlement(name="Settlement 2", pos=[200, 20])
    env.add_settlement(name="Settlement 3", pos=[100, -180])
    env.add_link(start="Settlement 1", end=[0, 0])
    env.add_link(start=[0.5, 0.5], end=[80, 60])
    env.add_link(start=[80, 60], end=[200, 20])
    env.add_link(start=[0, 0], end="Settlement 3")

    soc = Society(env)
    soc.add_agents(5)

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
        soc.all_agents_from(settlement=settlements[0])
        soc.all_agents_from(settlement=settlements[1])
        soc.all_agents_from(settlement=settlements[2])


if __name__ == "__main__":
    unittest.main()