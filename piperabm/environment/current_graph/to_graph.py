from copy import deepcopy

from piperabm.tools import ElementExists


class ToGraph:
    """
    Contains methods for LinkGraph class
    Create graph from input
    """

    def to_graph(self, start_date=None, end_date=None):
        """
        Create path graph from environment graph
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

        def validate_structure(structure, start_date, end_date) -> bool:
            result = False
            if structure is not None and \
                structure.exists(start_date, end_date) and \
                structure.active is True:
                result = True
            return result

        start_date, end_date = refine_input(start_date, end_date)
        index_list = self.env.all_indexes()

        for index in index_list:
            structure = self.env.get_node_object(index)
            valid = validate_structure(structure, start_date, end_date)
            if valid is True:
                add_node(index)
        
        for index in index_list:
            for other_index in index_list:
                if other_index != index:
                    structure = self.env.get_edge_object(index, other_index)
                    valid = validate_structure(structure, start_date, end_date)
                    if valid is True:
                        add_edge(index, other_index)
        
        for index in self.all_indexes('hub'):
            if self.node_degree(index) == 0:
                self.G.remove_node(index)
