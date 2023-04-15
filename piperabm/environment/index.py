import numpy as np


class Index:
    """
    Contains methods for Environment class
    Manage nodes index
    """

    def find_next_index(self):
        """
        Check all indexes in self.node_types dictionary and suggest a new index
        """
        all = self.all_indexes()
        if len(all) > 0:
            max_index = max(all)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def get_node_object(self, index: int):
        """
        Retrieve node object based on its index
        """
        try:
            result = self.G.nodes[index]['element']
        except:
            result = None
        return result
    
    def get_node_objects(self, indexes: list):
        result = []
        for index in indexes:
            object = self.get_node_object(index)
            result.append(object)
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
                element = self.get_node_object(index)
                if element.get_type() == type:
                    result.append(index)
        return result