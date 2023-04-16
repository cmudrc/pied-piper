#from piperabm.tools import euclidean_distance
from piperabm.environment.add.node import Node
from piperabm.environment.add.edge import Edge


class Add(Node, Edge):
    """
    Contains methods for Environment class
    Add new elements to the environment
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




