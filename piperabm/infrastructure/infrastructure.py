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
        # Create infrastructure
        self.G = nx.Graph()
        for id in self.model.infrastructure_nodes:
            object = self.model.get(id)
            self.add_node(id, type=object.type)
        for id in self.model.infrastructure_edges:
            object = self.get(id)
            self.add_edge(
                id_1=object.id_1,
                id_2=object.id_2,
                id=id,
                adjusted_length=object.adjusted_length
            )
        # Calculate infrastructure margins
        self.margins = self.xylim()
        # Calculate paths graph
        self.paths = self.create_paths()

    def get(self, id: int):
        """
        Get object
        """
        return self.model.get(id)

    def add_node(self, id: int, type):
        """
        Add a node based on its id
        """
        self.G.add_node(id, type=type)

    def add_edge(self, id_1: int, id_2: int, id: int, adjusted_length: float = None):
        """
        Add an edge based on its id_1 and id_2 (both ends), together with its id
        """
        self.G.add_edge(id_1, id_2, id=id, adjusted_length=adjusted_length)

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
    
    def node_type(self, id):
        """
        Return node type
        """
        return self.G.nodes[id]['type']
    
    def filter_type(self, type, nodes_id=None):
        """
        Filter a list of nodes id based on their type
        """
        result = []
        if nodes_id is None:  # All nodes
            nodes_id = self.nodes_id
        for node_id in nodes_id:
            if self.node_type(node_id) == type:
                result.append(node_id)
        return result
    
    @property
    def settlements_id(self):
        """
        Return a list of all settlement nodes id
        """
        return self.filter_type(type='settlement')
    
    @property
    def markets_id(self):
        """
        Return a list of all market nodes id
        """
        return self.filter_type(type='market')
    
    @property
    def nonjunctions_id(self):
        """
        Return a list of all non-junction nodes id
        """
        nodes_id = self.nodes_id
        settlements_id = self.filter_type(type='settlement', nodes_id=nodes_id)
        markets_id = self.filter_type(type='market', nodes_id=nodes_id)
        return settlements_id + markets_id

    def find_path(self, id_1, id_2):
        """
        Find the shortest path between id_1 and id_2
        """
        path = None
        if nx.has_path(
            self.G,
            source=id_1,
            target=id_2
        ):
            path = nx.dijkstra_path(
                self.G,
                source=id_1,
                target=id_2,
                weight="adjusted_length"
            )
        return path

    def create_paths(self):
        """
        Return infrastructure graph of items
        """
        return Paths(infrastructure=self)

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

    def __str__(self):
        return self.G.__str__()


if __name__ == "__main__":
    from piperabm.model.samples import model_1 as model

    model.create_infrastructure()
    infrastructure = model.infrastructure
    print(infrastructure)
