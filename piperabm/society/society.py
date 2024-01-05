import networkx as nx
import numpy as np


class Society:

    def __init__(self, model):
        self.G = nx.Graph()
        self.model = model
        self.create()

    def create(self):
        """
        Create graph *G* from *self.model*
        """
        #all_nodes_alive = self.model.all_alive_agents
        #all_nodes_dead = self.model.all_dead_agents
        all_nodes = self.model.all_agents
        all_edges = self.model.all_relationships
        for item_index in all_nodes:
            self.G.add_node(item_index)
        for item_index in all_edges:
            item = self.model.get(item_index)
            self.G.add_edge(item.index_1, item.index_2)

    def get(self, index: int):
        return self.model.get(index)
    
    @property
    def agents(self):
        return list(self.G.nodes())


if __name__ == "__main__":

    from piperabm.model.samples import model_3 as model

    society = model.society
    print(society.G)