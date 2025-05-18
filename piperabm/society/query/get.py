from piperabm.tools.nx_query import NxGet


class Get(NxGet):
    """
    Get attributes from network elements
    """

    def get_action_queue(self, id: int):
        """
        Get agent action queue
        """
        return self.actions[id]
    
    def get_pos(self, id: int):
        """
        Get node position value
        """
        return [self.get_node_attribute(id, 'x', None), self.get_node_attribute(id, 'y', None)]
    
    def get_node_type(self, id: int) -> str:
        """
        Get node *type* value
        """
        return self.get_node_attribute(id=id, attribute='type')

    def get_edge_type(self, ids: list) -> str:
        """
        Get edge *type* value
        """
        return self.get_edge_attribute(ids=ids, attribute='type')
    
    def get_node_name(self, id: int) -> str:
        """
        Get node *name* value
        """
        return self.get_node_attribute(id=id, attribute='name')
    
    def get_edge_name(self, ids: list) -> str:
        """
        Get edge *name* value
        """
        return self.get_edge_attribute(ids=ids, attribute='name')
    
    def get_resource(self, id: int, name: str) -> float:
        """
        Get agent *resource* value
        """
        return self.get_node_attribute(id=id, attribute=name)
    
    def get_resources(self, id: int) -> dict:
        """
        Get agent resources value
        """
        result = {}
        for name in self.resource_names:
            result[name] = self.get_resource(id=id, name=name)
        return result
    
    def get_enough_resource(self, id: int, name: str) -> float:
        """
        Get agent *enough_resource* value
        """
        attribute = 'enough_' + name
        return self.get_node_attribute(id=id, attribute=attribute)

    def get_alive(self, id: str) -> bool:
        """
        Get agent *alive* value
        """
        return self.get_node_attribute(id=id, attribute='alive')
    
    def get_socioeconomic_status(self, id: str) -> bool:
        """
        Get agent *socioeconomic_status* value
        """
        return self.get_node_attribute(id=id, attribute='socioeconomic_status')
    
    def get_income(self, id: str) -> float:
        """
        Get agent *income* value
        """
        return self.get_socioeconomic_status(id=id) * self.average_income
    
    def get_current_node(self, id: str) -> int:
        """
        Get agent *current_node* value
        """
        return self.get_node_attribute(id=id, attribute='current_node')
    
    def get_home_id(self, id: str) -> int:
        """
        Get agent *home_id* value
        """
        return self.get_node_attribute(id=id, attribute='home_id')
    
    def get_balance(self, id: int) -> float:
        """
        Get agent *balance* value
        """
        return self.get_node_attribute(id=id, attribute='balance')