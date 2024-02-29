from piperabm.object import PureObject


class Brain(PureObject):

    def __init__(self, agent):
        self.agent = agent

    def observe(self):
        self.id = self.agent.id
        self.current_node = self.agent.current_node
        self.model = self.agent.model
        self.infrastructure = self.model.infrastructure
        self.path = self.infrastructure.path
        self.society = self.model.society

    def possible_destinations(self):
        return self.path.destinations(self.current_node, type='all')
    
    def best_destination(self):
        destinations = self.possible_destinations()


if __name__ == "__main__":
    pass