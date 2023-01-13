import networkx as nx


class Society:
    def __init__(self, env):
        self.L = env
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
        settlement_index = self.L.random_settlement()
        settlement_node = self.L.G.nodes[settlement_index]
        pos = settlement_node['boundary'].center
        self.G.add_node(
            index,
            settlement=settlement_index,
            pos=pos
            )

    def add_agents(self, n):
        for _ in range(n):
            self.add_agent()
