from piperabm.society.query.node import Node
from piperabm.society.query.edge import Edge


class Query(Node, Edge):
    """
    *** Extends Environment Class ***
    Manage query
    """

    def oldest_date(self):
        """
        Fild the oldest date between node and edge objects
        """
        result = None
        index = self.oldest_node()
        edge = self.oldest_edge()
        if index is None and \
            edge is not None:
            structure_edge = self.get_edge_object(edge[0], edge[1])
            result = structure_edge.start_date
        elif index is not None and \
            edge is None:
            structure_index = self.get_node_object(index)
            result = structure_index.start_date
        elif index is not None and \
            edge is not None:
            structure_index = self.get_node_object(index)
            structure_edge = self.get_edge_object(edge[0], edge[1])
            if structure_index.start_date < structure_edge.start_date:
                result = structure_index.start_date
            else:
                result = structure_edge.start_date
        return result