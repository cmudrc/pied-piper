import networkx as nx
import numpy as np

from piperabm.infrastructure.paths import Paths
from piperabm.graphics import Graphics


class Infrastructure:

    def __init__(self, model):
        self.G = nx.Graph()
        self.model = model
        self.create()

    def create(self):
        """
        Create graph *G* from *self.model*
        """
        all_nodes = self.model.all_environment_nodes
        all_edges = self.model.all_environment_edges
        for item_index in all_nodes:
            self.G.add_node(item_index)
        for item_index in all_edges:
            item = self.model.get(item_index)
            index_1, _ = self.model.find_nearest_node(item.pos_1, all_nodes)
            index_2, _ = self.model.find_nearest_node(item.pos_2, all_nodes)
            self.G.add_edge(
                index_1,
                index_2,
                index=item.index,
                adjusted_length=item.adjusted_length
            )
    
    def get(self, index: int):
        return self.model.get(index)

    def find_edge_index(self, index_1, index_2):
        """
        Get edge index based on its index_1 and index_2 (both ends)
        """
        edge = self.G.edges[index_1, index_2]
        return edge['index']
    
    def adjusted_length(self, index_1, index_2):
        edge = self.G.edges[index_1, index_2]
        return edge['adjusted_length']

    def all_nodes(self, type=None):
        """
        Return all nodes
        """
        result = None
        if type is None:
            result = list(self.G.nodes())
        else:
            result = []
            for index in self.all_nodes():
                item = self.model.get(index)
                if item.type == type:
                    result.append(index)
        return result

    def all_edges(self):
        """
        Return all edges
        """
        return list(self.G.edges())

    def find_path(self, index_1, index_2):
        """
        Find the shortest path between index_1 and index_2
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
    
    def principal_vectors(self, num=None):
        """
        Calculate connecting vectors between n nearest nodes
        """
        vectors = []
        nodes = self.all_nodes()
        for node_index in nodes:
            neighbors = self.neighbor_vectors(node_index, num)
            main = self.get(node_index)
            main_pos = np.array(main.pos)
            for element in neighbors:
                neighbor_index = element[1]
                neighbor = self.get(neighbor_index)
                neighbor_pos = np.array(neighbor.pos)
                vector = neighbor_pos - main_pos
                vectors.append(vector)
        return vectors

    def neighbor_vectors(self, index, num=None):
        """
        Find and return index of n nearest nodes
        """
        nodes = self.all_nodes()
        nodes.remove(index)
        if num is None:
            num = len(nodes)
        else:
            if num > len(nodes):
                raise ValueError
        item = self.get(index)
        neighbors = self.model.find_nearest_nodes(item.pos, nodes, num)
        return neighbors

    def xylim(self):
        """
        Calculate limits of axis that encompasses all nodes
        """
        x_min = None
        x_max = None
        y_min = None
        y_max = None
        for index in self.all_nodes():
            node = self.get(index)
            pos = node.pos
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
        xlim = [x_min, x_max]
        ylim = [y_min, y_max]
        return xlim, ylim
    
    def show(self):
        graphics = Graphics(infrastructure=self)
        graphics.show()


if __name__ == "__main__":

    from piperabm.model.samples import model_2 as model

    infrastructure = model.infrastructure
    infrastructure.show()
