import unittest

from piperabm.actions.action import Action
from piperabm.time import DeltaTime, Date


class TestActionClass(unittest.TestCase):

    def setUp(self):
        date_start = Date(2000, 1, 1)
        duration = DeltaTime(days=1)
        self.action = Action(date_start, duration)

    def test_progress(self):
        progress = self.action.progress(date=Date(1999, 12, 30))
        self.assertEqual(progress, 0)
        
        progress = self.action.progress(date=Date(2000, 1, 1)+DeltaTime(hours=12))
        self.assertEqual(progress, 0.5)
        
        progress = self.action.progress(date=Date(2000, 1, 2))
        self.assertEqual(progress, 1)

    def test_is_current(self):
        date = Date(2000, 1, 1) - DeltaTime(hours=12)
        self.assertFalse(self.action.is_current(date))

        date = Date(2000, 1, 1) + DeltaTime(hours=12)
        self.assertTrue(self.action.is_current(date))

        date = Date(2000, 1, 2) + DeltaTime(hours=12)
        self.assertFalse(self.action.is_current(date))

    def test_serialization(self):
        dictionary = self.action.serialize()
        action = Action()
        action.deserialize(dictionary)
        self.assertEqual(self.action, action)


if __name__ == "__main__":
    unittest.main()