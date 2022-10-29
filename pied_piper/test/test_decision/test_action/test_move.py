import unittest
from copy import deepcopy

from decision import Move
from tools import date, dt
from tools.path import Path
from transportation import Foot


class TestMoveClass(unittest.TestCase):
    
    path = Path()
    path.add(pos=[0, 0])
    path.add(pos=[0, 3])
    path.add(pos=[4, 3])

    m = Move(
        start_date=date(2020, 1, 1),
        path=path,
        transportation=Foot(),
        instant=True
    )
    '''
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

    def test_progress_instant_0(self):
        m = deepcopy(self.m)
        m.instant = True
        time = m.start_date - dt(seconds=1)
        progress = m.progress(time)
        self.assertEqual(progress, 0)

    def test_progress_instant_1(self):
        m = deepcopy(self.m)
        m.instant = True
        time = m.start_date + dt(seconds=1)
        progress = m.progress(time)
        self.assertEqual(progress, 1)
    
    def test_action_duration(self):
        m = deepcopy(self.m)
        m.path.add(pos=[0, 0])
        duration = m.action_duration()
        self.assertAlmostEqual(duration.seconds, 8, places=1)

    def test_action_duration_instant(self):
        m = deepcopy(self.m)
        m.instant = True
        duration = m.action_duration()
        self.assertAlmostEqual(duration.seconds, 0, places=1)
    '''