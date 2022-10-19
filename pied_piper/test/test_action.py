import unittest

from action import Action
from tools import date
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
        pos=[1, 1],
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
        self.assertListEqual(self.a.end_pos, [1, 1])
        self.assertListEqual(self.a.start_pos, [0, 0])

    def test_(self):
        settlements = [self.s_1, self.s_2]
        self.a.update(settlements)
        self.assertListEqual(self.a.end_pos, [1, 1])