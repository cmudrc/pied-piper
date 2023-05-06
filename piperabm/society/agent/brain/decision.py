from piperabm.society.agent.brain.relocation import Relocation
from piperabm.society.agent.brain.trade import Trade


class Decision:

    def observe(self, environment, society) -> dict:
        """
        Agent observe itself, environment and the society
        """
        observation = {}
        print("NOT IMPLEMENTED YET")
        return observation
    
    def decide(self, observation: dict):
        print("NOT IMPLEMENTED YET")