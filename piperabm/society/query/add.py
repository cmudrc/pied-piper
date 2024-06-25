import uuid
import random
from copy import deepcopy

from piperabm.society.actions.action_queue import ActionQueue
from piperabm.society.info import *
from piperabm.tools.symbols import SYMBOLS


class Add:
    """
    Add new network elements
    """

    def check_id(self, id):
        """
        Check whether id already exists
        """
        if id is None:
            id = self.new_id()
        else:
            if id in self.agents:
                id = self.new_id()
                print("id already exists. replaced with new id.")
        return id

    def new_id(self) -> int:
        """
        Generate new unique and radnom id
        """
        return uuid.uuid4().int
    
    def add_agent(
        self,
        home_id: int = None,
        id: int = None,
        name: str = '',
        socioeconomic_status: float = 1,
        food: float = 0,
        water: float = 0,
        energy: float = 0,
        enough_food: float = SYMBOLS['eps'],
        enough_water: float = SYMBOLS['eps'],
        enough_energy: float = SYMBOLS['eps'],
        balance: float = 0
    ):
        """
        Add agent node
        """
        if self.infrastructure.baked is False:
            raise ValueError("Model is not baked.")
        type = 'agent'
        id = self.check_id(id)
        self.actions[id] = ActionQueue(agent_id=id)
        self.actions[id].society = self # Binding
        if home_id is None:
            homes_id = self.infrastructure.homes
            home_id = random.choice(homes_id)
        pos = self.infrastructure.get_pos(id=home_id)
        self.G.add_node(
            id,
            name=name,
            type=type,
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
        # Add family
        family_members = self.agents_from(home_id=home_id)
        for member in family_members:
            if member != id:
                self.add_family(id_1=id, id_2=member)
        # Add neighbor
        neighbor_homes = self.infrastructure.nodes_closer_than(
            id=home_id,
            search_radius=self.neighbor_radius,
            nodes=self.infrastructure.homes,
            include_self=False
        )
        for neighbor_home_id in neighbor_homes:
            neighbors = self.agents_from(home_id=neighbor_home_id)
            for neighbor in neighbors:
                self.add_neighbor(id_1=id, id_2=neighbor)
        

    def add_family(
        self,
        id_1: int,
        id_2: int
    ):
        """
        Add family edge
        """
        type = 'family'
        home_id_1 = self.get_node_attribute(id=id_1, attribute='home_id')
        home_id_2 = self.get_node_attribute(id=id_1, attribute='home_id')
        if home_id_1 == home_id_2 and \
        id_1 != id_2:
            home_id = home_id_1
            self.G.add_edge(
                id_1,
                id_2,
                type=type,
                home_id=home_id
            )

    def add_friend(
        self,
        id_1: int,
        id_2: int
    ):
        """
        Add friend edge
        """
        type = 'friend'
        self.G.add_edge(
            id_1,
            id_2,
            type=type
        )

    def add_neighbor(
        self,
        id_1,
        id_2
    ):
        """
        Add neighbor edge
        """
        type = 'neighbor'
        home_id_1 = self.get_node_attribute(id=id_1, attribute='home_id')
        home_id_2 = self.get_node_attribute(id=id_2, attribute='home_id')
        if home_id_1 != home_id_2 and \
        id_1 != id_2:
            self.G.add_edge(
                id_1,
                id_2,
                type=type,
            )