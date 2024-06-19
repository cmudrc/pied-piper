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
    
    def pos(self, id: int):
        """
        Get node position
        """
        return [float(self.get_node_attribute(id, 'x', None)), float(self.get_node_attribute(id, 'y', None))]
    
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
    def junctions(self) -> list:
        """
        Return all junction nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'junction']
        except:
            return []
        
    @property
    def nonjunctions(self) -> list:
        """
        Return all nonjunction nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') != 'junction']
        except:
            return []
        
    @property
    def homes(self) -> list:
        """
        Return all homes nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'home']
        except:
            return []

    @property
    def markets(self) -> list:
        """
        Return all market nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'market']
        except:
            return []
    
    @property
    def streets(self) -> list:
        """
        Return all street edges
        """
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'street']
        except:
            return []
    
    @property
    def neighborhood_accesses(self) -> list:
        """
        Return all neighborhood access edges
        """
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'neighborhood_access']
        except:
            return []
