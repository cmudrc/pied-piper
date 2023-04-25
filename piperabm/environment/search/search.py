from piperabm.environment.search.node import Node
from piperabm.environment.search.edge import Edge


class Search(Node, Edge):
    """
    *** Extends Environment Class ***
    Methods for searching
    """

    def find(self, input):
        """
        Find and return node index based on input (name, position, or index)
        """
        result = None
        result_node = self.find_node(input)
        result_edge = None
        if result_node is not None:
            result = result_node
        elif result_edge is not None:
            result = result_edge
        return result
