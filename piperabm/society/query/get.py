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
        return self.get_node_attribute(id=id, attribute='type')

    def get_edge_type(self, ids: list) -> str:
        return self.get_edge_attribute(ids=ids, attribute='type')
    
    def get_resource(self, name: str, id: int) -> float:
        return self.get_node_attribute(id=id, attribute=name)
    
    def get_enough_resource(self, name: str, id: int) -> float:
        attribute = 'enough_' + name
        return self.get_node_attribute(id=id, attribute=attribute)
    
    def get_idle_fuel_rate(self, name: str, id: int) -> float:
        attribute = 'idle_' + name + '_rate'
        return self.get_node_attribute(id=id, attribute=attribute)

    def get_transportation_fuel_rate(self, name: str, id: int) -> float:
        attribute = 'transportation_' + name + '_rate'
        return self.get_node_attribute(id=id, attribute=attribute)

    def get_transportation_speed(self, id: int) -> float:
        return self.get_node_attribute(id=id, attribute='speed')

    def get_alive(self, id: str) -> bool:
        return self.get_node_attribute(id=id, attribute='alive')
    
    def get_socioeconomic_status(self, id: str) -> bool:
        return self.get_node_attribute(id=id, attribute='socioeconomic_statu')
    
    def get_income(self, id: str) -> float:
        return self.get_socioeconomic_status(id=id) * self.average_income
    
    def get_current_node(self, id: str) -> int:
        return self.get_node_attribute(id=id, attribute='current_node')
    
    def get_home_id(self, id: str) -> int:
        return self.get_node_attribute(id=id, attribute='home_id')
    
    def get_balance(self, id: int) -> float:
        return self.get_node_attribute(id=id, attribute='balance')
    
    def get_max_time_outside(self, id: int):
        return self.get_node_attribute(id=id, attribute='max_time_outside')