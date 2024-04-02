from piperabm.object import PureObject
from piperabm.actions import Move, Stay


class Brain(PureObject):

    def __init__(self, agent):
        self.agent = agent

    @property
    def queue(self):
        return self.agent.queue

    @property
    def society(self):
        return self.agent.society
    
    @property
    def model(self):
        return self.society.model
    
    @property
    def infrastructure(self):
        return self.model.infrastructure
    
    @property
    def current_node(self):
        return self.agent.current_node
    
    @property
    def queue(self):
        return self.agent.queue
    
    @property
    def paths(self):
        return self.model.paths

    def decide(self):
        """
        Decide and create new appropriate actions
        """
        # Choose destination
        if self.agent.time_outside >= self.agent.max_time_outside:
            # Has to return home
            destination = self.agent.home
        else:
            # Choose a destination outside
            destination = self.best_destination()
        
        if destination is not None:
            # Create actions
            action_1 = Move(
                self.paths.path(
                    id_start=self.agent.current_node,
                    id_end=destination
                )
            )
            self.queue.add(action_1)
            duration = action_1.remaining_time
            stay_duration = self.agent.max_time_outside - duration
            action_2 = Stay(stay_duration)
            self.queue.add(action_2)

    def possible_destinations(self):
        """
        List all possible destinations for the agent
        """
        destinations = self.infrastructure.nonjunctions
        destinations.remove(self.current_node)
        # Filter destionations
        destinations = destinations ######
        return destinations
    
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
        exchange_rate = self.society.exchange_rate
        resources_value = 0
        for agent_id in agents_there:
            object = self.society.get(agent_id)
            resources_value += object.resources.value(exchange_rate.prices)
        if self.infrastructure.object_type(id) == 'market':
            object = self.infrastructure.get(id)
            resources_value += object.resources.value(exchange_rate.prices)
        return resources_value / adjusted_distance


if __name__ == "__main__":
    pass