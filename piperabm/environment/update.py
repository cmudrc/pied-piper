class Update:
    """
    *** Extends Environment Class ***
    Methods for updating environment elements in each step
    """

    def update(self, start_date, end_date):
        """
        Update all active non-None elements
        """
        indexes = self.all_indexes()
        for index in indexes:
            structure = self.get_node_object(index)
            if structure is not None and \
                structure.active is True:
                structure.update(start_date, end_date)
        edges = self.all_edges()
        for edge in edges:
            structure = self.get_edge_object(edge[0], edge[1])
            if structure is not None and \
                structure.active is True:
                structure.update(start_date, end_date)
        ##### stat
        