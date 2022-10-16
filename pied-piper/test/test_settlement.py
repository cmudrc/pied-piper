import unittest

from settlement import Settlement
from agent import Agent


class TestRoadClass(unittest.TestCase):
    def test_add_agent(self):
        a = Agent(
            name='John',
            pos=[1, 1]
        )
        s = Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        )
        s.add_agent(a)
        self.assertListEqual(s.pos, a.pos, msg="position should be equal")

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
        a = s.find_element(s.agents[0], all_agents)
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
        