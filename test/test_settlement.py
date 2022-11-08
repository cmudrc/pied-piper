import unittest
from copy import deepcopy

from pr.settlement import Settlement
from pr.agent import Agent
from pr.tools import find_element


class TestRoadClass(unittest.TestCase):

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

    def test_add_agent(self):
        s = deepcopy(self.s)
        a = deepcopy(self.a_1)
        s.add_agent(a)
        self.assertEqual(len(self.agents), 1)

    def test_find_agents_by_pos_0(self):
        all_agents = [
            Agent(
                name='John',
                pos=[1, 1]
            ),
            Agent(
                name='Betty',
                pos=[0.5, 0.5]
            )
        ]
        s = Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        )
        s.find_all_agents_by_pos(all_agents)
        self.assertListEqual(s.agents, ['Betty'], msg='only "Betty" remains')

    def test_find_agents_by_pos_1(self):
        all_agents = [
            Agent(
                name='John',
                pos=[1, 1]
            ),
            Agent(
                name='Betty',
                pos=[0.5, 0.5]
            )
        ]
        s = Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        )
        s.find_all_agents_by_pos(all_agents)
        a = find_element(s.agents[0], all_agents)
        self.assertEqual(a.settlement, 'home_1', msg='they both has to be the same')

    def test_find_agents_by_settlement(self):
        all_agents = [
            Agent(
                name='John',
                pos=[1, 1],
                settlement='home_1'
            ),
            Agent(
                name='Betty',
                pos=[0.5, 0.5],
                settlement='home_1'
            )
        ]
        s = Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        )
        s.find_all_agents_by_settlement(all_agents)
        self.assertListEqual(s.agents, ['John', 'Betty'], msg='both "John" and "Betty" are in')

    def test_find_agents_by_both_settlement_pos(self):
        all_agents = [
            Agent(
                name='John',
                pos=[1, 1],
                settlement='home_1'
            ),
            Agent(
                name='Betty',
                pos=[0.5, 0.5]
            )
        ]
        s = Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        )
        s.update(all_agents)
        self.assertListEqual(s.agents, ['Betty', 'John'], msg='both "John" and "Betty" are in')
        
    def test_road_length_calc(self):
        all_agents = [
            Agent(
                name='John',
                pos=[1, 1]
            ),
            Agent(
                name='Betty',
                pos=[1, 1]
            )
        ]
        s = Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        )
        s.add_agents(all_agents)


if __name__ == "__main__":
    unittest.main()
        