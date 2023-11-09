import networkx as nx


class ConditionConversion:

    def __init__(self):
        self.G = self.create()

    def create(self):
        G = nx.DiGraph()
        """ Add """
        G.add_edge(0, 1, type='add')
        G.add_edge(1, 2, type='add')
        G.add_edge(1, 3, type='add')
        G.add_edge(2, 4, type='add')
        G.add_edge(3, 4, type='add')
        G.add_edge(4, 5, type='add')
        """ Sub """
        G.add_edge(5, 4, type='sub')
        G.add_edge(4, 3, type='sub')
        G.add_edge(4, 2, type='sub')
        G.add_edge(3, 1, type='sub')
        G.add_edge(2, 1, type='sub')
        G.add_edge(1, 0, type='sub')
        return G

