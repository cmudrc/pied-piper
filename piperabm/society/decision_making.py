import numpy as np

from piperabm.society.actions.action import Move, Stay
from piperabm.tools.symbols import SYMBOLS


class DecisionMaking:
    """
    Methods related to agents' decision-making
    """

    def possible_search_destinations(self, agent_id: int) -> list:
        """
        Return possible search destinations which are NOT market nodes
        """
        result = set()
        # Friends
        friends = self.ego(id=agent_id, type='friend')
        friends_homes = []
        for friend in friends:
            friends_homes.append(self.get_home_id(id=friend))
        result |= set(friends_homes)
        # Neighbors
        neighbors = self.ego(id=agent_id, type='neighbor')
        neighbors_homes = []
        for neighbor in neighbors:
            neighbors_homes.append(self.get_home_id(id=neighbor))
        result |= set(neighbors_homes)
        return list(result)

    def select_top_destination(self, agent_id: int, destinations: list, is_market: bool):
        """
        Select top destination
        """
        if len(destinations) > 0:
            result = []
            for node_id in destinations:
                score = self.destination_score(agent_id, destination_id=node_id, is_market=is_market)
                if score is not None:
                    result.append([node_id, score])
            max_score = max(node[1] for node in result)
            top_nodes = [node for node in result if node[1] == max_score]
            random_index = np.random.choice(len(top_nodes))
            selected_node = top_nodes[random_index]
            top_node = selected_node[0]
            top_score = selected_node[1]
        else:
            top_node, top_score = None, None
        return top_node, top_score
    
    def destination_score(self, agent_id, destination_id, is_market: bool) -> float:
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
    
    def path(self, agent_id: int, destination_id: int) -> list:
        """
        Path finding for agents
        """
        result = None
        if destination_id is not None:
            id_start = self.get_current_node(id=agent_id)
            if id_start is not None:
                result = self.infrastructure.path(
                    id_start=id_start,
                    id_end=destination_id
                )
        return result

    def go_and_comeback_and_stay(self, agent_id: int, destination_id: int) -> None:
        """
        A complete daily cycle of choosing and going to a destination, waiting there for trade, and coming back home
        """
        path = self.path(agent_id, destination_id)
        if path is not None:
            critical_stay_length = 0
            action_queue = self.actions[agent_id]
            # Go
            move_go = Move(
                action_queue=action_queue,
                path=path,
                usage=1
            )
            action_queue.add(move_go)
            # Stay (destination)
            stay_length = self.max_time_outside - (2 * move_go.total_duration)
            if stay_length < critical_stay_length:
                stay_length = critical_stay_length
            stay = Stay(
                action_queue=action_queue,
                duration=stay_length
            )
            action_queue.add(stay)
            # Comeback
            move_back = move_go.reverse()
            action_queue.add(move_back) 
            # Stay (home)
            stay_length = self.activity_cycle - action_queue.total_duration
            if stay_length < critical_stay_length:
                stay_length = critical_stay_length
            stay = Stay(
                action_queue=action_queue,
                duration=stay_length
            )
            action_queue.add(stay)

    def decide_destination(self, id: int) -> None:
        """
        Decide the destination
        """
        markets = self.infrastructure.markets
        best_destination, _ = self.select_top_destination(agent_id=id, destinations=markets, is_market=True)
        if best_destination is None:  # When market is not available
            # Possible non-market destinations to search
            best_destination, _ = self.select_top_destination(
                agent_id=id,
                destinations=self.possible_search_destinations(agent_id=id),
                is_market=False
            )
        self.go_and_comeback_and_stay(agent_id=id, destination_id=best_destination)


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_1 import model

    agent_id = 0
    home_id = 1
    destination_id = 2
    model.society.add_agent(
        home_id=home_id,
        id=agent_id,
    )
    print("current node: ", model.society.get_current_node(id=agent_id))
    print("possible destinations: ", model.society.possible_search_destinations(agent_id=agent_id))
    print("estimated distance: ", model.society.estimated_distance(agent_id=agent_id, destination_id=destination_id))
    print("estimated duration: ", model.society.estimated_duration(agent_id=agent_id, destination_id=destination_id))
    print("destination score: ", model.society.destination_score(agent_id=agent_id, destination_id=destination_id, is_market=True))
    print("path: ", model.society.path(agent_id=agent_id, destination_id=destination_id))

