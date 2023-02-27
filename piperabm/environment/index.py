import numpy as np


class Index:
    """
    Contains methods for Environment class
    Manage nodes index
    """

    def __init__(self):
        '''node_types is node indexes gathered as list inside a dictionary based on their type'''
        self.node_types = {
            'settlement': [],
            'cross': [],
            'market': [],
        }

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

        