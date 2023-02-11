import networkx as nx
import matplotlib.pyplot as plt

from piperabm.tools import check_existance


class Path:
    def __init__(self, env, start_date=None, end_date=None):
        self.env = env
        self.G = nx.DiGraph()
        self.to_path(start_date, end_date)

    def to_path(self, start_date=None, end_date=None):
        """
        Create path graph from environment graph
        """
        def check_path_active(path, env):
            """
            Check all links within a path to see if they are all active
            """
            path_active = True
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    active = env.G[start][end]['active']
                    if active is False:
                        path_active = False
                        break
            return path_active

        def calculate_path_length(path, env):
            """
            Calculate the equivalent length of path
            """
            total_length = 0
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    length = env.G[start][end]['length']
                    difficulty = env.G[start][end]['difficulty']
                    #progressive_deg_coeff = env.G[start][end]['####']
                    adjusted_length = length * difficulty
                    total_length += adjusted_length
            return total_length   

        def node_exists(node, start_date, end_date):
            """
            Check whether the node has been already initiated
            """
            initiation_date = node['initiation_date']
            return check_existance(initiation_date, start_date, end_date)

        def check_path_exists(path, env, start_date, end_date):
            """
            Check all links within a path to see if they all exist
            """
            path_exists = True
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    initiation_date = env.G[start][end]['initiation_date']
                    exists = check_existance(initiation_date, start_date, end_date)
                    if exists is False:
                        path_exists = False
                        break
            return path_exists

        env = self.env
        index_list = env.node_types['settlement']
        index_list += env.node_types['market']
        for index in index_list:
            node = env.G.nodes[index]
            active = node['active']
            if node_exists(node, start_date, end_date) and active is True:
                name = node['name']
                pos = node['boundary'].center
                self.G.add_node(index, name=name, pos=pos)
                for other in index_list:
                    if other != index and nx.has_path(env.G, source=index, target=other):
                        path = nx.shortest_path(env.G, source=index, target=other)
                        path_active = check_path_active(path, env)
                        path_exists = check_path_exists(path, env, start_date, end_date)
                        if path_active is True and path_exists is True:
                            length = calculate_path_length(path, env)
                            self.G.add_edge(index, other, path=path, length=length)

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

    def show(self):
        pos_dict = {}
        label_dict = {}
        for index in self.G.nodes():
            node = self.G.nodes[index]
            pos = node['pos']
            pos_dict[index] = pos
            label = node['name']
            label_dict[index] = label
        nx.draw_networkx(
            self.G,
            pos=pos_dict,
            labels=label_dict
        )
        plt.show()

    def __str__(self):
        return str(self.G)

