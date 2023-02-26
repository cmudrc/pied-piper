import numpy as np


class Index:
    def __init__(self):
        '''node_types is node indexes gathered as list inside a dictionary based on their type'''
        self.node_types = {
            'settlement': [],
            'cross': [],
            'market': [],
        }

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

    def find_next_index(self):
        """
        Check all indexes in self.node_types dictionary and suggest a new index
        """
        all = self.all_nodes()
        if len(all) > 0:
            max_index = max(all)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

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
        settlement_list = self.node_types['settlement']
        return self.random_node(settlement_list)

    def edge_info(self, start, end, property):
        """
        Return *property* of edge between *start* and *end*
        """
        result = None
        start = self.find_node(start)
        end = self.find_node(end)
        if start is not None and end is not None:
            if self.G.has_edge(start, end):
                result = self.G[start][end][property]
        return result

    def settlement_info(self, node, property):
        """
        Return *property* of settlement *node*
        """
        result = None
        node_index = self.find_node(node)
        node_type = self.node_type(node_index)
        if node_index is not None and node_type == 'settlement':
            node = self.G.nodes[node_index]
            result = node[property]
        return result

    def node_info(self, node_index, property):
        """
        Return *property* of all types of nodes
        """
        node = self.G.nodes[node_index]
        return node[property]

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

    def filter_nodes(self, nodes: list, n=1):
        """
        filter nodes based on the number of their connecting links
        """
        result = []
        for node in nodes:
            node_index = self.find_node(node)
            count = self.G.degree(node_index)
            if count > n:
                result.append(node_index)
        return result

        