import unittest
import numpy as np

from action import Action
from tools import date, dt
from transportation import Foot
from settlement import Settlement


class TestActionClass(unittest.TestCase):
    s_1 = Settlement(
        name='settlement_1',
        pos=[0, 0],
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )

    s_2 = Settlement(
        name='settlement_2',
        pos=[1000, 0],
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 0.5
        }
    )

    a = Action(
        start_date=date(2020, 1, 1),
        start_point='settlement_1',
        end_point='settlement_2',
        transportation=Foot()
    )

    def test_update(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        self.assertListEqual(self.a.start_pos, self.s_1.pos)
        self.assertListEqual(self.a.end_pos, self.s_2.pos)

    def test_total_displacement_vector(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        self.assertListEqual(list(self.a.total_displacement_vector()), self.s_2.pos)

    def test_direction_vector(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        self.assertListEqual(list(self.a.direction_vector()), [1, 0])

    def test_travel_duration(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        self.assertEqual(self.a.travel_duration().seconds, 720)

    def test_pos_0(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        date = self.a.start_date - dt(hours=1)
        self.assertListEqual(list(self.a.pos(date)), self.s_1.pos)

    def test_pos_1(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        date = self.a.start_date + dt(seconds=360)
        self.assertListEqual(list(self.a.pos(date)), [500, 0])

    def test_pos_2(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        date = self.a.start_date + dt(hours=1)
        self.assertListEqual(list(self.a.pos(date)), self.s_2.pos)