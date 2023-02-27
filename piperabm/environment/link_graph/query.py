import numpy as np


class Query:
    """
    Contains methods for LinkGraph class
    Create a wrap-up for accessing graph data
    """

    def all_nodes(self, type='all'):
        """
        Aggregate all lists of nodes in self.node_types
        """
        all_index = []
        nodes_list = list(self.G)
        if type == 'all':
            all_index = nodes_list
        else:
            for node in nodes_list:
                if type == self.env.node_type(node):
                    all_index.append(node)
        return all_index

    def all_edges(self, node=None):
        """
        Return a list of all edges if *node* is None, and if *node* is provided,
        return a list of edges that connect to the *node*
        """
        result = None
        if node in None:
            result = self.G.edges()
        else:
            result = self.G.out_edges(node)
        return result

    def node_info(self, node, property):
        """
        Return *property* of *node*
        """
        node_index = self.env.find_node(node)
        node = self.env.G.nodes[node_index]
        return node[property]

    def edge_info(self, start, end, property):
        """
        Return *property* of edge between *start* and *end*
        """
        result = None
        start_index = self.env.find_node(start)
        end_index = self.env.find_node(end)
        if start_index is not None and end_index is not None:
            if self.G.has_edge(start_index, end_index):
                result = self.G[start_index][end_index][property]
        return result

    def node_degree(self, node):
        """
        Return number of edges connecting to the node
        """
        index = self.env.find_node(node)
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

