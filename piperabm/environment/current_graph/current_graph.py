import networkx as nx

from piperabm.environment.current_graph.to_graph import ToGraph
from piperabm.environment.current_graph.query import Query
from piperabm.environment.current_graph.graphics import Graphics
from piperabm.environment.current_graph.path_graph import PathGraph


class CurrentGraph(ToGraph, Query, Graphics):
    """
    A graph quivalent to environment, but frozen in time
    """

    def __init__(self, environment, start_date=None, end_date=None):
        self.env = environment
        self.G = nx.Graph()
        self.to_graph(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date
        super().__init__()

    def to_path_graph(self):
        """
        Convert the environment to PathGraph object
        """
        return PathGraph(self)
    
    def __str__(self):
        return str(self.G)


if __name__ == "__main__":
    from piperabm.environment.samples import environment_1 as environment
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    environment.update(start_date, end_date)
    environment.show()
