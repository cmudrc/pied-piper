import unittest
from copy import deepcopy

from piperabm.actions.queue import Queue
#from piperabm.agent.samples import agent_0
#from piperabm.environment.samples import environment_1
#from piperabm.society import Society
from piperabm.actions.move.samples import move_0
from piperabm.actions.action import Action
from piperabm.unit import Date
from piperabm.society.samples import society_2


class TestQueueClass(unittest.TestCase):

    def setUp(self) -> None:
        '''
        env = deepcopy(environment_1)
        society = Society(environment=env)
        agent = deepcopy(agent_0)
        society.add_agent_object(agent)
        move = deepcopy(move_0)
        agent.queue.add(move)
        print(agent.society)
        '''
        self.society = deepcopy(society_2)
        agent = self.society.get_agent_object(0)
        move = deepcopy(move_0)
        agent.queue.add(move)

    def test_current(self):
        agent = self.society.get_agent_object(0)
        current_actions = agent.queue.current
        self.assertEqual(len(current_actions), 1)

    def test_history(self):
        agent = self.society.get_agent_object(0)
        completed_actions = agent.queue.history
        self.assertEqual(len(completed_actions), 0)

    def test_end_date(self):
        agent = self.society.get_agent_object(0)
        self.assertEqual(agent.queue.end_date.second, 37)

    def test_break_index(self):
        agent = self.society.get_agent_object(0)
        self.assertEqual(agent.queue.break_index, 0)

        action = agent.queue(0)
        action.done = True
        self.assertEqual(agent.queue.break_index, 1)

        action = Action()
        agent.queue.add(action)
        self.assertEqual(agent.queue.break_index, 1)

        action = agent.queue(1)
        action.done = True
        action = Action()
        agent.queue.add(action)
        self.assertEqual(agent.queue.break_index, 2)

        action = agent.queue(2)
        action.done = True
        self.assertEqual(agent.queue.break_index, 3)

    def test_pos(self):
        agent = self.society.get_agent_object(0)
        print(agent.queue.society)
        ''' before movement '''
        date = Date(
            year=2020,
            month=1,
            day=4,
            hour=23,
            minute=0,
            second=0
        )
        pos = agent.queue.pos(date)
        expected_result = [-2, -2]
        self.assertListEqual(pos, expected_result)
        ''' during movement '''
        date = Date(
            year=2020,
            month=1,
            day=5,
            hour=0,
            minute=0,
            second=20
        )
        pos = agent.queue.pos(date)
        expected_result = [20.0, 3.7913703703703705]
        self.assertListEqual(pos, expected_result)
        ''' during movement '''
        date = Date(
            year=2020,
            month=1,
            day=5,
            hour=0,
            minute=0,
            second=30
        )
        pos = agent.queue.pos(date)
        expected_result = [20.0, 13.05062962962963]
        self.assertListEqual(pos, expected_result)
        ''' after movement '''
        date = Date(
            year=2020,
            month=1,
            day=5,
            hour=0,
            minute=0,
            second=40
        )
        pos = agent.queue.pos(date)
        expected_result = [20.0, 20]
        self.assertListEqual(pos, expected_result)

    def test_dict(self):
        agent = self.society.get_agent_object(0)
        dictionary = agent.queue.to_dict()
        expected_result = [
            {
                'start_date': {'year': 2020, 'month': 1, 'day': 5, 'hour': 0, 'minute': 0, 'second': 0},
                'end_date': {'year': 2020, 'month': 1, 'day': 5, 'hour': 0, 'minute': 0, 'second': 37},
                'duration': 37.50532,
                'done': False,
                'type': 'move',
                'path': [(0, 2), (2, 1)],
                'transportation': {'name': 'foot', 'speed': 1.3888888888888888, 'fuel_rate': {'food': 2.3148148148148147e-05, 'water': 1.1574074074074073e-05, 'energy': 0.0}}
            }
        ]
        self.maxDiff = None
        self.assertListEqual(dictionary, expected_result)
        queue = Queue()
        queue.from_dict(dictionary)
        self.assertEqual(queue, agent.queue)


if __name__ == "__main__":
    unittest.main()