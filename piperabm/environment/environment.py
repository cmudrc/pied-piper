import networkx as nx
import uuid

from piperabm.object import PureObject
from piperabm.environment.items import Junction
from piperabm.tools.coordinate import distance_point_to_point, distance_point_to_line


class Environment(PureObject):

    def __init__(self):
        super().__init__()
        self.G = nx.Graph()
        self.society = None  # used for binding
        self.proximity_radius = 0.1  # distance less than this amount is equal to zero
        self.type = 'environment'

    def add(self, object):
        """ Add new item """
        result = None
        if object.category == 'node':
            result = self.add_node(object)
        elif object.category == 'edge':
            result = self.add_edge(object)
        return result

    def add_node(self, object):
        """ Add new node and return the index """
        nodes_distance = self.filter_nodes_by_distance(pos=object.pos)
        if len(nodes_distance) == 0:  # create new
            index = self.new_id()
            object.index = index
            self.G.add_node(
                object.index,
                object=object
            )
        else:  # return currently available node index
            distance, index = self.find_nearest_node(pos=object.pos)
        return index

    def add_edge(self, object):
        """ Add new edge """
        junction_1 = Junction(pos=object.pos_1)
        junction_2 = Junction(pos=object.pos_2)
        index_1 = self.add_node(junction_1)
        index_2 = self.add_node(junction_2)
        object.index_1 = index_1
        object.index_2 = index_2
        self.G.add_edge(
            index_1,
            index_2,
            object=object
        )

    def new_id(self) -> int:
        """ Generate a new unique integer """
        return uuid.uuid4().int
    
    def check_node_edge_proximity(self, pos: list):
        result = None
        return result
    
    def check_node_node_proximity(self, pos: list):
        result = None
        nodes_distance = self.filter_nodes_by_distance(pos)
        if len(nodes_distance) == 0:
            result = False
        else:
            result = True
        return result

    def calculate_nodes_distance(self, pos: list):
        """ Calculate nodes distance from pos """
        result = []  # list of [distance, index]
        for node_index in self.all_nodes():
            item = self.get_node_object(node_index)
            distance = distance_point_to_point(pos, item.pos)
            result.append([distance, node_index])
        return result
    
    def calculate_edges_distance(self, pos: list):
        """ Calculate edges distance from pos """
        result = []  # list of [distance, index]
        for edge_indexes in self.all_edges():
            item = self.get_edge_object(*edge_indexes)
            distance = distance_point_to_line(pos, item.pos_1, item.pos_2)
            if distance is not None:
                result.append([distance, edge_indexes])
        return result

    def sort_nodes_by_distance(self, pos: list):
        """ Sort all nodes based on their distance from pos """
        nodes_distance = self.calculate_nodes_distance(pos)
        return [[distance, index] for distance, index in sorted(nodes_distance)]
    
    def sort_edges_by_distance(self, pos: list):
        """ Sort all edges based on their distance from pos """
        edges_distance = self.calculate_edges_distance(pos)
        return [[distance, indexes] for distance, indexes in sorted(edges_distance)]

    def filter_nodes_by_distance(self, pos: list):
        """ Filter nodes closer than *self.proximity_radius* """
        result = []  # list of [distance, index]
        nodes_distance = self.sort_nodes_by_distance(pos)
        for element in nodes_distance:
            distance = element[0]
            node_index = element[1]
            if distance < self.proximity_radius:
                result.append([distance, node_index])
            else:
                break
        return result
    
    def filter_edges_by_distance(self, pos: list):
        """ Filter edges closer than *self.proximity_radius* """
        result = []  # list of [distance, index]
        edges_distance = self.sort_edges_by_distance(pos)
        for element in edges_distance:
            distance = element[0]
            edge_indexes = element[1]
            if distance < self.proximity_radius:
                result.append([distance, edge_indexes])
            else:
                break
        return result

    def find_nearest_node(self, pos: list):
        """ Return index and distance of the closest nodes to the input pos """
        nodes_distance = self.sort_nodes_by_distance(pos)
        nearest_item = nodes_distance[0]
        distance = nearest_item[0]
        index = nearest_item[1]
        return distance, index
    
    def find_nearest_edge(self, pos: list):
        """ Return index and distance of the closest edge to the input pos """
        edges_distance = self.sort_edges_by_distance(pos)
        nearest_item = edges_distance[0]
        distance = nearest_item[0]
        indexes = nearest_item[1]
        return distance, indexes
    
    def get_node_object(self, index: int):
        """ Return node object by its index """
        result = None
        if self.G.has_node(index):
            node = self.G.nodes[index] 
            result = node['object']
        return result
    
    def get_edge_object(self, index_1: int, index_2: int):
        """ Return edge object by its index_1 and index_2 """
        result = None
        if self.G.has_edge(index_1, index_2):
            edge = self.G.edges[index_1, index_2]
            result = edge['object']
        return result
    
    def all_nodes(self) -> list:
        """ Return a list of all nodes """
        all = list(self.G.nodes())
        return all
    
    def all_edges(self) -> list:
        """ Return a list of all edges """
        all = list(self.G.edges())
        return all


if __name__ == '__main__':
    from items import Junction

    env = Environment()
    item_1 = Junction(name='sample', pos=[0, 0])
    env.add_node(item_1)
    print(env.all_nodes())
    