class Edge:
    """
    *** Extends Search Class ***
    Methods for searching for edge
    """

    def _find_edge_by_name(self, name: str):
        """
        Find and return settlement node index by its name property
        """
        result = None
        if len(name) > 0: # to avoid: (name='')
            edges = self.all_edges()
            for edge in edges:
                structure = self.get_edge_object(edge[0], edge[1])
                if structure is not None and structure.name == name:
                    result = edge
                    break
        return result

    def _find_edge_by_pos(self, pos: list):
        """
        Find and return node index by its position
        """
        result = None
        edges = self.all_edges()
        for edge in edges:
            center_pos = self.get_edge_pos(edge[0], edge[1])
            structure = self.get_edge_object(edge[0], edge[1])
            if center_pos is not None and center_pos == pos:
                result = edge
                break
            if structure is not None and structure.is_in(pos, center=center_pos, local=False) is True:
                result = edge
                break
        return result

    def find_edge(self, input):
        """
        Find and return node index based on input (name, position, or index)
        """
        result = None
        if isinstance(input, str):
            result = self._find_edge_by_name(input)
        elif isinstance(input, list):
            result = self._find_edge_by_pos(input)
        return result