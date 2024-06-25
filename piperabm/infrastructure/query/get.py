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
    
    def get_length(self, ids: list) -> float:
        return self.get_edge_attribute(ids=ids, attribute='length')
    
    def get_adjusted_length(self, ids: list) -> float:
        return self.get_edge_attribute(ids=ids, attribute='adjusted_length')
    
    def get_usage_impact(self, ids: list) -> float:
        return self.get_edge_attribute(ids=ids, attribute='usage_impact')
    
    def get_resource(self, name: str, id: int) -> float:
        return self.get_node_attribute(id=id, attribute=name)
