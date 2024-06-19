from piperabm.society.query.add import Add
from piperabm.society.query.get import Get
from piperabm.society.query.set import Set


class Query(Add, Get, Set):
    """
    Query network elements
    """

    def has_node(self, id: int) -> bool:
        """
        Check whether the network already contains the node
        """
        return self.G.has_node(id)

    def has_edge(self, ids: list) -> bool:
        """
        Check whether the network already contains the edge
        """
        return self.G.has_edge(*ids)
    
    def pos(self, id: int, value: list = None):
        """
        Set and get for position
        """
        if value is None:
            return self.get_pos(id=id)
        else:
            self.set_pos(id=id, value=value)