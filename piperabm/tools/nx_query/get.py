class NxGet:
    """
    General get methods for networkx
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
