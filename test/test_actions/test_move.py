import unittest
from copy import deepcopy

from piperabm.unit import Date, DT
from piperabm.actions import Move, Walk


class TestMoveClass(unittest.TestCase):

    m = Move(
        start_date=Date(2020, 1, 1),
        start_pos=[0, 0],
        end_pos=[10000, 10000],
        adjusted_length=20000,
        transportation=Walk()
    )

    def test_move_end_date(self):
        m = deepcopy(self.m)
        self.assertEqual(m.end_date.hour, 5, msg="it must take 5 hours.")

    def test_move_progress_0(self):
        m = deepcopy(self.m)
        date = Date(2020, 1, 1)
        self.assertEqual(m.progress(date), 0)

    def test_move_progress_1(self):
        m = deepcopy(self.m)
        date = Date(2020, 1, 2)
        self.assertEqual(m.progress(date), 1)
        #print(m.pos(date=Date(2020, 1, 1)+DT(hours=1)))
    
    def test_move_progress_2(self):
        m = deepcopy(self.m)
        date = Date(2020, 1, 1) + DT(hours=1)
        self.assertAlmostEqual(m.progress(date), 0.18)

if __name__ == "__main__":
    unittest.main()