import numpy as np


class Query:
    """
    Contains methods for LinkGraph class
    Create a wrap-up for accessing graph data
    """
    
    def get_node_element(self, index: int):
        """
        Retrieve node element from environment based on its index
        """
        result = None
        if self.env.G.has_node(index):
            result = self.env.G.nodes[index]['element']
        return result
    
    def get_edge_element(self, index_start: int, index_end: int):
        """
        Retrieve node element from environment based on its index
        """
        result = None
        if self.env.G.has_edge(index_start, index_end):
            result = self.env.G.edges[index_start][index_end]['element']
        return result

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
    
    def find_node(self, node):
        result = None
        node_index = self.env.find_node(node)
        if node_index in self.G.nodes():
            result = node_index
        return result

    def node_degree(self, node):
        """
        Return number of edges connecting to the node
        """
        index = self.find_node(node)
        return self.G.degree[index]

    def xy_lim(self):
        """
        Resturn x and y limits of links graph based on elemets pos
        """
        x_min, x_max = None, None
        y_min, y_max = None, None
        for index in self.all_nodes():
            boundary = self.node_info(index, 'boundary')
            pos = boundary.center
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

