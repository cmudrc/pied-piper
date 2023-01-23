import networkx as nx
from piperabm import Environment

from piperabm.unit import DT, Date
from piperabm.actions import Queue, Move
from piperabm.tools import euclidean_distance


class Society:
    def __init__(self, env: Environment):
        self.env = env
        self.G = nx.Graph()
        self.index_list = []

    def find_next_index(self):
        """
        Check self.index_list (indexes) and suggest a new index
        """
        index_list = self.index_list
        if len(index_list) > 0:
            max_index = max(index_list)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def add_agent(self):
        index = self.find_next_index()
        self.index_list.append(index)
        settlement_index = self.env.random_settlement()
        settlement_node = self.env.G.nodes[settlement_index]
        pos = settlement_node['boundary'].center
        self.G.add_node(
            index,
            settlement=settlement_index,
            pos=pos,
            queue=Queue()
            )

    def update_agents(self, start_date, end_date):
        pass

    def add_agents(self, n):
        for _ in range(n):
            self.add_agent()

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


if __name__ == "__main__":
    from piperabm.unit import Unit, Date
    from piperabm.actions import Move, Walk

    m = Move(
        start_date=Date(2020, 1, 1),
        start_pos=[0, 0],
        end_pos=[10000, 10000],
        adjusted_length=20000,
        transportation=Walk()
        )
    print(m.end_date)
    print(m.pos(date=Date(2020, 1, 1)+DT(hours=1)))
