import random

from piperabm.society.actions.action import Move, Stay
from piperabm.tools.symbols import SYMBOLS


class DecisionMaking:

    def select_top_destination(self, agent_id: int, destinations: list, is_market: bool):
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
    
    def destination_score(self, agent_id, destination_id, is_market: bool):
        travel_duration = self.estimated_duration(agent_id, destination_id)
        fuel_food, fuel_water, fuel_energy = self.transportation_fuel(agent_id, duration=travel_duration)
        # When the agent has enough fuel
        if fuel_food <= self.food(id=agent_id) and \
            fuel_water <= self.water(id=agent_id) and \
            fuel_energy <= self.energy(id=agent_id):
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
    
    def estimated_distance(self, agent_id, destination_id):
        return self.infrastructure.heuristic_paths.estimated_distance(
            id_start=self.get_current_node(id=agent_id),
            id_end=destination_id
        )

    def estimated_duration(self, agent_id, destination_id):
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

    def go_and_comeback_and_stay(self, agent_id, destination_id):
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