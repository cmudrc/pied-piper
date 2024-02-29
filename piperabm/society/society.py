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
        nodes_id = self.model.agents
        edges_id = self.model.relationships
        for id in nodes_id:
            self.G.add_node(id)
        for id in edges_id:
            object = self.model.get(id)
            self.G.add_edge(object.id_1, object.id_2)

    def get(self, id: int):
        return self.model.get(id)
    
    @property
    def agents(self):
        return list(self.G.nodes())


if __name__ == "__main__":

    from piperabm.model.samples import model_3 as model

    society = model.society
    print(society.G)