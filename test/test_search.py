from gettext import find
import unittest

from piperabm.agent import Agent
from piperabm.search import find_element


class TestFindElementFunc(unittest.TestCase):

    a_1 = Agent(name='agent_1')
    a_2 = Agent(name='agent_2')
    all_agents = [a_1, a_2]

    def test_find_element_0(self):
        agent = find_element(self.a_1.name, all_elements=self.all_agents)
        self.assertEqual(self.a_1.name, agent.name)

    def test_find_element_1(self):
        agent = find_element('blah blah', all_elements=self.all_agents)
        self.assertIsNone(agent)


if __name__ == "__main__":
    unittest.main()