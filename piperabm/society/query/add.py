import numpy as np
from copy import deepcopy

from piperabm.exceptions import ModelNotBakedError
from piperabm.resource import Resource
from piperabm.society.actions.action_queue import ActionQueue
from piperabm.society.info import *


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
        while id in self.agents:
            id = self.new_id()
        return id

    def new_id(self) -> int:
        """
        Generate new unique random id
        """
        return int(
            np.random.randint(low=0, high=np.iinfo(np.int64).max, dtype=np.int64)
        )

    def add_agent(
        self,
        home_id: int = None,
        id: int = None,
        name: str = "",
        socioeconomic_status: float = 1,
        resources: dict | Resource = Resource(),
        enough_resources: dict | Resource | None = None,
        balance: float = 0,
    ):
        """
        Add an agent node to the society network.

        Agents are represented as nodes in the society graph. Each agent is assigned to
        a home node in the infrastructure and initialized with resources and a balance.
        When an agent is added, family and neighbor relationships may be created
        automatically based on the agent's home assignment.

        Parameters
        ----------
        home_id : int, optional
            ID of the home node that the agent belongs to. If ``None``, a home is chosen
            at random from existing infrastructure homes.

        id : int, optional
            Unique identifier of the agent node. If ``None``, a unique ID is automatically
            generated. If the provided ID already exists, a new unique ID is generated
            instead (the existing agent is not overwritten).

        name : str, optional
            Optional human-readable name for the agent.

        socioeconomic_status : float, optional
            Socioeconomic status of the agent (used by the decision-making and/or
            behavior models). Defaults to ``1``.

        resources : dict or Resource, optional
            Initial resource inventory for the agent. This can be provided either as a
            dictionary (e.g., ``{'food': 10, 'water': 10, 'energy': 10}``) or as a
            :class:`piperabm.Resource` instance. If a ``Resource`` object is provided,
            it is converted internally to a dictionary before being attached to the
            underlying graph representation.

        enough_resources : dict or Resource or None, optional
            The per-resource "enough" thresholds used by the agent's satisfaction/utility
            model. If provided as a ``Resource`` object, it is converted internally to a
            dictionary. If ``None``, the system initializes the threshold for each
            resource to match the corresponding initial ``resources`` value.

        balance : float, optional
            Initial monetary balance of the agent. Defaults to ``0``.

        Returns
        -------
        int
            The ID of the newly added agent node.

        Raises
        ------
        ModelNotBakedError
            If the infrastructure has not been baked. Agents require a finalized
            infrastructure network (via :meth:`~piperabm.Model.bake`) to ensure
            physically consistent routing and access edges.

        Notes
        -----
        Internally, agent state (including resources and thresholds) is stored as plain
        attributes on the NetworkX society graph. The :class:`piperabm.Resource` class
        is provided as an optional convenience wrapper for validation/readability and
        does not change the internal representation.
        """
        if self.infrastructure.baked is False:
            raise ModelNotBakedError("Model is not baked.")
        type = "agent"
        id = self.check_id(id)
        self.actions[id] = ActionQueue(agent_id=id)
        self.actions[id].society = self  # Binding
        if home_id is None:
            homes_id = self.infrastructure.homes
            home_id = int(np.random.choice(homes_id))
        pos = self.infrastructure.get_pos(id=home_id)
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
            socioeconomic_status=socioeconomic_status,
            home_id=home_id,
            current_node=deepcopy(home_id),
            x=float(pos[0]),
            y=float(pos[1]),
            balance=balance,
            alive=True,
            **resource_kwargs,
        )

        # Add relationship edge(s)
        # Family
        family_members = self.agents_from(home_id=home_id)
        for member in family_members:
            if member != id:
                self.add_family(id_1=id, id_2=member)

        # Neighbor
        neighbor_homes = self.infrastructure.nodes_closer_than(
            id=home_id,
            search_radius=self.neighbor_radius,
            nodes=self.infrastructure.homes,
            include_self=False,
        )
        for neighbor_home_id in neighbor_homes:
            neighbors = self.agents_from(home_id=neighbor_home_id)
            for neighbor in neighbors:
                self.add_neighbor(id_1=id, id_2=neighbor)
        return id

    def add_family(self, id_1: int, id_2: int):
        """
        Add a family relationship edge between two agents.

        A family relationship is created automatically when two distinct agents are
        assigned to the same home. This method adds a ``family``-typed edge between
        the two agent nodes in the society graph, provided that both agents share
        the same ``home_id``.

        Parameters
        ----------
        id_1 : int
            ID of the first agent.

        id_2 : int
            ID of the second agent.

        Notes
        -----
        - A family edge is only added if ``id_1`` and ``id_2`` are different agents
          and both are associated with the same home node.
        - The edge is stored in the underlying NetworkX multi-graph with
          ``type='family'`` and includes the shared ``home_id`` as an edge attribute.
        - If the agents do not share the same home, no edge is added and the method
          exits silently.

        See Also
        --------
        add_neighbor : Add a neighbor relationship between agents in nearby homes.
        add_friend : Add a user-defined friendship relationship between agents.
        """
        type = "family"
        home_id_1 = self.get_node_attribute(id=id_1, attribute="home_id")
        home_id_2 = self.get_node_attribute(id=id_1, attribute="home_id")
        if home_id_1 == home_id_2 and id_1 != id_2:
            home_id = home_id_1
            self.G.add_edge(id_1, id_2, type=type, home_id=home_id)

    def add_friend(self, id_1: int, id_2: int):
        """
        Add a friendship relationship edge between two agents.

        A friendship relationship represents an explicit, user-defined social tie
        between two agents. Unlike family or neighbor relationships, friendship
        edges are not created automatically and must be added explicitly by the user.

        Parameters
        ----------
        id_1 : int
            ID of the first agent.

        id_2 : int
            ID of the second agent.

        Notes
        -----
        - Friendship edges are stored in the underlying NetworkX multi-graph with
          ``type='friend'`` as an edge attribute.
        - No structural constraints are enforced: the agents do not need to share
          the same home or be geographically close.
        - This method does not prevent duplicate friendship edges from being added;
          multiple friendship edges between the same pair of agents may exist.

        See Also
        --------
        add_family : Add a family relationship between agents sharing the same home.
        add_neighbor : Add a neighbor relationship between agents in nearby homes.
        """
        type = "friend"
        self.G.add_edge(id_1, id_2, type=type)

    def add_neighbor(self, id_1, id_2):
        """
        Add a neighbor relationship edge between two agents.

        A neighbor relationship represents spatial proximity between agents whose
        assigned home nodes are distinct but located within a specified neighborhood
        radius. This method adds a ``neighbor``-typed edge between two agents if they
        are not members of the same household.

        Parameters
        ----------
        id_1 : int
            ID of the first agent.

        id_2 : int
            ID of the second agent.

        Notes
        -----
        - A neighbor edge is only added if ``id_1`` and ``id_2`` are different agents
          and their associated ``home_id`` values are not equal.
        - Neighbor relationships are typically created automatically during agent
          initialization based on spatial proximity between home nodes.
        - The edge is stored in the underlying NetworkX multi-graph with
          ``type='neighbor'`` as an edge attribute.
        - If the agents share the same home, no edge is added and the method exits
          silently.

        See Also
        --------
        add_family : Add a family relationship between agents sharing the same home.
        add_friend : Add a user-defined friendship relationship between agents.
        """
        type = "neighbor"
        home_id_1 = self.get_node_attribute(id=id_1, attribute="home_id")
        home_id_2 = self.get_node_attribute(id=id_2, attribute="home_id")
        if home_id_1 != home_id_2 and id_1 != id_2:
            self.G.add_edge(
                id_1,
                id_2,
                type=type,
            )


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_0 import model

    model.society.add_agent()
    print(model.society)
