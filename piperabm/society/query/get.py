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

