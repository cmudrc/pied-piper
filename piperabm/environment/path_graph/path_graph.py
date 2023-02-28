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

    def from_node_perspective(self, node):
        return self.G.out_edges(node)
    '''
    def path_to_pos(self, path: list):
        """
        Convert edge path data to a list of pos
        """
        pos_list = []
        for index in path:
            node = self.env.G.nodes[index]
            pos = node['boundary'].center
            pos_list.append(pos)
        return pos_list

    def path_real_length_list(self, path: list):
        """
        Convert edge path data to a list of real length
        """
        real_length_list = []
        for index in path:
            node = self.env.G.nodes[index]
            length = node['length']
            real_length_list.append(length)
        return real_length_list

    def route_info(self, start, end, property):
        """
        Return *property* of edge between *start* and *end*
        """
        start = self.env.find_node(start)
        end = self.env.find_node(end)
        if start is not None and end is not None:
            result = self.G[start][end][property]
        else:
            result = None
        return result
    '''
    
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