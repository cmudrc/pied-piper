import unittest
from copy import deepcopy

from piperabm.society.samples import society_1
from piperabm.unit import Date

from piperabm.agent.brain.decision.move import MovementDecision


class TestBrainClass(unittest.TestCase):

    def setUp(self) -> None:
        self.society = deepcopy(society_1)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        self.society.environment.update(start_date, end_date)

        index = 0
        agent = self.society.get_agent_object(index)
        self.observation = agent.brain.observe(index, self.society.environment, self.society)
        self.decision = MovementDecision()