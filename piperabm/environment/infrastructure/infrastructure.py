import networkx as nx

from piperabm.object import PureObject
from piperabm.environment.infrastructure.graphics import Graphics


class Infrastructure(PureObject, Graphics):

    def __init__(self, environment):
        super().__init__()
        self.G = nx.Graph()
        self.environment = environment

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
    
    def all_nodes(self):
        return list(self.G.nodes())
    
    def all_edges(self):
        return list(self.G.edges())
    

if __name__ == "__main__":

    from piperabm.environment.samples import environment_1 as env
    from piperabm.time import Date


    date_start = Date(2020, 1, 1)
    date_end = Date(2020, 1, 2)
    infrastructure = env.to_infrastrucure_graph(date_start, date_end)
    infrastructure.show()