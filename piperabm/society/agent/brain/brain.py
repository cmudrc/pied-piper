from piperabm.object import PureObject
from piperabm.actions import Move, Stay


class Brain(PureObject):

    def __init__(self, agent):
        self.agent = agent
    
    @property
    def model(self):
        return self.agent.model
    
    @property
    def current_node(self):
        return self.agent.current_node
    
    @property
    def queue(self):
        return self.agent.queue

    @property
    def idle(self):
        """
        Check if the agent is idle
        """
        return self.queue.done

    def observe(self):
        self.infrastructure = self.model.infrastructure
        self.paths = self.infrastructure.paths
        self.society = self.model.society

    def decide(self):
        if self.idle is True:
            # Observe
            self.observe()
            # Choose destination
            destination = self.best_destination()
            # Create actions
            actions = []
            self.queue.add(actions)

    def possible_destinations(self):
        return self.paths.destinations(self.current_node, type='all')
    
    def best_destination(self):
        destinations = self.possible_destinations()
        destination = destinations[0] ##########
        return destination
    
    def destination_score(self, id):
        adjusted_distance = self.paths.adjusted_length(
            id_start = self.current_node,
            id_end = id
        )
        resources_value = 0
        return resources_value / adjusted_distance


if __name__ == "__main__":
    pass