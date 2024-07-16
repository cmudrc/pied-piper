from piperabm.tools.nx_query import NxSet


class Set(NxSet):
    """
    Set attributes to network elements
    """

    def set_adjusted_length(self, ids: list, value: float) -> None:
        """
        Set edge *adjusted_length* value
        """
        self.set_edge_attribute(ids=ids, attribute='adjusted_length', value=value)
    
    def set_usage_impact(self, ids: list, value: float) -> None:
        """
        Set edge *usage_impact* value
        """
        self.set_edge_attribute(ids=ids, attribute='usage_impact', value=value)

    def set_climate_impact(self, ids: list, value: float) -> None:
        """
        Set edge *climate_impact* value
        """
        self.set_edge_attribute(ids=ids, attribute='climate_impact', value=value)

    def set_resource(self, id: int, name: str, value: float) -> None:
        """
        Set market *resource* value
        """
        if value <= 0:
            value = 0
        self.set_node_attribute(id=id, attribute=name, value=value)

    def set_balance(self, id: int, value: float) -> None:
        """
        Set market *balance* value
        """
        if value < 0:
            value = 0
        self.set_node_attribute(id=id, attribute='balance', value=value)