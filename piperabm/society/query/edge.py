class Edge:
    """
    *** Extends Query Class ***
    Manage edge query
    """

    def all_edges(self, type='all'):
        """
        Filter all edges based on their type
        """
        result = None
        if type == 'all':
            result = list(self.G.edges())
        return result

    def get_edge_attr(self, index_start: int, index_end: int, attr: str):
        """
        Retrieve node element based on its index
        """
        result = None
        if self.G.has_edge(index_start, index_end):
            edge = self.G.edges[index_start, index_end]
            result = edge[attr]
        return result

    def get_edge_object(self, index_start: int, index_end: int):
        """
        Retrieve node element based on its index
        """
        return self.get_edge_attr(index_start, index_end, 'object')

    def oldest_edge(self):
        """
        Find the oldest edge object
        """
        oldest_edge = None
        for edge in self.all_edges():
            structure = self.get_edge_object(edge[0], edge[1])
            if structure is not None:
                start_date = structure.start_date
                if oldest_edge is None:
                    oldest_edge = edge
                current_oldest_structure = self.get_edge_object(oldest_edge[0], oldest_edge[1])
                current_oldest_date = current_oldest_structure.start_date
                if start_date < current_oldest_date:
                    oldest_edge = edge
        return oldest_edge