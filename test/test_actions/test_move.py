import unittest
from copy import deepcopy

from piperabm.actions import Move
from piperabm.actions.move.tracks import Track, Tracks
from piperabm.society.agent.samples import agent_0
from piperabm.time import Date


class TestMoveClass(unittest.TestCase):

    def setUp(self):
        agent = deepcopy(agent_0)
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
        self.move = Move(agent, date_start)
        self.move.add_tracks(tracks)

    def test_serialization(self):
        dictionary = self.move.serialize()
        move = Move()
        move.deserialize(dictionary)
        self.assertEqual(self.move, move)


if __name__ == "__main__":
    unittest.main()