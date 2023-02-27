import networkx as nx

from piperabm.environment.path_graph import PathGraph
try: from .to_graph import ToGraph
except: from to_graph import ToGraph
try: from .query import Query
except: from query import Query
try: from .graphics import Graphics
except: from graphics import Graphics


class LinkGraph(ToGraph, Query, Graphics):
    """
    A graph quivalent to environment, but frozen in time
    """

    def __init__(self, env, start_date=None, end_date=None):
        self.env = env
        self.G = nx.Graph()
        self.to_graph(start_date, end_date)

    def to_path_graph(self):
        """
        Convert the environment to PathGraph object
        """
        return PathGraph(self)

    def __str__(self):
        return str(self.G)


if __name__ == "__main__":
    from piperabm.unit import Date
    from piperabm.environment.sample import env_0 as env

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    env.update_elements(start_date, end_date)
    link_graph = LinkGraph(env, start_date, end_date)
    link_graph.show()
