import networkx as nx

from piperabm.object import PureObject

class Infrastructure(PureObject):

    def __init__(self):
        super().__init__()
        self.G = nx.Graph()
        self.environment = None

    def add_node(self, item_index):
        self.G.add_node(
            item_index
        )

    def add_edge(self, index_1, index_2, item_index):
        self.G.add_edge(
            index_1,
            index_2,
            index=item_index
        )

    def get_node_item(self, index):
        return self.environment.item(index)
    
    def get_edge_item(self, index_1, index_2):
        edge = self.G.edges[index_1, index_2]
        index = edge['index']
        return self.environment.item(index)