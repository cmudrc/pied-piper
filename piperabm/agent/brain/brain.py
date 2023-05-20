from piperabm.agent.brain.decision import Move, Trade
from piperabm.object import Object


class Brain(Object):

    def __init__(self):
        pass

    def observe(self):
        observation = {}
        return observation
    
    def decide(self):
        pass



if __name__ == "__main__":
    brain = Brain()
    print(brain)