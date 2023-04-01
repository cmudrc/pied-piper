import networkx as nx

try: from .to_graph import ToGraph
except: from to_graph import ToGraph
try: from .query import Query
except: from query import Query
try: from .graphics import Graphics
except: from graphics import Graphics


class PathGraph(ToGraph, Query, Graphics):
    def __init__(self, links_graph):
        self.env = links_graph.env
        self.G = nx.DiGraph()
        self.to_graph(links_graph)
        self.start_date = links_graph.start_date
        self.end_date = links_graph.end_date

    def from_node_perspective(self, node):
        result = []
        node_index = self.find_node(node)
        if node_index is not None:
            if node_index in self.G.nodes():
                result = list(self.G.out_edges(node_index))
        return result
    
    def __str__(self):
        return str(self.G)


if __name__ == "__main__":
    from piperabm.unit import Date
    from piperabm.environment.sample import env_0 as env
    from piperabm.environment.link_graph import LinkGraph

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    env.update_elements(start_date, end_date)
    link_graph = LinkGraph(env, start_date, end_date)
    path_graph = PathGraph(link_graph)
    path_graph.show()