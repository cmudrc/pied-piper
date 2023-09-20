import networkx as nx
from copy import deepcopy

from piperabm.object import PureObject
from piperabm.environment.query import Query
from piperabm.environment.items import Junction
from piperabm.tools.coordinate import distance_point_to_point, distance_point_to_line, intersect_line_line


class Environment(PureObject, Query):

    def __init__(
            self,
            proximity_radius: float = 0.1    
        ):
        super().__init__()
        self.G = nx.Graph()
        self.society = None  # used for binding
        self.proximity_radius = proximity_radius  # distance less than this amount is equivalent to zero
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
        ''' node proximity '''
        node_node_proximity = self.check_node_node_proximity(pos=object.pos)
        if node_node_proximity is False:  # create new node
            index = self.new_id()
            object.index = index
            self.G.add_node(
                object.index,
                object=object
            )
            ''' edge proximity '''
            object = self.get_node_object(index)
            node_edge_proximity = self.check_node_edge_proximity(pos=object.pos)
            if node_edge_proximity is True:  # create new edges and delete old edge
                distance, indexes = self.find_nearest_edge(pos=object.pos)
                old_edge_object = self.get_edge_object(*indexes)
                new_edge_object_1 = deepcopy(old_edge_object)
                new_edge_object_2 = deepcopy(old_edge_object)
                new_edge_object_1.length_actual = None
                new_edge_object_2.length_actual = None
                new_edge_object_1.pos_1 = object.pos
                new_edge_object_2.pos_2 = object.pos
                self.G.remove_edge(*indexes)
                self.add(new_edge_object_1)
                self.add(new_edge_object_2)
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
    
    def check_node_edge_proximity(self, pos: list):
        result = None
        edges_distance = self.calculate_edges_distance_from_node(pos)
        edges_distance = self.filter_distances(edges_distance)
        if len(edges_distance) == 0:
            result = False
        else:
            result = True
        return result
    
    def check_node_node_proximity(self, pos: list):
        result = None
        nodes_distance = self.calculate_nodes_distance_from_node(pos)
        nodes_distance = self.filter_distances(nodes_distance)
        if len(nodes_distance) == 0:
            result = False
        else:
            result = True
        return result
    
    def check_edge_node_proximity(self, pos_1: list, pos_2: list):
        result = None
        nodes_distance = self.calculate_nodes_distance_from_edge(pos_1, pos_2)
        nodes_distance = self.filter_distances(nodes_distance)
        if len(nodes_distance) == 0:
            result = False
        else:
            result = True
        return result

    def calculate_nodes_distance_from_node(self, pos: list):
        """ Calculate nodes distance from pos """
        result = []  # list of [distance, index]
        for node_index in self.all_nodes():
            item = self.get_node_object(node_index)
            distance = distance_point_to_point(pos, item.pos)
            result.append([distance, node_index])
        return result
    
    def calculate_edges_distance_from_node(self, pos: list):
        """ Calculate edges distance from pos """
        result = []  # list of [distance, index]
        for edge_indexes in self.all_edges():
            item = self.get_edge_object(*edge_indexes)
            distance = distance_point_to_line(pos, item.pos_1, item.pos_2)
            if distance is not None:
                result.append([distance, edge_indexes])
        return result
    
    def calculate_nodes_distance_from_edge(self, pos_1: list, pos_2: list):
        """ Calculate nodes distance from edge """
        result = []  # list of [distance, index]
        for node_index in self.all_nodes():
            item = self.get_node_object(node_index)
            distance = distance_point_to_line(item.pos, pos_1, pos_2)
            result.append([distance, node_index])
        return result
    
    def calculate_edges_distance_from_edge(self, pos_1: list, pos_2: list):
        pass

    def find_nearest_node(self, pos: list):
        """ Return index and distance of the closest nodes to the input pos """
        nodes_distance = self.calculate_nodes_distance_from_node(pos)
        nodes_distance = self.sort_distances(nodes_distance)
        nearest_item = nodes_distance[0]
        distance = nearest_item[0]
        index = nearest_item[1]
        return distance, index
    
    def find_nearest_edge(self, pos: list):
        """ Return index and distance of the closest edge to the input pos """
        edges_distance = self.calculate_edges_distance_from_node(pos)
        edges_distance = self.sort_distances(edges_distance)
        nearest_item = edges_distance[0]
        distance = nearest_item[0]
        indexes = nearest_item[1]
        return distance, indexes


if __name__ == '__main__':
    from items import Junction

    env = Environment()
    item_1 = Junction(name='sample', pos=[0, 0])
    env.add_node(item_1)
    print(env.all_nodes())
    