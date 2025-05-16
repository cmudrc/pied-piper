import numpy as np

from piperabm.society.actions.action import Move, Stay
from piperabm.tools.symbols import SYMBOLS


class DecisionMaking:
    """
    Methods related to agents' decision-making
    """

    def preasssumed_destinations(self, agent_id: int) -> list:
        """
        Return preassumed destinations (which are market nodes here)
        """
        result = []
        nodes = self.infrastructure.markets
        for node in nodes:
            path_exists = self.infrastructure.has_path(id_start=self.get_current_node(id=agent_id), id_end=node)
            if path_exists is True:
                result.append(
                    {
                        'id': node,
                        'score': self.destination_score(agent_id=agent_id, destination_id=node, is_market=True)
                    }
                )
        return result
    
    def search_destinations(self, agent_id: int) -> list:
        """
        Return possible search destinations which are NOT market nodes
        """
        result = []
        nodes = set()
        # Friends
        friends = self.ego(id=agent_id, type='friend')
        friends_homes = []
        for friend in friends:
            friends_homes.append(self.get_home_id(id=friend))
        nodes |= set(friends_homes)
        # Neighbors
        neighbors = self.ego(id=agent_id, type='neighbor')
        neighbors_homes = []
        for neighbor in neighbors:
            neighbors_homes.append(self.get_home_id(id=neighbor))
        nodes |= set(neighbors_homes)
        nodes = list(nodes)
        for node in nodes:
            path_exists = self.infrastructure.has_path(id_start=self.get_current_node(id=agent_id), id_end=node)
            if path_exists is True:
                result.append(
                    {
                        'id': node,
                        'score': self.destination_score(agent_id=agent_id, destination_id=node, is_market=False)
                    }
                )
        return result

    def destination_score(self, agent_id: int, destination_id: int, is_market: bool) -> float:
        """
        Destination score
        """
        # Calculate the estimated amount of fuel required
        travel_duration = self.estimated_duration(agent_id, destination_id)
        fuel_resources = {}
        for name in self.resource_names:
            fuel_resources[name] = self.transportation_resource_rates[name] * travel_duration
        # Calculate the value of required fuel
        fuel_possible = True
        for name in self.resource_names:
            if fuel_resources[name] > self.get_resource(id=agent_id, name=name):
                fuel_possible = False
        if fuel_possible is True:
            total_fuel_value = 0
            for name in self.resource_names:
                fuel_value = fuel_resources[name] * self.prices[name]
                total_fuel_value += fuel_value
        else:
            total_fuel_value = SYMBOLS['inf']
        # Calculate the value of resources there
        resources_there = self.resources_in(node_id=destination_id, is_market=is_market)
        total_value_there = 0
        for name in self.resource_names:
            total_value_there += resources_there[name] * self.prices[name]
        # Calculate score
        score = total_value_there - total_fuel_value
        return score
    
    def estimated_distance(self, agent_id: int, destination_id: int) -> float:
        """
        Estimated distance between agent and destination
        """
        return self.infrastructure.heuristic_paths.estimated_distance(
            id_start=self.get_current_node(id=agent_id),
            id_end=destination_id
        )

    def estimated_duration(self, agent_id, destination_id) -> float:
        """
        Estimated duration of reaching a certain destination
        """
        estimated_distance = self.estimated_distance(agent_id, destination_id)
        speed = self.speed
        return estimated_distance / speed

    def decide_destination(self, agent_id: int, duration: float) -> None:
        """
        Decide the destination
        """
        destination_id = None
        critical_stay_length = duration
        action_queue = self.get_action_queue(id=agent_id)
        # Find suitable market
        destinations = self.preasssumed_destinations(agent_id=agent_id)
        destinations = sorted(destinations, key=lambda x: x['score'], reverse=True)
        suitable_destination_found = False
        for destination in destinations:
            path = self.infrastructure.path(
                id_start=self.get_current_node(id=agent_id),
                id_end=destination['id']
            )
            move_go = Move(
                action_queue=action_queue,
                path=path,
                usage=self.transportation_degradation
            )
            # Stay (at the destination)
            stay_length = self.max_time_outside - (2 * move_go.total_duration)
            if stay_length > critical_stay_length:
                suitable_destination_found = True
                destination_id = destination['id']
                break
        if suitable_destination_found is True:
            self.go_and_comeback_and_stay(action_queue, move_go, stay_length)
        elif suitable_destination_found is False:
            destinations = self.search_destinations(agent_id=agent_id)
            destinations = sorted(destinations, key=lambda x: x['score'], reverse=True)
            for destination in destinations:
                path = self.infrastructure.path(
                    id_start=self.get_current_node(id=agent_id),
                    id_end=destination['id']
                )
                move_go = Move(
                    action_queue=action_queue,
                    path=path,
                    usage=self.transportation_degradation
                )
                # Stay (at the destination)
                stay_length = self.max_time_outside - (2 * move_go.total_duration)
                if stay_length > critical_stay_length:
                    suitable_destination_found = True
                    destination_id = destination['id']
                    break
            if suitable_destination_found is True:
                self.go_and_comeback_and_stay(action_queue, move_go, stay_length)
            elif suitable_destination_found is False:
                pass # No suitable destination found
        return destination_id

    def go_and_comeback_and_stay(self, action_queue, move_go, stay_length) -> None:
        """
        A complete daily cycle of choosing and going to a destination, waiting there for trade, and coming back home
        """
        # Move
        action_queue.add(move_go)
        stay_destination = Stay(
            action_queue=action_queue,
            duration=stay_length
        )
        # Stay
        action_queue.add(stay_destination)
        # Move
        move_back = move_go.reverse()
        action_queue.add(move_back) 
        # Stay
        stay_length = self.activity_cycle - action_queue.total_duration
        stay_home = Stay(
            action_queue=action_queue,
            duration=stay_length
        )
        action_queue.add(stay_home)


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_1 import model

    agent_id = 0
    home_id = 1
    destination_id = 2
    model.society.add_agent(
        home_id=home_id,
        id=agent_id,
    )

    print("preassumed destinations: ", model.society.preasssumed_destinations(agent_id=agent_id))
    print("search destinations: ", model.society.search_destinations(agent_id=agent_id))
    print("estimated distance: ", model.society.estimated_distance(agent_id=agent_id, destination_id=destination_id))
    print("estimated duration: ", model.society.estimated_duration(agent_id=agent_id, destination_id=destination_id))
    print("destination score: ", model.society.destination_score(agent_id=agent_id, destination_id=destination_id, is_market=True))
    print("destination id: ", model.society.decide_destination(agent_id=agent_id, duration=100))
    #print(model.society.get_action_queue(id=agent_id))
