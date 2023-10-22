from piperabm.agent.brain.decision.decision import Decision
from piperabm.actions import Move, Stay
from piperabm.unit import DT


class MovementDecision(Decision):

    def decide(self, observation: dict):
        action = None
        decision_go_or_stay = self.go_or_stay(observation)
        if decision_go_or_stay == 'go':
            action = self.where_to_go(observation)
        elif decision_go_or_stay == 'stay':
            action = self.how_long_stay(observation)
        return action

    def go_or_stay(self):
        """
        Should agent move to another location or stay?
        """
        result = None
        path = self.find_best_destination()
        pass

    def find_best_destination(self, observation):
        """
        Where is the best suitable destination?
        """
        ''' list all possible destinations '''
        path_graph = observation['map']
        destinations = path_graph.all_indexes()
        ''' remove current node '''
        society = observation['society']
        index = observation['index']
        current_node = society.current_node(index)
        destinations.remove(current_node)
        ''' score destinations '''
        scores = []
        for destination in destinations:
            score = self.destionation_score(observation, destination)
            scores.append(score)
        ''' sort based on score '''
        destinations = [destination for _, destination in sorted(zip(scores, destinations))]
        ''' pick the best destination '''
        path = destinations[0]
        return path
    
    def destionation_score(self, observation, destination):
        """
        Calculate score of each destination
        """
        result = None
        start_date = observation['start_date']
        environment = observation['environment']
        agent_index = observation['index']
        agent = environment.society.get_agent_object(agent_index)
        transportation = agent.transportation
        path = self.find_path(destination)
        action = Move(
            start_date=start_date,
            path=path,
            transportation=transportation,
            environment=environment,
            agent_index=agent_index,
        )
        benefit = 0 ##############
        result = benefit / action.total_fuel
        return result

    def where_to_go(self, observation):
        """
        Where should agent go next?
        """
        start_date = observation['start_date']
        environment = observation['environment']
        agent_index = observation['index']
        agent = environment.society.get_agent_object(agent_index)
        transportation = agent.transportation
        path = self.find_best_destination()
        action = Move(
            start_date=start_date,
            path=path,
            transportation=transportation,
            environment=environment,
            agent_index=agent_index
        )
        return action

    def how_long_stay(self, observation):
        """
        How long should agent stay?
        """
        start_date = observation['start_date']
        environment = observation['environment']
        agent_index = observation['index']
        action = Stay(
            start_date=start_date,
            duration=DT(days=1),
            environment=environment,
            agent_index=agent_index
        )
        return action