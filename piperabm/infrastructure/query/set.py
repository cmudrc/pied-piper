from piperabm.tools.nx_query import NxSet


class Set(NxSet):
    """
    Set attributes to network elements
    """

    def set_adjusted_length(self, ids: list, value: float) -> None:
        self.set_edge_attribute(ids=ids, attribute='adjusted_length', value=value)
    
    def set_usage_impact(self, ids: list, value: float):
        self.set_edge_attribute(ids=ids, attribute='usage_impact', value=value)

    def set_resource(self, name: str, id: int, value: float):
        if value <= 0:
            value = 0
        self.set_node_attribute(id=id, attribute=name, value=value)