import numpy as np


class Query:
    """
    Contains methods for PathGraph class
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
        if node is None:
            result = self.G.edges()
        else:
            node_index = self.find_node(node)
            result = self.G.out_edges(node_index)
        return result

    def node_info(self, node, property):
        """
        Return *property* of *node*
        """
        node_index = self.find_node(node)
        node = self.env.G.nodes[node_index]
        return node[property]

    def edge_info(self, start, end, property):
        """
        Return *property* of edge between *start* and *end*
        """
        result = None
        start_index = self.find_node(start)
        end_index = self.find_node(end)
        if start_index is not None and end_index is not None:
            if self.G.has_edge(start_index, end_index):
                result = self.G[start_index][end_index][property]
        return result

    def find_node(self, node):
        return self.env.find_node(node)

