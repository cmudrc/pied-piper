from piperabm.tools.nx_query import NxGet


class Get(NxGet):
    """
    Get attributes from network elements
    """
    
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
