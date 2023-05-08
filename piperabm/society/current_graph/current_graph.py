import networkx as nx

from piperabm.society.current_graph.to_graph import ToGraph
#from piperabm.society.current_graph.query import Query
from piperabm.society.current_graph.graphics import Graphics


class CurrentGraph(ToGraph, Graphics):
    """
    A graph quivalent to environment, but frozen in time
    """

    def __init__(self, society, start_date=None, end_date=None):
        self.society = society
        self.G = nx.Graph()
        self.to_graph(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date
        super().__init__()

    def __str__(self):
        return str(self.G)
    

if __name__ == "__main__":
    from piperabm.society.samples import society_1 as society
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    society.update(start_date, end_date)
    society.show()