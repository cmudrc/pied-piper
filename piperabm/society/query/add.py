import uuid
from copy import deepcopy

from piperabm.society.actions import ActionQueue


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
        home_id: int,
        id: int = None,
        name: str = '',
        socioeconomic_status: float = 1,
        food: float = 1,
        water: float = 1,
        energy: float = 1,
        enough_food: float = 1,
        enough_water: float = 1,
        enough_energy: float = 1,
        balance: float = 1
    ):
        """
        Add agent node
        """
        type = 'agent'
        id = self.check_id(id)
        self.actions[id] = ActionQueue(agent_id=id)
        self.actions[id].society = self # Binding
        pos = self.infrastructure.pos(id=home_id)
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

    def add_family(
        self,
        id_1: int,
        id_2: int
    ):
        """
        Add family edge (bidirectional)
        """
        type = 'family'
        home_id_1 = self.get_node_attribute(id=id_1, attribute='home_id')
        home_id_2 = self.get_node_attribute(id=id_1, attribute='home_id')
        if home_id_1 != home_id_2:
            raise ValueError
        else:
            home_id = home_id_1
        self.G.add_edge(
            id_1,
            id_2,
            type=type,
            home_id=home_id
        )
        self.G.add_edge(
            id_2,
            id_1,
            type=type,
            home_id=home_id
        )

    def add_friend(
        self,
        id_1: int,
        id_2: int
    ):
        """
        Add friend edge (directional)
        """
        type = 'family'
        self.G.add_friend(
            id_1,
            id_2,
            type=type
        )