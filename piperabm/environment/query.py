import numpy as np


class Query:
    """
    Contains methods for Environment class
    Create a wrap-up for accessing graph data
    """

    def all_nodes(self, type='all'):
        """
        Aggregate all lists of nodes in self.node_types
        """
        all_index = []
        if type == 'all':
            for key in self.node_types:
                all_index += self.node_types[key]
        else:
            all_index = self.node_types[type]
        return all_index

    def node_type(self, index):
        """
        Find node type based on its index
        """
        result = None
        for key in self.node_types:
            if index in self.node_types[key]:
                result = key
                break
        return result

    def random_node(self, nodes_list: list):
        """
        Generate random index from *nodes_list*
        """
        rnd = np.random.choice(nodes_list, size=1)
        return int(rnd[0])

    def random_settlement(self):
        """
        Generate a random index from settlements
        """
        settlement_list = self.all_nodes('settlement')
        return self.random_node(settlement_list)

    def node_info(self, node, property):
        """
        Return *property* of *node*
        """
        node_index = self.find_node(node)
        node = self.G.nodes[node_index]
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

    def sort_nodes_distance(self, node, other_nodes: list):
        """
        sort *other_nodes* based on their distance from *node*
        """
        node_index = self.find_node(node)
        distances = {} # in form of {node: distance}
        for node in other_nodes:
            dist = None ###
            distances[node] = dist
        ## sort
        return

    def oldest_date(self):
        """
        Find oldest node (which is not a cross type)
        """
        oldest_date = None
        for key in self.node_types:
            if key != 'cross':
                for index in self.node_types[key]:
                    node = self.G.nodes[index]
                    initiation_date = node['initiation_date']
                    if oldest_date is None:
                        oldest_date = initiation_date
                    elif initiation_date < oldest_date:
                        oldest_date = initiation_date
        return oldest_date