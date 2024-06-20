from piperabm.tools.nx_query import NxSet


class Set(NxSet):
    """
    Set attributes to network elements
    """

    def set_pos(self, id: int, value: list):
        """
        Set node position
        """
        x = float(value[0])
        y = float(value[1])
        self.set_node_attribute(id=id, attribute='x', value=x)
        self.set_node_attribute(id=id, attribute='y', value=y)
