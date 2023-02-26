import networkx as nx

try: from .to_graph import ToGraph
except: from to_graph import ToGraph
try: from .graphics import Graphics
except: from graphics import Graphics


class LinkGraph(ToGraph, Graphics):
    def __init__(self, env, start_date=None, end_date=None):
        self.env = env
        self.G = nx.Graph()
        self.to_graph(start_date, end_date)

    def from_node_perspective(self, node):
        return self.G.out_edges(node)

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

    def __str__(self):
        return str(self.G)
