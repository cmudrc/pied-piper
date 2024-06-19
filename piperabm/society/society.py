import networkx as nx
import random
from copy import deepcopy
import uuid

#from piperabm.data.agents_info import *
#from piperabm.data.utqiavik.info import *
from piperabm.society.graphics import Graphics
#from piperabm.economy import utility, trade_solver
from piperabm.tools.gini import gini
from piperabm.society.actions import ActionQueue, Move, Stay
from piperabm.tools.symbols import SYMBOLS
from piperabm.tools import nx_serialize, nx_deserialize


class Society(Graphics):

    type = "society"

    def __init__(
            self,
            food_price: float = 1,
            water_price: float = 1,
            energy_price: float = 1,
            average_income: float = average_income,
        ):
        super().__init__()
        self.G = nx.DiGraph()
        self.model = None # Binding
        self.actions = {}
        self.food_price = food_price
        self.water_price = water_price
        self.energy_price = energy_price
        self.average_income = average_income

    @property
    def infrastructure(self):
        result = None
        if self.model is not None:
            result = self.model.infrastructure
        return result
    
    def check_id(self, id):
        if id is None:
            id = self.new_id()
        else:
            if id in self.agents:
                id = self.new_id()
                print("id already exists. replaced with new id.")
        return id

    def new_id(self) -> int:
        return uuid.uuid4().int

    def generate_agents(
            self,
            num: int = 1,
            gini_index: float = gini_index,
            average_food: float = average_food,
            average_water: float = average_water,
            average_energy: float = average_energy
        ):
        """
        Generate agents
        """
        distribution = gini.lognorm(gini_index)
        homes_id = self.infrastructure.homes
        for _ in range(num):
            home_id = random.choice(homes_id)
            socioeconomic_status = distribution.rvs()
            food = average_food * socioeconomic_status
            water = average_water * socioeconomic_status
            energy = average_energy * socioeconomic_status
            balance = average_balance * socioeconomic_status 
            self.add_agent(
                home_id=home_id,
                socioeconomic_status=socioeconomic_status,
                food=food,
                water=water,
                energy=energy,
                enough_food=deepcopy(food),
                enough_water=deepcopy(water),
                enough_energy=deepcopy(energy),
                balance=balance
            )

    def add_agent(
        self,
        home_id: int,
        id: int = None,
        socioeconomic_status: float = 1,
        food: float = 1,
        water: float = 1,
        energy: float = 1,
        enough_food: float = 1,
        enough_water: float = 1,
        enough_energy: float = 1,
        balance: float = 1
    ):
        id = self.check_id(id)
        self.actions[id] = ActionQueue(agent_id=id)
        self.actions[id].society = self # Binding
        pos = self.infrastructure.pos(id=home_id)
        self.G.add_node(
            id,
            socioeconomic_status=socioeconomic_status,
            home_id=home_id,
            current_node=deepcopy(home_id),
            x=pos[0],
            y=pos[1],
            food=food,
            water=water,
            energy=energy,
            idle_food_rate=idle_food_rate,
            idle_water_rate=idle_water_rate,
            idle_energy_rate=idle_energy_rate,
            enough_food=enough_food,
            enough_water=enough_water,
            enough_energy=enough_energy,
            balance=balance,
            alive=True,
            speed=speed,
            transportation_food_rate=transportation_food_rate,
            transportation_water_rate=transportation_water_rate,
            transportation_energy_rate=transportation_energy_rate,
            max_time_outside=max_time_outside
        )

    def pos(self, id: int, new_val: list = None):
        if new_val is None:
            return [float(self.G.nodes[id].get('x', None)), float(self.G.nodes[id].get('y', None))]
        else:
            self.G.nodes[id]['x'] = float(new_val[0])
            self.G.nodes[id]['y'] = float(new_val[1])
        
    def home_id(self, id: int):
        return self.G.nodes[id].get('home_id', None)
    
    def get_current_node(self, id: int):
        return self.G.nodes[id].get('current_node', None)
        
    def set_current_node(self, id: int, new_val: int = None):
        self.G.nodes[id]['current_node'] = new_val

    def is_home(self, id: int):
        return self.home_id(id) == self.get_current_node(id)

    def max_time_outside(self, id: int):
        return self.G.nodes[id].get('max_time_outside', None)

    def balance(self, id: int, new_val: float = None):
        if new_val is None:
            return self.G.nodes[id].get('balance', None)
        else:
            self.G.nodes[id]['balance'] = new_val
    
    def income(self, id: int):
        return self.G.nodes[id].get('socioeconomic_status', None) * self.average_income
    
    def is_alive(self, id: int, new_val: bool = None):
        if new_val is None:
            val = self.G.nodes[id].get('alive', None)
            if val is None:
                raise ValueError
            return val
        else:
            self.G.nodes[id]['alive'] = new_val
    
    def speed(self, id: int):
        return self.G.nodes[id].get('speed', None)
    
    def transportation_food_rate(self, id: int):
        return self.G.nodes[id].get('transportation_food_rate', None)
    
    def transportation_water_rate(self, id: int):
        return self.G.nodes[id].get('transportation_water_rate', None)

    def transportation_energy_rate(self, id: int):
        return self.G.nodes[id].get('transportation_energy_rate', None)
    
    def idle_food_rate(self, id: int):
        return self.G.nodes[id].get('idle_food_rate', None)
    
    def idle_water_rate(self, id: int):
        return self.G.nodes[id].get('idle_water_rate', None)

    def idle_energy_rate(self, id: int):
        return self.G.nodes[id].get('idle_energy_rate', None)
    
    def enough_food(self, id: int):
        return self.G.nodes[id].get('enough_food', None)
    
    def enough_water(self, id: int):
        return self.G.nodes[id].get('enough_water', None)

    def enough_energy(self, id: int):
        return self.G.nodes[id].get('enough_energy', None)

    def food(self, id: int, new_val: float = None):
        if new_val is None:
            return float(self.G.nodes[id].get('food', None))
        else:
            if new_val < 0:
                new_val = 0
                self.is_alive(id, new_val=False)
            self.G.nodes[id]['food'] = new_val
    
    def water(self, id: int, new_val: float = None):
        if new_val is None:
            return float(self.G.nodes[id].get('water', None))
        else:
            if new_val < 0:
                new_val = 0
                self.is_alive(id, new_val=False)
            self.G.nodes[id]['water'] = new_val
    
    def energy(self, id: int, new_val: float = None):
        if new_val is None:
            return float(self.G.nodes[id].get('energy', None))
        else:
            if new_val < 0:
                new_val = 0
                self.is_alive(id, new_val=False)
            self.G.nodes[id]['energy'] = new_val

    def resources_value(self, id: int) -> float:
        """
        Monetary value of resources that an agent possesses
        """
        food_value = self.food(id) * self.food_price
        water_value = self.water(id) * self.water_price
        energy_value = self.energy(id) * self.energy_price
        return food_value + water_value + energy_value

    def wealth(self, id: int) -> float:
        """
        Wealth of an agent
        """
        return self.balance(id) + self.resources_value(id)

    @property
    def gini_index(self) -> float:
        """
        Calculate the current gini index of society
        """
        data = []
        for id in self.agents:
            data.append(self.wealth(id))
        return gini.coefficient(data)
    
    def edge_id(self, id_1: int, id_2: int):
        """
        Get edge id based on its id_1 and id_2 (both ends)
        """
        result = None
        if self.G.has_edge(id_1, id_2):
            edge = self.G.edges[id_1, id_2]
            result = edge['id']
        return result
    
    def edge_ids(self, id: int):
        """
        Get edge id_1 and id_2 (both ends) based on its id
        """
        result = None
        for id_1, id_2 in self.G.edges():
            if self.edge_id(id_1, id_2) == id:
                result = [id_1, id_2]
                break
        return result
    
    @property
    def edges_ids(self):
        """
        Return all edges ids
        """
        return list(self.G.edges())

    @property
    def edges_id(self):
        """
        Return all edges id
        """
        result = []
        edges = self.edges_ids
        for ids in edges:
            id = self.edge_id(*ids)
            result.append(id)
        return result
    
    @property
    def nodes_id(self):
        """
        Return all nodes id
        """
        return list(self.G.nodes())
    
    @property
    def agents(self):
        """
        List all agents
        """
        return self.nodes_id
    
    @property
    def dead_agents(self):
        """
        List all dead agents
        """
        result = []
        for agent in self.agents:
            if self.is_alive(id=agent) is False:
                result.append(agent)
        return result
    
    @property
    def alive_agents(self):
        """
        List all alive agents
        """
        result = []
        for agent in self.agents:
            if self.is_alive(id=agent) is True:
                result.append(agent)
        return result
    
    def agents_in(self, id: int):
        """
        Return a list of agents currently within a certain node
        """
        result = []
        for agent in self.alive_agents:
            if self.get_current_node(id=agent) == id:
                result.append(agent)
        return result
    
    def trade(self, agents: list, market: int = None):
        # Load data to solver
        info = []
        if market is not None:
            market_info = {
                'id': market,
                'resources': {
                    'food': self.infrastructure.food(market),
                    'water': self.infrastructure.water(market),
                    'energy': self.infrastructure.energy(market),
                },
                'enough_resources': {
                    'food': self.infrastructure.enough_food(market),
                    'water': self.infrastructure.enough_water(market),
                    'energy': self.infrastructure.enough_energy(market),
                },
                'balance': self.infrastructure.balance(market)
            }
            info.append(market_info)
        for agent_id in agents:
            agent_info = {
                'id': agent_id,
                'resources': {
                    'food': self.food(agent_id),
                    'water': self.water(agent_id),
                    'energy': self.energy(agent_id),
                },
                'enough_resources': {
                    'food': self.enough_food(agent_id),
                    'water': self.enough_water(agent_id),
                    'energy': self.enough_energy(agent_id),
                },
                'balance': self.balance(agent_id)
            }
            info.append(agent_info)
        prices = {
            'food': self.food_price,
            'water': self.water_price,
            'energy': self.energy_price
        }
        # Solve
        result = trade_solver(info, prices)
        #log = []
        # Apply results to the model
        for i, info in enumerate(result):
            id = info['id']
            if market is not None and i == 0:
                self.infrastructure.food(market, new_val=info['resources']['food'])
                self.infrastructure.water(market, new_val=info['resources']['water'])
                self.infrastructure.energy(market, new_val=info['resources']['energy'])
                self.infrastructure.balance(market, new_val=info['balance'])
            else:
                self.food(id, new_val=info['resources']['food'])
                self.water(id, new_val=info['resources']['water'])
                self.energy(id, new_val=info['resources']['energy'])
                self.balance(id, new_val=info['balance'])
        #return log
    
    def utility_food(self, agent_id: int) -> float:
        amount = self.food(agent_id)
        enough_amount = self.enough_food(agent_id)
        return utility(resource=amount, enough_resource=enough_amount)

    def utility_water(self, agent_id: int) -> float:
        amount = self.food(agent_id)
        enough_amount = self.enough_water(agent_id)
        return utility(resource=amount, enough_resource=enough_amount)
        
    def utility_energy(self, agent_id: int) -> float:
        amount = self.food(agent_id)
        enough_amount = self.enough_energy(agent_id)
        return utility(resource=amount, enough_resource=enough_amount)
    
    def utility(self, agent_id: int):
        return {
            'food': self.utility_food(agent_id),
            'water': self.utility_water(agent_id),
            'energy': self.utility_energy(agent_id)
        }
    
    def update(self, duration: float, measure: bool = False):
        # Measure accessibility (first entry)
        if measure is True and self.model.accessibility.pristine is True:
            self.model.accessibility.add_date(self.model.date)
            self.model.accessibility.pristine = False

        # Idle resource consumption & income
        for id in self.alive_agents:
            # Food
            food = self.food(id)
            food_rate = self.idle_food_rate(id)
            new_food = food - food_rate * duration
            self.food(id, new_val=new_food)
            # Water
            water = self.water(id)
            water_rate = self.idle_water_rate(id)
            new_water = water - water_rate * duration
            self.water(id, new_val=new_water)
            # Energy
            energy = self.energy(id)
            energy_rate = self.idle_energy_rate(id)
            new_energy = energy - energy_rate * duration
            self.energy(id, new_val=new_energy)
            # Income
            balance = self.balance(id)
            income = self.income(id)
            new_balance = balance + income * duration
            self.balance(id, new_val=new_balance)

        # Action update
        for id in self.alive_agents:
            action_queue = self.actions[id]
            if action_queue.done is True:
                action_queue.reset()
                # Decide
                markets = self.infrastructure.markets
                best_destination, _ = self.select_top_destination(agent_id=id, destinations=markets, is_market=True)
                # When market is available
                if best_destination is not None:
                    self.go_and_comeback_and_stay(agent_id=id, destination_id=best_destination)
                else:
                    possible_destinations = self.infrastructure.filter_nodes_closer_than(
                        id=self.get_current_node(id),
                        nodes=self.infrastructure.homes,
                        distace=100
                    )
                    best_destination, _ = self.select_top_destination(agent_id=id, destinations=possible_destinations, is_market=False)
                    self.go_and_comeback_and_stay(agent_id=id, destination_id=best_destination)
            # Execute
            action_queue.update(duration, measure=measure)

        # Trade
        for market_id in self.infrastructure.markets:
            agents = self.agents_in(id=market_id)
            if len(agents) >= 1:
                self.trade(agents=agents, market=market_id)
        for home_id in self.infrastructure.homes:
            agents = self.agents_in(id=home_id)
            if len(agents) >= 2:
                self.trade(agents=agents)

        # Measure accessibility
        if measure is True:
            date = self.model.date
            self.model.accessibility.add_date(date)
            for id in self.agents:
                utility_food = self.utility(id, 'food')
                utility_water = self.utility(id, 'water')
                utility_energy = self.utility(id, 'energy')
                utility = {
                    'food': utility_food,
                    'water': utility_water,
                    'energy': utility_energy,
                }
                self.model.accessibility.add_utility(id, utility)

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

    def estimated_distance(self, agent_id, destination_id):
        return self.infrastructure.heuristic_paths.estimated_distance(
            id_start=self.get_current_node(id=agent_id),
            id_end=destination_id
        )
    
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

    def resources_in(self, node_id, is_market: bool):
        agents = self.agents_in(id=node_id)
        food = 0
        water = 0
        energy = 0
        for agent_id in agents:
            food += self.food(id=agent_id)
            water += self.water(id=agent_id)
            energy += self.energy(id=agent_id)
        if is_market is True:
            food += self.infrastructure.food(node_id)
            water += self.infrastructure.water(node_id)
            energy += self.infrastructure.energy(node_id)
        return food, water, energy
    
    def estimated_duration(self, agent_id, destination_id):
        estimated_distance = self.estimated_distance(agent_id, destination_id)
        speed = self.speed(id=agent_id)
        return estimated_distance / speed
    
    def transportation_fuel(self, agent_id, duration):
        fuel_food = self.transportation_food_rate(id=agent_id) * duration
        fuel_water = self.transportation_water_rate(id=agent_id) * duration
        fuel_energy = self.transportation_energy_rate(id=agent_id) * duration
        return fuel_food, fuel_water, fuel_energy
    
    def path(self, agent_id, destination_id):
        result = None
        id_start = self.get_current_node(id=agent_id)
        #print(id_start, destination_id)
        if nx.has_path(
            self.infrastructure.G,
            source=id_start,
            target=destination_id
        ):
            result = nx.astar_path(
                self.infrastructure.G,
                source=id_start,
                target=destination_id,
                heuristic=self.infrastructure.heuristic_paths.estimated_distance,
                weight="adjusted_length"
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
            stay_length = self.max_time_outside(id=agent_id) - (2 * move_go.total_duration)
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

    def serialize(self) -> dict:
        dictionary = {}
        actions_serialized = {}
        for id in self.actions:
            action_queue = self.actions[id]
            actions_serialized[id] = action_queue.serialize()
        dictionary['actions'] = actions_serialized
        dictionary['G'] = nx_serialize(self.G)
        dictionary['food_price'] = self.food_price
        dictionary['water_price'] = self.water_price
        dictionary['energy_price'] = self.energy_price
        dictionary['average_income'] = self.average_income
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        actions_serialized = dictionary['actions']
        self.actions = {}
        for id in actions_serialized:
            action_queue = ActionQueue(id)
            action_queue.society = self # Binding
            action_queue.deserialize(actions_serialized[id])
            self.actions[id] = action_queue
        self.G = nx_deserialize(dictionary['G'])
        self.food_price = dictionary['food_price']
        self.water_price = dictionary['water_price']
        self.energy_price = dictionary['energy_price']
        self.average_income = dictionary['average_income']


if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.bake()
    model.society.generate_agents(num=1)
    #model.society.update(1000000)
    #print(len(model.society.dead_agents))
    #print(society)
    print(model.society.serialize())