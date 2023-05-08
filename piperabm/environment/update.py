class Update:
    """
    *** Extends Environment Class ***
    Methods for updating environment elements in each step
    """

    def update(self, start_date, end_date) -> None:
        """
        Update all active non-None elements
        """
        ''' filter current elements '''
        self.to_current_graph(start_date, end_date)
        ''' update current elements '''
        for index in self.current.all_indexes():
            object = self.get_node_object(index)
            if object is not None:
                object.update(start_date, end_date)
        for edge in self.current.all_edges():
            object = self.get_edge_object(edge[0], edge[1])
            if object is not None:
                object.update(start_date, end_date)
        