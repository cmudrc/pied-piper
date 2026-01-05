"""
.. module:: piperabm.infrastructure.query.add
:synopsis: Add new network elements.
"""

import numpy as np
from copy import deepcopy

from piperabm.resource import Resource
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
        while id in self.nodes:
            id = self.new_id()
        return id

    def new_id(self):
        """
        Generate new unique random id
        """
        return int(
            np.random.randint(low=0, high=np.iinfo(np.int64).max, dtype=np.int64)
        )

    def add_junction(
        self, pos: list, id: int = None, name: str = "", report: bool = False
    ):
        """
        Add junction node.
        These are the nodes that connect edges in the network and represent a physical point in the world.

        Parameters
        ----------
        pos : list
            A list of [x, y] coordinates showing the position in space.
        id : int, optional
            The unique id number. The default is `None`, and if stays `None`, system will automatically assign a new unique id.
        name : str, optional
            Optional name of the element.
        report : bool
            If `True`, system will report successful creation of this element.
        """
        type = "junction"
        id = self.check_id(id)
        self.G.add_node(id, name=name, type=type, x=float(pos[0]), y=float(pos[1]))
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id

    def add_home(self, pos: list, id: int = None, name: str = "", report: bool = False):
        """
        Add home node.
        These are the nodes where agents live and belong to. Agents from the same home are a family and together they form a household.

        Parameters
        ----------
        pos : list
            A list of [x, y] coordinates showing the position in space.
        id : int, optional
            The unique id number. The default is `None`, and if stays `None`, system will automatically assign a new unique id.
        name : str, optional
            Optional name of the element.
        report : bool
            If `True`, system will report successful creation of this element.
        """
        type = "home"
        id = self.check_id(id)
        self.G.add_node(id, name=name, type=type, x=float(pos[0]), y=float(pos[1]))
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id

    def add_market(
        self,
        pos: list,
        resources: dict | Resource = Resource(),
        enough_resources: dict | Resource | None = None,
        id: int = None,
        name: str = "",
        report: bool = False,
    ):
        """
        Add market node
        These are the nodes where resources are bought and sold. The influx of resources to the model only happens through markets. They also act as social hubs in the model.

        Parameters
        ----------
        pos : list
            A list of [x, y] coordinates showing the position in space.
        resources : dict or Resource, optional
            Initial resource stock of the market. This can be provided either as a plain
            dictionary (e.g., ``{'food': 100, 'water': 100, 'energy': 100}``) or as a
            :class:`piperabm.Resource` instance. If a ``Resource`` object is provided,
            it is converted internally to a dictionary before being attached to the
            underlying graph representation. If not specified, default resource values
            are used.
        enough_resources : dict or Resource or None, optional
            Maximum stock capacity for each resource. If provided as a ``Resource`` object,
            it is converted internally to a dictionary. If ``None``, the system initializes
            this value to match the initial ``resources`` levels.
        id : int, optional
            The unique id number. The default is `None`, and if stays `None`, system will automatically assign a new unique id.
        name : str, optional
            Optional name of the element.
        report : bool
            If `True`, system will report successful creation of this element.
        """
        type = "market"
        id = self.check_id(id)
        if isinstance(resources, Resource):
            resources = resources.serialize()
        if isinstance(enough_resources, Resource):
            enough_resources = enough_resources.serialize()
        resource_kwargs = {}
        if enough_resources is None:
            enough_resources = {}
            for resource_name in self.resource_names:
                enough_resources[resource_name] = None
        for resource_name in self.resource_names:
            if enough_resources[resource_name] is None:
                enough_resources[resource_name] = deepcopy(resources[resource_name])
            resource_kwargs[resource_name] = resources[resource_name]
            resource_kwargs["enough_" + resource_name] = enough_resources[resource_name]

        self.G.add_node(
            id,
            name=name,
            type=type,
            x=float(pos[0]),
            y=float(pos[1]),
            balance=0,
            **resource_kwargs,
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
        name: str = "",
        usage_impact: float = 0,
        age_impact: float = 0,
        report: bool = False,
    ):
        """
        Add street edge. These edges are used by agents to move around the simulation world.

        Parameters
        ----------
        pos_1 : list
            A list of [x, y] coordinates showing the position of one of the ends in space.
        pos_2 : list
            A list of [x, y] coordinates showing the position of the other end in space.
        name : str, optional
            Optional name of the element.
        usage_impact : float, optional
            The more the element is used, this number will grow. It will be used to calcualte `adjustment_facor` when computing the degradation. The default is 0.
        age_impact : float, optional
            The more the element age, this number will grow. It will be used to calcualte `adjustment_facor` when computing the degradation. The default is 0.
        report : bool
            If `True`, system will report successful creation of this element.
        """
        type = "street"
        id_1 = self.add_junction(pos=pos_1)
        id_2 = self.add_junction(pos=pos_2)
        length = ds.point_to_point(pos_1, pos_2)
        adjustment_factor = self.calculate_adjustment_factor(
            usage_impact=usage_impact, age_impact=age_impact
        )
        adjusted_length = self.calculate_adjusted_length(
            length=length, adjustment_factor=adjustment_factor
        )
        self.G.add_edge(
            id_1,
            id_2,
            name=name,
            length=length,
            adjusted_length=adjusted_length,
            usage_impact=usage_impact,
            age_impact=age_impact,
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
        name: str = "",
        usage_impact: float = 0,
        age_impact: float = 0,
        report: bool = False,
    ):
        """
        Add neighborhood access edge. These edges connect homes and markets to the street network, allowing agents to access these nodes.

        Parameters
        ----------
        pos_1 : list
            A list of [x, y] coordinates showing the position of one of the ends in space.
        pos_2 : list
            A list of [x, y] coordinates showing the position of the other end in space.
        name : str, optional
            Optional name of the element.
        usage_impact : float, optional
            The more the element is used, this number will grow. It will be used to calcualte `adjustment_facor` when computing the degradation. The default is 0.
        age_impact : float, optional
            The more the element age, this number will grow. It will be used to calcualte `adjustment_facor` when computing the degradation. The default is 0.
        report : bool
            If `True`, system will report successful creation of this element.
        """
        type = "neighborhood_access"
        length = ds.point_to_point(self.get_pos(id_1), self.get_pos(id_2))
        adjustment_factor = self.calculate_adjustment_factor(
            usage_impact=usage_impact, age_impact=age_impact
        )
        adjusted_length = self.calculate_adjusted_length(
            length=length, adjustment_factor=adjustment_factor
        )
        self.G.add_edge(
            id_1,
            id_2,
            name=name,
            length=length,
            adjusted_length=adjusted_length,
            usage_impact=usage_impact,
            age_impact=age_impact,
            type=type,
        )
        # self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(
                f">>> {type} edge at positions {self.get_pos(id_1)} - {self.get_pos(id_2)} added."
            )
        return id
