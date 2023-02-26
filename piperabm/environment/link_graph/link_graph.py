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

    ######
    def all_nodes(self, node_type='all'):
        result = []
        nodes_list = list(self.G)
        if node_type == 'all':
            result = nodes_list
        else:
            for node in nodes_list:
                if self.env.node_type(node) == node_type:
                    result.append(node)
        return result

    def xy_lim(self):
        pass

    def __str__(self):
        return str(self.G)


if __name__ == "__main__":

    from piperabm import Environment
    from piperabm.unit import Date, DT
    from piperabm.degradation import DiracDelta


    env = Environment(links_unit_length=10)

    env.add_settlement(
        name="John's Home",
        pos=[-2, -2],
        initiation_date=Date(2020, 1, 2),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        initiation_date=Date(2020, 1, 4),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

    env.add_link(
        "John's Home",
        [20, 0],
        initiation_date=Date(2020, 1, 2),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_link(
        [20.3, 0.3],
        "Peter's Home",
        initiation_date=Date(2020, 1, 4),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

    start_date = Date(2020, 1, 2)
    end_date = Date(2020, 1, 15)
    env.update_elements(start_date, end_date)
    print(env.node_info(1, 'active'))
    link_graph = LinkGraph(env, start_date, end_date)
    #link_graph.show()
    print(link_graph.G)