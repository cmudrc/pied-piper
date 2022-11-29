import unittest
from copy import deepcopy

from piperabm.settlement import Settlement
from piperabm.agent import Agent
from piperabm.tools import find_element


class TestSettlementClass(unittest.TestCase):

    a_1 = Agent(
        name='John',
        pos=[1, 1]
    )
    a_2 = Agent(
        name='Betty',
        pos=[0.5, 0.5]
    )
    all_agents = [a_1, a_2]

    s = Settlement(
        name='home_1',
        pos=[0, 0],
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )

    def test_register_agent(self):
        s = deepcopy(self.s)
        a_1 = deepcopy(self.a_1)
        a_2 = deepcopy(self.a_2)
        s.all_agents = [a_1, a_2]
        self.assertEqual(len(s.find_agents_inside()), 1)
        s.register_agent(a_1.name)
        self.assertEqual(len(s.find_agents_inside()), 1)
        self.assertEqual(len(s.members), 1)
        self.assertEqual(s.members[0], a_1.name)
        self.assertFalse(s.is_in(a_1.pos))

    def test_tunnel_agent(self):
        s = deepcopy(self.s)
        a_1 = deepcopy(self.a_1)
        a_2 = deepcopy(self.a_2)
        s.all_agents = [a_1, a_2]
        self.assertEqual(len(s.find_agents_inside()), 1)
        s.tunnel_agent(a_1.name)
        self.assertEqual(len(s.find_agents_inside()), 2)
        self.assertEqual(len(s.members), 0)
    
    def test_add_agent(self):
        s = deepcopy(self.s)
        a_1 = deepcopy(self.a_1)
        a_2 = deepcopy(self.a_2)
        s.all_agents = [a_1, a_2]
        self.assertEqual(len(s.find_agents_inside()), 1)
        s.add_agent(a_1.name)
        self.assertEqual(len(s.find_agents_inside()), 2)
        self.assertEqual(len(s.members), 1)
        self.assertEqual(s.members[0], a_1.name)
        self.assertTrue(s.is_in(a_1.pos))

    def test_dict_conversion(self):
        s = deepcopy(self.s)
        dictionary = s.to_dict()
        s_new = Settlement()
        s_new.from_dict(dictionary)
        dictionary_new = s_new.to_dict()
        self.assertDictEqual(dictionary, dictionary_new)


if __name__ == "__main__":
    unittest.main()
        