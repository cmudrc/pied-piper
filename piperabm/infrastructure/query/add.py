import uuid
from copy import deepcopy

from piperabm.tools.coordinate import distance as ds


class Add:

    def check_id(self, id):
        """
        Check whether id already exists
        """
        if id is None:
            id = self.new_id()
        else:
            if id in self.nodes:
                id = self.new_id()
                print("id already exists. replaced with new id.")
        return id

    def new_id(self):
        """
        Generate new unique and radnom id
        """
        return uuid.uuid4().int

    def add_junction(
        self,
        pos: list,
        id: int = None,
        name: str = '',
        report: bool = False
    ):
        """
        Add junction node
        """
        type = 'junction'
        id = self.check_id(id)
        self.G.add_node(
            id,
            name=name,
            type=type,
            x=pos[0],
            y=pos[1]
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id
    
    def add_home(
        self,
        pos: list,
        id: int = None,
        name: str = '',
        report: bool = False
    ):
        """
        Add home node
        """
        type = 'home'
        id = self.check_id(id)
        self.G.add_node(
            id,
            name=name,
            type=type,
            x=pos[0],
            y=pos[1]
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id
    
    def add_market(
        self,
        pos: list,
        food: float = 0,
        water: float = 0,
        energy: float = 0,
        id: int = None,
        name: str = '',
        report: bool = False,
    ):
        """
        Add market node
        """
        type = 'market'
        id = self.check_id(id)
        self.G.add_node(
            id,
            name=name,
            type=type,
            x=pos[0],
            y=pos[1],
            food=food,
            water=water,
            energy=energy,
            enough_food=deepcopy(food),
            enough_water=deepcopy(water),
            enough_energy=deepcopy(energy),
            balance=0,
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id

    def add_street(
        self,
        pos_1: list,
        pos_2: list,
        name: str = '',
        usage_impact: float = 0,
        weather_impact: float = 0,
        report: bool = False
    ):
        """
        Add street edge
        """
        type = 'street'
        id_1 = self.add_junction(pos=pos_1)
        id_2 = self.add_junction(pos=pos_2)
        length = ds.point_to_point(pos_1, pos_2)
        self.G.add_edge(
            id_1,
            id_2,
            name=name,
            length=length,
            #adjusted_length=self.calculate_adjusted_length(length, degradation),
            usage_impact=usage_impact,
            weather_impact=weather_impact,
            adjusted_length=None,
            type=type,
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} edge at positions {pos_1}-{pos_2} added.")
        return id
    
    def add_neighborhood_access(
        self,
        id_1: list,
        id_2: list,
        name: str = '',
        usage_impact: float = 0,
        weather_impact: float = 0,
        report: bool = False
    ):
        """
        Add neighborhood access edge
        """
        type = 'neighborhood_access'
        length = ds.point_to_point(self.pos(id_1), self.pos(id_2))
        self.G.add_edge(
            id_1,
            id_2,
            name=name,
            length=length,
            #adjusted_length=self.calculate_adjusted_length(length, degradation),
            usage_impact=usage_impact,
            weather_impact=weather_impact,
            adjusted_length=None,
            type=type
        )
        #self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} edge at positions {self.pos(id_1)} - {self.pos(id_2)} added.")
        return id