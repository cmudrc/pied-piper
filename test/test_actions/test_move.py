import unittest
from copy import deepcopy

from piperabm.actions import Move
from piperabm.actions.move.tracks import Track, Tracks
from piperabm.society.agent.samples import agent_0
from piperabm.model.samples import model_0
from piperabm.time import Date, DeltaTime


class TestMoveClass_0(unittest.TestCase):

    def setUp(self):
        model = deepcopy(model_0)
        self.agent = deepcopy(agent_0)
        model.add(self.agent)

        track_1 = Track(
            pos_start=[0, 0],
            pos_end=[5000, 0],
            adjustment_factor=1
        )
        track_2 = Track(
            pos_start=[5000, 0],
            pos_end=[5000, 5000],
            adjustment_factor=2
        )
        tracks = Tracks([track_1, track_2])
        date_start = Date(2000, 1, 1)
        self.move = Move(date_start)
        self.move.agent = self.agent
        self.move.add_tracks(tracks)

    def test_pos(self):
        date = Date(2000, 1, 1) + DeltaTime(seconds=-5000)
        pos = self.move.pos(date)
        self.assertListEqual(pos, [0, 0])

        date = Date(2000, 1, 1) + DeltaTime(seconds=1800)
        pos = self.move.pos(date)
        self.assertListEqual(pos, [2500, 0])

        date = Date(2000, 1, 1) + DeltaTime(seconds=7200)
        pos = self.move.pos(date)
        self.assertListEqual(pos, [5000, 2500])

        date = Date(2000, 1, 1) + DeltaTime(seconds=15000)
        pos = self.move.pos(date)
        self.assertListEqual(pos, [5000, 5000])

    def test_update(self):
        self.assertFalse(self.move.done)

        date = Date(2000, 1, 1) + DeltaTime(seconds=-5000)
        self.move.update(date)
        self.assertListEqual(self.agent.pos, [0, 0])
        self.assertFalse(self.move.done)

        date = Date(2000, 1, 1) + DeltaTime(seconds=1800)
        self.move.update(date)
        self.assertListEqual(self.agent.pos, [2500, 0])
        self.assertFalse(self.move.done)

        date = Date(2000, 1, 1) + DeltaTime(seconds=7200)
        self.move.update(date)
        self.assertListEqual(self.agent.pos, [5000, 2500])
        self.assertFalse(self.move.done)

        date = Date(2000, 1, 1) + DeltaTime(seconds=15000)
        self.move.update(date)
        self.assertListEqual(self.agent.pos, [5000, 5000])
        self.assertTrue(self.move.done)

    def test_serialization(self):
        dictionary = self.move.serialize()
        move = Move()
        move.deserialize(dictionary)
        self.assertEqual(self.move, move)


if __name__ == '__main__':
    unittest.main()