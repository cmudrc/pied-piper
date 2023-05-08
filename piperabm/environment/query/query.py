from piperabm.environment.query.node import Node
from piperabm.environment.query.edge import Edge


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
            edge_object = self.get_edge_object(edge[0], edge[1])
            result = edge_object.start_date
        elif index is not None and \
            edge is None:
            node_object = self.get_node_object(index)
            result = node_object.start_date
        elif index is not None and \
            edge is not None:
            node_object = self.get_node_object(index)
            edge_object = self.get_edge_object(edge[0], edge[1])
            if node_object.start_date < edge_object.start_date:
                result = node_object.start_date
            else:
                result = edge_object.start_date
        return result