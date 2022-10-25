import unittest

from agent import Move
from tools import date, dt
from transportation import Foot
from tools.path import Path

class TestMoveClass(unittest.TestCase):
    
    path = Path()
    path.add(pos=[0, 0])
    path.add(pos=[0, 3])
    path.add(pos=[4, 3])

    m = Move(
        start_date=date(2020, 1, 1),
        path=path,
        transportation=Foot()
    )
    
    def test_progress_0(self):
        time = self.m.start_date + dt(seconds=100)
        progress = self.m.progress(time)
        self.assertEqual(progress, 1)

    def test_progress_1(self):
        time = self.m.start_date + dt(seconds=1)
        progress = self.m.progress(time)
        self.assertAlmostEqual(progress, 0.2, places=1)
    
    def test_progress_2(self):
        time = self.m.start_date - dt(seconds=1)
        progress = self.m.progress(time)
        self.assertEqual(progress, 0)
    
    def test_action_duration(self):
        duration = self.m.action_duration()
        self.assertAlmostEqual(duration.seconds, 5, places=1)
    