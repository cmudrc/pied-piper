class Get:

    def get_node_attr(self, id: int, attr: str, default=None):
        """
        Get node attributes from networkx graph
        """
        return self.G.nodes[id].get(attr, default)
    
    def get_edge_attr(self, ids: list, attr: str, default=None):
        """
        Get edge attributes from networkx graph
        """
        return self.G.edges[*ids].get(attr, default)
    
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
