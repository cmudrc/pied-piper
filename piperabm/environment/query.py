class Query:
    """
    Manage query
    Extends Environment class
    """
    
    def all_indexes(self, type='all'):
        """
        Filter all node indexes based on their type
        """
        result = None
        if type == 'all':
            result = self.G.nodes()
        else:
            result = []
            for index in self.all_indexes():
                element = self.get_node_element(index)
                if element.get_type() == type:
                    result.append(index)
        return result

    def get_node_element(self, index: int):
        """
        Retrieve node element based on its index
        """
        result = None
        if self.G.has_node(index):
            result = self.G.nodes[index]['element']
        return result

    def get_edge_element(self, index_start: int, index_end: int):
        """
        Retrieve node element based on its index
        """
        result = None
        if self.G.has_edge(index_start, index_end):
            result = self.G.edges[index_start][index_end]['element']
        return result