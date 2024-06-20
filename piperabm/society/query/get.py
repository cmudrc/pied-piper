class Get:
    """
    Get attributes from network elements
    """

    def get_node_attribute(self, id: int, attribute: str, default=None):
        """
        Get node attribute from networkx graph
        """
        return self.G.nodes[id].get(attribute, default)
    
    def get_edge_attribute(self, ids: list, attribute: str, default=None):
        """
        Get edge attribute from networkx graph
        """
        return self.G.edges[*ids].get(attribute, default)
    
    def get_node_attributes(self, id: list) -> dict:
        """
        Get all node attribute from networkx graph
        """
        return self.G.nodes[id]
    
    def get_edge_attributes(self, ids: list) -> dict:
        """
        Get all edge attribute from networkx graph
        """
        return self.G.get_edge_data(*ids)
    
    def get_pos(self, id: int):
        """
        Get node position
        """
        return [self.get_node_attribute(id, 'x', None), self.get_node_attribute(id, 'y', None)]
    
    def node_type(self, id: int) -> str:
        return self.get_node_attribute(id=id, attribute='type')

    def edge_type(self, ids: list) -> str:
        return self.get_edge_attribute(ids=ids, attribute='type')

    @property
    def nodes(self) -> list:
        """
        Return all nodes id
        """
        return list(self.G.nodes())
    
    @property
    def edges(self) -> list:
        """
        Return all edges ids
        """
        return list(self.G.edges())

    def edges_from(self, id: int) -> list:
        """
        All edges from a node
        """
        return list(self.G.edges(id))
    
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
        
    def agents_from(self, home_id: int) -> list:
        """
        Return all family edges
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'agent' and attr.get('home_id') == home_id]
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

