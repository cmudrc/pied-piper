from piperabm.agent.brain.decision import MovementDecision, TradingDecision
from piperabm.object import Object


class Brain(Object):

    def __init__(self):
        self.decisions = {
            'movement': MovementDecision(),
            'trading': TradingDecision()
        }
        self.observation = None

    def observe(self, agent_index, environment, society) -> dict:
        """
        Agent observe itself, environment and the society
        """
        observation = {
            'index': agent_index,
            'map': environment.current.to_path_graph(),
            'self': None,
            'others': None,
        }
        self.observation = observation
        return observation
    
    def decide(self):
        actions = []
        actions.append(self.decisions['movement'].decide(self.observation))
        actions.append(self.decisions['trading'].decide(self.observation))
        return actions


if __name__ == "__main__":
    brain = Brain()
    print(brain)