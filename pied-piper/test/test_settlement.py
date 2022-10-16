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
        