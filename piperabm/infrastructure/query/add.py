import numpy as np
from copy import deepcopy

from piperabm.tools.coordinate import distance as ds


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
            if id in self.nodes:
                id = self.new_id()
                print("id already exists. replaced with new id.")
        return id

    def new_id(self):
        """
        Generate new unique random id
        """
        return int(np.random.randint(low=0, high=np.iinfo(np.int64).max, dtype=np.int64))

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
            x=float(pos[0]),
            y=float(pos[1])
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
            x=float(pos[0]),
            y=float(pos[1])
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id
    
    def add_market(
        self,
        pos: list,
        resources: dict = {
            'food': 10,
            'water': 10,
            'energy': 10,
        },
        enough_resources: dict = None,
        id: int = None,
        name: str = '',
        report: bool = False,
    ):
        """
        Add market node
        """
        type = 'market'
        id = self.check_id(id)
        resource_kwargs = {}
        if enough_resources is None:
            enough_resources = {}
            for resource_name in self.resource_names:
                enough_resources[resource_name] = None
        for resource_name in self.resource_names:
            if enough_resources[resource_name] is None:
                enough_resources[resource_name] = deepcopy(resources[resource_name])
            resource_kwargs[resource_name] = resources[resource_name]
            resource_kwargs['enough_'+resource_name] = enough_resources[resource_name]
        
        self.G.add_node(
            id,
            name=name,
            type=type,
            x=float(pos[0]),
            y=float(pos[1]),
            balance=0,
            **resource_kwargs
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
        climate_impact: float = 0,
        report: bool = False
    ):
        """
        Add street edge
        """
        type = 'street'
        id_1 = self.add_junction(pos=pos_1)
        id_2 = self.add_junction(pos=pos_2)
        length = ds.point_to_point(pos_1, pos_2)
        adjustment_factor = self.calculate_adjustment_factor(
            usage_impact=usage_impact,
            climate_impact=climate_impact
        )
        adjusted_length = self.calculate_adjusted_length(
            length=length,
            adjustment_factor=adjustment_factor
        )
        self.G.add_edge(
            id_1,
            id_2,
            name=name,
            length=length,
            adjusted_length=adjusted_length,
            usage_impact=usage_impact,
            climate_impact=climate_impact,
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
        climate_impact: float = 0,
        report: bool = False
    ):
        """
        Add neighborhood access edge
        """
        type = 'neighborhood_access'
        length = ds.point_to_point(self.get_pos(id_1), self.get_pos(id_2))
        adjustment_factor = self.calculate_adjustment_factor(
            usage_impact=usage_impact,
            climate_impact=climate_impact
        )
        adjusted_length = self.calculate_adjusted_length(
            length=length,
            adjustment_factor=adjustment_factor
        )
        self.G.add_edge(
            id_1,
            id_2,
            name=name,
            length=length,
            adjusted_length=adjusted_length,
            usage_impact=usage_impact,
            climate_impact=climate_impact,
            type=type
        )
        #self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} edge at positions {self.get_pos(id_1)} - {self.get_pos(id_2)} added.")
        return id