import unittest
from copy import deepcopy

from piperabm.actions import Move
from piperabm.transporation.samples import transportation_0 as walk
from piperabm.time import Date
from piperabm.society.agent.samples import agent_0 as agent


class TestMoveClass(unittest.TestCase):

    def setUp(self):
        transporation = walk
        tracks = None #####
        date_start = Date(2000, 1, 1)
        self.move = Move(agent, date_start, tracks, transporation)


if __name__ == "__main__":
    unittest.main()