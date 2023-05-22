import networkx as nx

from piperabm.environment.current_graph.path_graph.to_graph import ToGraph
from piperabm.environment.current_graph.path_graph.query import Query
from piperabm.environment.current_graph.path_graph.graphics import Graphics


class PathGraph(ToGraph, Query, Graphics):

    def __init__(self, current_environment):
        self.current_environment = current_environment.to_active_graph()
        self.G = nx.Graph()
        self.to_graph(current_environment)
        super().__init__()


if __name__ == "__main__":
    from piperabm.environment.samples import environment_1 as environment
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    environment.update(start_date, end_date)
    path_graph = environment.current.to_path_graph()
    path_graph.show()