import numpy as np


class Query:
    """
    *** Extends CurrentGraph Class ***
    Create a wrap-up for accessing graph data
    """
    
    def get_node_object(self, index: int):
        """
        Retrieve node element from environment based on its index
        """
        result = None
        if index in self.all_indexes():
            result = self.env.get_node_object(index)
        return result
    
    def get_node_pos(self, index: int):
        """
        Retrieve node element from environment based on its index
        """
        result = None
        if index in self.all_indexes():
            result = self.env.get_node_pos(index)
        return result
    
    def get_edge_object(self, index_start: int, index_end: int):
        """
        Retrieve node element from environment based on its index
        """
        result = None
        if index_start in self.all_indexes() and \
            index_end in self.all_indexes():
            result = self.env.get_edge_object(index_start, index_end)
        return result
    
    def get_edge_pos(self, index_start: int, index_end: int):
        """
        Retrieve node element from environment based on its index
        """
        result = None
        if index_start in self.all_indexes() and \
            index_end in self.all_indexes():
            result = self.env.get_edge_pos(index_start, index_end)
        return result
    
    def all_indexes(self, type='all'):
        """
        Filter all node indexes based on their type
        """
        result = None
        if type == 'all':
            result = self.G.nodes()
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
    
    def find_node(self, node):
        result = None
        node_index = self.env.find_node(node)
        if node_index in self.all_indexes():
            result = node_index
        return result

    def node_degree(self, index):
        """
        Return number of edges connecting to the node
        """
        result = None
        if index in self.all_indexes():
            result = self.G.degree[index]
        return result

    def xy_lim(self):
        """
        Resturn x and y limits of links graph based on elemets pos
        """
        x_min, x_max = None, None
        y_min, y_max = None, None
        for index in self.all_indexes():
            pos = self.get_node_pos(index)
            x = pos[0]
            y = pos[1]
            if x_max is None: x_max = x
            elif x > x_max: x_max = x
            if x_min is None: x_min = x
            elif x < x_min: x_min = x
            if y_max is None: y_max = y
            elif y > y_max: y_max = y
            if y_min is None: y_min = y
            elif y < y_min: y_min = y
        y_lim = [y_min, y_max]
        x_lim = [x_min, x_max]
        return x_lim, y_lim

    def size(self):
        """
        Return size of environment
        """
        x_lim, y_lim = self.xy_lim()
        x_size = x_lim[1] - x_lim[0]
        y_size = y_lim[1] - y_lim[0]
        size = [x_size, y_size]
        return size

