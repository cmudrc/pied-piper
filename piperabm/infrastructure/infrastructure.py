import networkx as nx

from piperabm.infrastructure.paths import Paths
from piperabm.graphics import Graphics


class Infrastructure:

    def __init__(self, model=None):
        self.G = nx.Graph()
        self.model = model
        if self.model is not None:
            self.create()

    def create(self):
        """
        Create graph from model
        """
        self.G = nx.Graph()
        for id in self.model.infrastructure_nodes:
            self.add_node(id)
        for id in self.model.infrastructure_edges:
            object = self.get(id)
            self.add_edge(
                id_1=object.id_1,
                id_2=object.id_2,
                id=id,
                adjusted_length=object.adjusted_length
            )
        
        self.margins = self.xylim()

    def get(self, id: int):
        """
        Get object
        """
        return self.model.get(id)
    
    @property
    def proximity_radius(self):
        return self.model.proximity_radius

    def add_node(self, id: int):
        """
        Add a node based on its id
        """
        self.G.add_node(id)

    def add_edge(self, id_1: int, id_2: int, id: int, adjusted_length: float = None):
        """
        Add an edge based on its id_1 and id_2 (both ends), together with its id
        """
        self.G.add_edge(id_1, id_2, id=id, adjusted_length=adjusted_length)

    def remove_node(self, id: int):
        """
        Remove a node based on its id
        """
        self.G.remove_node(id)

    def remove_edge(self, id_1: int, id_2: int):
        """
        Remove an edge based on its id_1 and id_2 (both ends)
        """
        self.G.remove_edge(id_1, id_2)

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
    
    def filter_type(self, type, nodes_id=None):
        """
        Filter a list of nodes id based on their type
        """
        result = []
        if nodes_id is None:  # All nodes
            nodes_id = self.nodes_id
        for node_id in nodes_id:
            node_object = self.get(node_id)
            if node_object.type == type:
                result.append(node_id)
        return result
    
    @property
    def settlements_id(self):
        """
        Return a list of all settlement nodes id
        """
        return self.filter_type(type='settlement')

    def edges_from_node(self, node_id):
        return list(self.G.edges(node_id, data=True))

    '''
    def adjusted_length(self, id):
        item = self.model.get(id)
        return item.adjusted_length
        edge = self.G.edges[index_1, index_2]
        return edge['adjusted_length']


    def find_path(self, id_1, id_2):
        """
        Find the shortest path between id_1 and id_2
        """
        path = None
        if nx.has_path(
            self.G,
            source=index_1,
            target=index_2
        ):
            path = nx.dijkstra_path(
                self.G,
                source=index_1,
                target=index_2,
                weight="adjusted_length"
            )
        return path
    
    def find_nearest_node(self, pos: list, items: list):
        """
        Find the nearst node index to the *pos*
        """
        return self.model.find_nearest_node(pos, items)

    @property
    def paths(self):
        """
        Return infrastructure graph of items
        """
        return Paths(infrastructure=self)
    '''

    def xylim(self):
        """
        Calculate limits of axis that encompasses all nodes
        """
        x_min = None
        x_max = None
        y_min = None
        y_max = None
        for node_id in self.nodes_id:
            node_object = self.get(node_id)
            pos = node_object.pos
            x = pos[0]
            y = pos[1]
            if x_min is None or \
            x < x_min:
                x_min = x
            if x_max is None or \
            x > x_max:
                x_max = x
            if y_min is None or \
            y < y_min:
                y_min = y
            if y_max is None or \
            y > y_max:
                y_max = y
        if x_min == x_max:
            if y_min == y_max:
                y_min -= 10
                y_max += 10
            delta_y = y_max - y_min
            x_min -= delta_y / 2
            x_max += delta_y / 2
        if y_min == y_max:
            if x_min == x_max:
                x_min -= 10
                x_max += 10
            delta_x = x_max - x_min
            y_min -= delta_x / 2
            y_max += delta_x / 2
        offset_ratio = 0.15
        x_range = x_max - x_min
        y_range = y_max - y_min
        x_offset = x_range * offset_ratio
        y_offset = y_range * offset_ratio
        x_min -= x_offset
        x_max += x_offset
        y_min -= y_offset
        y_max += y_offset
        return {
            'x': {
                'min': x_min,
                'max': x_max
            },
            'y': {
                'min': y_min,
                'max': y_max
            },
        }
    
    def show(self):
        graphics = Graphics(infrastructure=self)
        graphics.show()

    def serialize(self):
        result = {}
        nodes = self.nodes_id
        for id_1 in nodes:
            result[id_1] = {}
            for id_2 in nodes:
                edge_id = self.edge_id(id_1, id_2)
                if edge_id is not None:
                    result[id_1][id_2] = edge_id
        return result
    
    def deserialize(self, data):
        self.G = nx.Graph()
        for id_1 in data:
            self.add_node(id_1)
            for id_2 in data[id_1]:
                self.add_edge(id_1, id_2, data[id_1][id_2])

    def __str__(self):
        return self.G.__str__()


if __name__ == "__main__":

    #from piperabm.model.samples import model_2 as model

    #infrastructure = model.infrastructure
    #infrastructure.show()
    infrastructure = Infrastructure()
    #infrastructure.add_node(1)
    #infrastructure.add_node(2)
    infrastructure.add_edge(1, 2, 3)
    infrastructure.add_edge(4, 5, 6)
    #infrastructure.add_edge(5, 4, 6)
    #infrastructure.remove_node(4)
    #print(infrastructure.edge_ids(3))
    #print(infrastructure.nodes_id)
    #print(infrastructure.edges_id)
    #data = infrastructure.serialize()
    #infrastructure.deserialize(data)
    #data = infrastructure.serialize()
    #print(data)
    print(infrastructure.edges_from_node(1))
