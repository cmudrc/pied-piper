import random

from piperabm.society.actions.action import Move, Stay
from piperabm.tools.symbols import SYMBOLS


class DecisionMaking:
    """
    Methods related to agents' decision-making
    """

    def select_top_destination(self, agent_id: int, destinations: list, is_market: bool):
        """
        Select top destination
        """
        result = []
        for node_id in destinations:
            score = self.destination_score(agent_id, destination_id=node_id, is_market=is_market)
            if score is not None:
                result.append([node_id, score])
        max_score = max(node[1] for node in result)
        top_nodes = [node for node in result if node[1] == max_score]
        selected_node = random.choice(top_nodes)
        top_node = selected_node[0]
        top_score = selected_node[1]
        return top_node, top_score
    
    def destination_score(self, agent_id, destination_id, is_market: bool) -> float:
        """
        Destination score
        """
        travel_duration = self.estimated_duration(agent_id, destination_id)
        fuel_food = self.get_transportation_fuel_rate(id=agent_id, name='food') * travel_duration
        fuel_water = self.get_transportation_fuel_rate(id=agent_id, name='water') * travel_duration
        fuel_energy = self.get_transportation_fuel_rate(id=agent_id, name='energy') * travel_duration
        
        # When the agent has enough fuel
        if fuel_food <= self.get_resource(id=agent_id, name='food') and \
            fuel_water <= self.get_resource(id=agent_id, name='water') and \
            fuel_energy <= self.get_resource(id=agent_id, name='energy'):
            fuel_value_food = fuel_food * self.food_price
            fuel_value_water = fuel_water * self.water_price
            fuel_value_energy = fuel_energy * self.energy_price
            total_fuel_value = fuel_value_food + fuel_value_water + fuel_value_energy
        else:
            total_fuel_value = SYMBOLS['inf']
        #print(total_fuel_value)
        
        # Calculate the value of resources there
        food_there, water_there, energy_there = self.resources_in(node_id=destination_id, is_market=is_market)
        total_value_there = (food_there * self.food_price) + \
                            (water_there * self.water_price) + \
                            (energy_there * self.energy_price)
        #print(total_value_there)
        
        return total_value_there - total_fuel_value
    
    def estimated_distance(self, agent_id, destination_id) -> float:
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
        speed = self.get_transportation_speed(id=agent_id)
        return estimated_distance / speed
    
    def path(self, agent_id: int, destination_id: int) -> list:
        """
        Path finding for agents
        """
        result = None
        id_start = self.get_current_node(id=agent_id)
        if id_start is not None:
            result = self.infrastructure.path(
                id_start=id_start,
                id_end=destination_id
            )
        return result

    def go_and_comeback_and_stay(self, agent_id, destination_id) -> None:
        """
        A complete daily cycle of choosing and going to a destination, waiting there for trade, and coming back home
        """
        path = self.path(agent_id, destination_id)
        if path is not None:
            action_queue = self.actions[agent_id]
            # Go
            move_go = Move(
                action_queue=action_queue,
                path=path,
                usage=1
            )
            action_queue.add(move_go)
            # Stay (destination)
            stay_length = self.get_max_time_outside(id=agent_id) - (2 * move_go.total_duration)
            stay = Stay(
                action_queue=action_queue,
                duration=stay_length
            )
            action_queue.add(stay)
            # Comeback
            move_back = move_go.reverse()
            action_queue.add(move_back) 
            # Stay (home)
            stay_length = (24 * 60 * 60) - action_queue.total_duration
            stay = Stay(
                action_queue=action_queue,
                duration=stay_length
            )
            action_queue.add(stay)


if __name__ == "__main__":

    from piperabm.infrastructure.samples import model_1 as model

    model.society.add_agent(
        home_id=1,
        id=1
    )
    #print(model.society.get_current_node(id=1))
    #print(model.society.estimated_distance(agent_id=1, destination_id=2))
    #print(model.society.estimated_duration(agent_id=1, destination_id=2))
    print(model.society.destination_score(agent_id=1, destination_id=1, is_market=False))
