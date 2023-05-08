class ToGraph:
    """
    *** Extends CurrentGraph Class ***
    Create graph from input
    """

    def to_graph(self, start_date=None, end_date=None):
        """
        Create current graph from environment graph
        """
        def add_node(index):
            """
            Add node to the graph
            """
            self.G.add_node(index)

        def add_edge(index, other_index):
            """
            Add edge to the graph
            """
            self.G.add_edge(index, other_index)

        def refine_input(start_date, end_date):
            """
            Refine inputs
            """
            '''
            def swap(start, end):
                temp = None
                if start > end:
                    temp = deepcopy(start)
                    start = deepcopy(end)
                    end = deepcopy(temp)
                return start, end
            '''

            if end_date is None:
                if start_date is not None:
                    end_date = start_date
            return start_date, end_date

        def validate_structure(structure, start_date, end_date, accept_none=False) -> bool:
            """
            Is it valid to get added to the current graph?
            """
            result = False
            if structure is None:
                if accept_none is True:
                    result = True
                else:
                    result = False
            else:
                if structure.exists(start_date, end_date) and \
                        structure.active is True:
                    result = True
            return result

        start_date, end_date = refine_input(start_date, end_date)

        ''' Filter nodes '''
        indexes = self.env.all_indexes()
        for index in indexes:
            structure = self.env.get_node_object(index)
            valid = validate_structure(
                structure,
                start_date,
                end_date,
                accept_none=True
            )
            if valid is True:
                add_node(index)

        ''' Filter edges '''
        edges = self.env.all_edges()
        for edge in edges:
            index = edge[0]
            other_index = edge[1]
            structure = self.env.get_edge_object(index, other_index)
            valid = validate_structure(
                structure,
                start_date,
                end_date,
                accept_none=False
            )
            if valid is True:
                add_edge(index, other_index)

        ''' Remove nodes without structure object (hub) and without any edges attachted '''
        for index in self.all_indexes('hub'):
            if self.node_degree(index) == 0:
                self.G.remove_node(index)
