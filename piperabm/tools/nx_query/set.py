class NxSet:
    """
    General set methods for networkx
    """

    def set_node_attribute(self, id: int, attribute: str, value=None) -> None:
        """
        Set node attribute in networkx graph
        """
        self.G.nodes[id][attribute] = value

    def set_edge_attribute(self, ids: list, attribute: str, value=None) -> None:
        """
        Set edge attribute in networkx graph
        """
        self.G[ids[0]][ids[1]][attribute] = value