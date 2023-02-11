import numpy as np


class Index:
    def __init__(self):
        '''node_types is node indexes gathered as list inside a dictionary based on their type'''
        self.node_types = {
            'settlement': [],
            'cross': [],
            'market': [],
        }

    def all_index(self):
        """
        Aggregate all lists of nodes in self.node_types
        """
        all_index = []
        for key in self.node_types:
            all_index += self.node_types[key]
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
        all = self.all_index()
        if len(all) > 0:
            max_index = max(all)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def random_settlement(self):
        settlement_list = self.node_types['settlement']
        rnd = np.random.choice(settlement_list, size=1)
        return rnd[0]