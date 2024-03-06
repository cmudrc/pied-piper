from piperabm.object import PureObject
from piperabm.actions import Move, Stay
from piperabm.time import DeltaTime


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
        """
        Observe the surrounding
        """
        self.infrastructure = self.model.infrastructure
        self.paths = self.infrastructure.paths
        self.society = self.model.society

    def decide(self):
        """
        Decide and create new appropriate actions
        """
        if self.idle is True:
            # Observe
            self.observe()
            # Choose destination
            if self.agent.time_outside >= self.agent.max_time_outside:
                # Has to return home
                destination = self.agent.home
            else:
                # Choose a destination outside
                destination = self.best_destination()
            if destination is not None:
                # Create actions
                action_1 = Move(self.paths.path(
                        id_start=self.agent.current_node,
                        id_end=destination
                    )
                )
                action_1.queue = self.queue
                duration = action_1.remaining_time
                stay_duration = self.agent.max_time_outside - duration
                action_2 = Stay(stay_duration)
                actions = [action_1, action_2]
                self.queue.add(actions)

    def possible_destinations(self):
        """
        List all possible destinations for the agent
        """
        return self.paths.destinations(self.current_node, type='all')
    
    def best_destination(self):
        """
        Choose the best destination among the possible destinations
        """
        destination = None
        destinations = self.possible_destinations()
        scores = {}
        for destination in destinations:
            scores[destination] = self.destination_score(id=destination)
        if len(destinations) > 0:
            destination = max(scores, key=scores.get)
        return destination
    
    def destination_score(self, id):
        """
        Score of a certain destination
        """
        adjusted_distance = self.paths.adjusted_length(
            id_start = self.current_node,
            id_end = id
        )
        agents_there = self.society.agents_in(id)
        exchange_rate = self.model.exchange_rate
        resources_value = 0
        for agent_id in agents_there:
            object = self.model.get(agent_id)
            resources_value += object.resources.value(exchange_rate)
        if self.infrastructure.node_type(id) == 'market':
            object = self.model.get(id)
            resources_value += object.resources.value(exchange_rate)
        return resources_value / adjusted_distance


if __name__ == "__main__":
    pass