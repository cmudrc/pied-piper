class Node:
    """
    *** Extends Query Class ***
    Manage node query
    """

    def all_indexes(self, type='all'):
        """
        Filter all nodes based on their type
        """
        result = None
        if type == 'all':
            result = list(self.G.nodes())
        return result
    
    def agents_from_origin(self, origin):
        result = []
        for index in self.all_indexes():
            agent = self.get_agent_object(index)
            if origin == agent.origin:
                result.append(index)
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
        return self.get_node_attr(index, 'object')
    
    def get_agent_object(self, index: int):
        """
        An alias for intuition
        """
        return self.get_node_object(index)
    
    def get_node_pos(self, index: int):
        """
        Retrieve node element based on its index
        """
        return self.get_node_attr(index, 'pos')
    
    def get_agent_pos(self, index: int):
        """
        An alias for intuition
        """
        return self.get_node_pos(index)
    
    def oldest_node(self):
        """
        Find the oldest node object
        """
        oldest_index = None
        for index in self.all_indexes():
            object = self.get_node_object(index)
            if object is not None:
                start_date = object.start_date
                if oldest_index is None:
                    oldest_index = index
                current_oldest_object = self.get_node_object(oldest_index)
                current_oldest_date = current_oldest_object.start_date
                if start_date < current_oldest_date:
                    oldest_index = index
        return oldest_index