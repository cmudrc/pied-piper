class Query:
    """
    *** Extends Environment Class ***
    Manage query
    """
    
    def all_indexes(self, type='all'):
        """
        Filter all nodes based on their type
        """
        result = None
        if type == 'all':
            result = list(self.G.nodes())
        elif type == 'hub':
            result = []
            for index in self.all_indexes():
                structure = self.get_node_object(index)
                if structure is None:
                    result.append(index)
        else:
            result = []
            for index in self.all_indexes():
                structure = self.get_node_object(index)
                if structure is not None and \
                    structure.type == type:
                    result.append(index)
        return result
    
    def all_edges(self, type='all'):
        """
        Filter all edges based on their type
        """
        result = None
        if type == 'all':
            result = list(self.G.edges())
        return result

    def get_node_attr(self, index: int, attr: str):
        result = None
        if self.G.has_node(index):
            node = self.G.nodes[index] 
            result = node[attr]
        return result 

    def get_node_object(self, index: int):
        """
        Retrieve node element based on its index
        """
        return self.get_node_attr(index, 'structure')
    
    def get_node_pos(self, index: int):
        """
        Retrieve node element based on its index
        """
        return self.get_node_attr(index, 'pos')

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
        return self.get_edge_attr(index_start, index_end, 'structure')

    def get_edge_pos(self, index_start: int, index_end: int):
        """
        Retrieve node element based on its index
        """
        return self.get_edge_attr(index_start, index_end, 'pos')