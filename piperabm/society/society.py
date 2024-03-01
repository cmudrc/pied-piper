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
            object = self.model.get(id)
            self.G.add_node(id, alive=object.alive)
        for id in edges_id:
            object = self.model.get(id)
            self.G.add_edge(object.id_1, object.id_2)

    def get(self, id: int):
        return self.model.get(id)
    
    def edge_id(self, id_1: int, id_2: int):
        """
        Get edge id based on its id_1 and id_2 (both ends)
        """
        result = None
        if self.G.has_edge(id_1, id_2):
            edge = self.G.edges[id_1, id_2]
            result = edge['id']
        return result
    
    def edge_ids(self, id: int):
        """
        Get edge id_1 and id_2 (both ends) based on its id
        """
        result = None
        for id_1, id_2 in self.G.edges():
            if self.edge_id(id_1, id_2) == id:
                result = [id_1, id_2]
                break
        return result
    
    @property
    def edges_ids(self):
        """
        Return all edges ids
        """
        return list(self.G.edges())

    @property
    def edges_id(self):
        """
        Return all edges id
        """
        result = []
        edges = self.edges_ids
        for ids in edges:
            id = self.edge_id(*ids)
            result.append(id)
        return result
    
    @property
    def nodes_id(self):
        """
        Return all nodes id
        """
        return list(self.G.nodes())
    
    @property
    def agents(self):
        return self.nodes_id
    
    @property
    def dead_agents(self):
        return self.filter_alive(alive=False)
    
    @property
    def alive_agents(self):
        return self.filter_alive(alive=True)
    
    def agents_in(self, id: int):
        result = []
        for agent_id in self.alive_agents:
            object = self.get(agent_id)
            if object.current_node == id:
                result.append(agent_id)
        return result
    
    def node_alive(self, id: int):
        """
        Return node type
        """
        return self.G.nodes[id]['alive']
    
    def filter_alive(self, alive: bool, nodes_id: list = None):
        """
        Filter a list of nodes id based on their type
        """
        result = []
        if nodes_id is None:  # All nodes
            nodes_id = self.nodes_id
        for node_id in nodes_id:
            if self.node_alive(node_id) is alive:
                result.append(node_id)
        return result


if __name__ == "__main__":

    from piperabm.model.samples import model_1 as model

    model.create_society()
    society = model.society
    print(society.G)