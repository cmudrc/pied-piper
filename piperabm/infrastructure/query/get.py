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
    
    def get_node_type(self, id: int) -> str:
        """
        Get node type
        """
        return self.get_node_attribute(id=id, attribute='type')

    def get_edge_type(self, ids: list) -> str:
        """
        Get edge type
        """
        return self.get_edge_attribute(ids=ids, attribute='type')    

    def get_node_name(self, id: int) -> str:
        """
        Get node name
        """
        return self.get_node_attribute(id=id, attribute='name')
    
    def get_edge_name(self, ids: list) -> str:
        """
        Get edge name
        """
        return self.get_edge_attribute(ids=ids, attribute='name')
    
    def get_length(self, ids: list) -> float:
        """
        Get edges length
        """
        return self.get_edge_attribute(ids=ids, attribute='length')
    
    def get_adjusted_length(self, ids: list) -> float:
        """
        Get edges *adjusted_length*
        """
        return self.get_edge_attribute(ids=ids, attribute='adjusted_length')
    
    def get_usage_impact(self, ids: list) -> float:
        """
        Get edges *usage_impact*
        """
        return self.get_edge_attribute(ids=ids, attribute='usage_impact')
    
    def get_climate_impact(self, ids: list) -> float:
        """
        Get edges *climate_impact*
        """
        return self.get_edge_attribute(ids=ids, attribute='climate_impact')
    
    def get_resource(self, id: int, name: str) -> float:
        """
        Get market *resource* value
        """
        return self.get_node_attribute(id=id, attribute=name)
    
    def get_enough_resource(self, id: int, name: str) -> float:
        """
        Get market *enough_resource* value
        """
        attribute = 'enough_' + name
        return self.get_node_attribute(id=id, attribute=attribute)
    
    def get_balance(self, id: int) -> float:
        """
        Get market *balance* value
        """
        return self.get_node_attribute(id=id, attribute='balance')
