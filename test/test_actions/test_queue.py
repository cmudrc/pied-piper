import unittest

from piperabm.actions.queue import Queue
from piperabm.actions.action import Action
from piperabm.time import Date, DeltaTime


class TestQueueClass(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()
        action_1 = Action(
            date_start=Date(2000, 1, 1),
            duration=DeltaTime(days=1)
        )
        action_2 = Action(
            date_start=Date(2000, 1, 2),
            duration=DeltaTime(days=1)
        )
        action_3 = Action(
            date_start=Date(2000, 1, 3),
            duration=DeltaTime(days=1)
        )
        actions = [action_1, action_2, action_3]
        self.queue.add(actions)

    def test_filter_actions(self):
        actions = self.queue.filter_actions(done=False)
        self.assertEqual(len(actions), 3)

        self.queue.library[0].done = True

        actions = self.queue.filter_actions(done=False)
        self.assertEqual(len(actions), 2)

    def test_current(self):
        date = Date(2000, 1, 1) - DeltaTime(hours=12)
        action = self.queue.current(date)
        self.assertEqual(action, None)

        date = Date(2000, 1, 2) + DeltaTime(hours=12)
        action = self.queue.current(date)
        self.assertEqual(action, self.queue.library[1])

        date = Date(2000, 1, 4) + DeltaTime(hours=12)
        action = self.queue.current(date)
        self.assertEqual(action, None)


if __name__ == "__main__":
    unittest.main()