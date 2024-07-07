from piperabm.society.query.add import Add
from piperabm.society.query.get import Get
from piperabm.society.query.set import Set


class Query(Add, Get, Set):
    """
    Query network elements
    """

    def has_node(self, id: int) -> bool:
        """
        Check whether the network already contains the node
        """
        return self.G.has_node(id)

    def has_edge(self, ids: list) -> bool:
        """
        Check whether the network already contains the edge
        """
        return self.G.has_edge(*ids)
    
    def is_home(self, id: int) -> bool:
        return self.get_home_id(id=id) == self.get_current_node(id=id)
    
    def resources_value(self, id: int) -> float:
        """
        Monetary value of resources that an agent possesses
        """
        values = []
        for name in self.resource_names:
            value = self.get_resource(id=id, name=name) * self.prices[name]
            values.append(value)
        return sum(values)
    
    def resources_in(self, node_id, is_market: bool):
        """
        All resources available in a node
        """
        agents = self.agents_in(id=node_id)
        result = {}
        for name in self.resource_names:
            result[name] = 0
        for agent_id in agents:
            for name in self.resource_names:
                result[name] += self.get_resource(id=agent_id, name=name)
        if is_market is True:
            for name in self.resource_names:
                result[name] += self.infrastructure.get_resource(id=node_id, name=name)
        return result
        '''
        food = 0
        water = 0
        energy = 0
        for agent_id in agents:
            food += self.get_resource(id=agent_id, name='food')
            water += self.get_resource(id=agent_id, name='water')
            energy += self.get_resource(id=agent_id, name='energy')
        if is_market is True:
            food += self.infrastructure.get_resource(id=node_id, name='food')
            water += self.infrastructure.get_resource(id=node_id, name='water')
            energy += self.infrastructure.get_resource(id=node_id, name='energy')
        return food, water, energy
        '''
        
    def wealth(self, id: int) -> float:
        """
        Wealth of an agent
        """
        return self.get_balance(id) + self.resources_value(id)
    
    def ego(self, id: int, type: str = None) -> list:
        """
        Return agent nodes in the ego network
        """
        connected_nodes = list(self.G.neighbors(id))  # Get all nodes connected to node_id
        if type is not None:
            # Filter connected nodes by the edge attribute 'type' equal to 'family'
            result = []
            for neighbor in connected_nodes:
                edges = self.G.get_edge_data(id, neighbor)
                for key, attr in edges.items():
                    if attr.get('type') == type:
                        result.append(neighbor)
                        break  # If one edge meets the condition, we can stop checking further
            connected_nodes = result
        return connected_nodes

    def agents_in(self, id: int) -> list:
        """
        Return all agents in a certain node
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'agent' and attr.get('current_node') == id]
        except:
            return []

    def agents_from(self, home_id: int) -> list:
        """
        Return all agents from a certain home (family)
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'agent' and attr.get('home_id') == home_id]
        except:
            return []

    @property
    def agents(self) -> list:
        """
        Return all agent nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'agent']
        except:
            return []
        
    @property
    def alives(self) -> list:
        """
        Return all alive agent nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'agent' and attr.get('alive') is True]
        except:
            return []
        
    @property
    def deads(self) -> list:
        """
        Return all alive agent nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'agent' and attr.get('alive') is False]
        except:
            return []

    @property
    def families(self) -> list:
        """
        Return all family edges
        """
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'family']
        except:
            return []
        
    @property
    def friends(self) -> list:
        """
        Return all friend edges
        """
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'friend']
        except:
            return []
        
    @property
    def neighbors(self) -> list:
        """
        Return all friend edges
        """
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'neighbor']
        except:
            return []