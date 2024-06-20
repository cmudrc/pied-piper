from piperabm.tools.nx_query import NxSet


class Set(NxSet):
    """
    Set attributes to network elements
    """

    def set_pos(self, id: int, value: list) -> None:
        """
        Set node position
        """
        x = float(value[0])
        y = float(value[1])
        self.set_node_attribute(id=id, attribute='x', value=x)
        self.set_node_attribute(id=id, attribute='y', value=y)

    def set_resource(self, name: str, id: int, value: float) -> None:
        if value <= 0:
            value = 0
            self.set_node_attribute(id=id, attribute='alive', value=False)
        self.set_node_attribute(id=id, attribute=name, value=value)

    def set_current_node(self, id: str, value: int) -> None:
        return self.set_node_attribute(id=id, attribute='current_node', value=value)
    
    def set_balance(self, id: str, value: float) -> None:
        return self.set_node_attribute(id=id, attribute='balance', value=value)
    