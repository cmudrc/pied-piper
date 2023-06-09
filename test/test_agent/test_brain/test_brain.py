import unittest
from copy import deepcopy

from piperabm.society.samples import society_1
from piperabm.unit import Date


class TestBrainClass(unittest.TestCase):

    def setUp(self) -> None:
        self.society = deepcopy(society_1)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        self.society.environment.update(start_date, end_date)
        

    def test_observe(self):
        index = 0
        agent = self.society.get_agent_object(index)
        observation = agent.brain.observe(index, self.society.environment, self.society)
        print(observation)
        #observation['map'].show()

    def test_(self):
        pass

    def test_decide(self):
        pass



if __name__ == "__main__":
    unittest.main()