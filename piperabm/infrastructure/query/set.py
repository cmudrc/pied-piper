class Set:

    def set_node_attr(self, id: int, attr: str, value=None) -> None:
        """
        Set node attributes in networkx graph
        """
        self.G.nodes[id][attr] = value

    def set_edge_attr(self, ids: list, attr: str, value=None) -> None:
        """
        Set edge attributes in networkx graph
        """
        self.G[ids[0]][ids[1]][attr] = value

