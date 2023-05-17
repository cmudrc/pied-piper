import unittest
from copy import deepcopy

from piperabm.actions.queue import Queue
from piperabm.actions.queue.samples import queue_0
from piperabm.actions.action import Action


class TestQueueClass(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = deepcopy(queue_0)

    def test_current(self):
        current_actions = self.queue.current
        self.assertEqual(len(current_actions), 1)

    def test_history(self):
        completed_actions = self.queue.history
        self.assertEqual(len(completed_actions), 0)

    def test_break_index(self):
        self.assertEqual(self.queue.break_index, 0)

        action = self.queue(0)
        action.done = True
        self.assertEqual(self.queue.break_index, 1)

        action = Action()
        self.queue.add(action)
        self.assertEqual(self.queue.break_index, 1)

        action = self.queue(1)
        action.done = True
        action = Action()
        self.queue.add(action)
        self.assertEqual(self.queue.break_index, 2)

        action = self.queue(2)
        action.done = True
        self.assertEqual(self.queue.break_index, 3)

    def test_dict(self):
        dictionary = self.queue.to_dict()
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
        self.assertListEqual(dictionary, expected_result)
        queue = Queue()
        queue.from_dict(dictionary)
        self.assertEqual(queue, self.queue)


if __name__ == "__main__":
    unittest.main()