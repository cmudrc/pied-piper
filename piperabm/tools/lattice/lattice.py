import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from copy import deepcopy

from piperabm.tools.lattice.conditions import *
from piperabm.tools.coordinate import rotate
from piperabm.tools.symbols import SYMBOLS
from piperabm.tools.file_manager import JsonHandler as jsh


class Lattice:

    def __init__(self, x: int = 1, y: int = 1):
        self.len_x = x
        self.len_y = y
        self.G = nx.grid_2d_graph(self.len_x, self.len_y)
        self.conditions = [
            condition_0,
            condition_1,
            condition_2,
            condition_3,
            condition_4,
            condition_5,
        ]

    @property
    def nodes(self):
        """
        Return all nodes index
        """
        return list(self.G.nodes())
    
    @property
    def edges(self):
        """
        Return all nodes index
        """
        return list(self.G.edges())
    
    @property
    def missing_edges(self):
        """
        Return all missing edges from the imperfect lattice
        """
        edges = []
        current_edges = self.edges
        full_lattice = Lattice(self.len_x, self.len_y)
        all_possible_edges = full_lattice.edges
        for edge in all_possible_edges:
            if edge not in current_edges:
                edges.append(edge)
        return edges
    
    def remove_node(self, node):
        """
        Remove node by index
        """
        self.G.remove_node(node)
    
    def remove_edge(self, node_1, node_2):
        """
        Remove edge by index
        """
        self.G.remove_edge(node_1, node_2)

    def add_edge(self, node_1, node_2):
        """
        Add edge between nodes
        """
        self.G.add_edge(node_1, node_2)

    def has_edge(self, node_1, node_2):
        """
        Check whether edge exists between nodes
        """
        return self.G.has_edge(node_1, node_2)
    
    @property
    def components(self):
        """
        Calculate number of components in lattice structure
        """
        all_components = nx.number_connected_components(self.G)
        return all_components - len(self.isolated_nodes)
    
    @property
    def is_connected(self):
        """
        Check if the lattice is connected
        """
        return self.components == 1

    @property
    def isolated_nodes(self):
        """
        Return list of isolated nodes
        """
        return [node for node, degree in dict(self.G.degree()).items() if degree == 0]
    
    def neighbor_value(self, node, neighbor):
        """
        Calculate neighbor values to create shape matrix of each node
        """
        result = None
        # out of margins are 0
        if neighbor[0] < 0 or \
            neighbor[1] < 0 or \
            neighbor[0] >= self.len_x or \
            neighbor[1] >= self.len_y:
            result = 0
        else:
            result = int(self.has_edge(node, neighbor))
        return result
        
    def shape_matrix(self, node):
        """
        Create shape matrix of each node
        """

        if node[0] < self.len_x and \
            node[0] >= 0 and \
            node[1] < self.len_y and \
            node[1] >= 0: # within the range
            
            result = np.zeros([3, 3]) # corners are always 0
            result[1, 1] = 1 # center is always 1

            neighbor = (node[0]-1, node[1])
            result[0, 1] = self.neighbor_value(node, neighbor)
            
            neighbor = (node[0]+1, node[1])
            result[2, 1] = self.neighbor_value(node, neighbor)
            
            neighbor = (node[0], node[1]-1)
            result[1, 0] = self.neighbor_value(node, neighbor)
            
            neighbor = (node[0], node[1]+1)
            result[1, 2] = self.neighbor_value(node, neighbor)
            
            return result
        
        else:
            raise ValueError
        
    def find_condition(self, shape_matrix):
        """
        Find condition name of each node based on its shape matrix
        """
        result = None
        for condition in self.conditions:
            output = condition.check(shape_matrix)
            if output is True:
                result = condition.name
                break
        return result
    
    @property
    def shape(self):
        """
        Create shape matrix of all nodes
        """
        result = []
        for i in range(self.len_x):
            row = []
            for j in range(self.len_y):
                shape_matrix = self.shape_matrix((i, j))
                condition_name = self.find_condition(shape_matrix)
                row.append(condition_name)
            result.append(row)
        return result
    
    @property
    def distribution(self):
        """
        Return distribution of conditions of node shapes in lattice
        """
        result = {}
        for condition in self.conditions:
            result[condition.name] = 0
        shape = self.shape
        for i in range(self.len_x):
            for j in range(self.len_y):
                condition_name = shape[i][j]
                if condition_name in result:
                    result[condition_name] += 1
        return self.normalize(result)
    
    def normalize(self, dictionary):
        """
        Normalize dictionary values
        """
        total = 0
        for key in dictionary:
            total += dictionary[key]
        for key in dictionary:
            dictionary[key] /= total
        return dictionary
    
    @property
    def total_length(self):
        """
        Number of all existing edges
        """
        return len(self.edges)
    
    @property
    def max_length(self):
        """
        Number of possible edges in a perfect lattice with similar size
        """
        horizontal = (self.len_x - 1) * self.len_y
        vertical = self.len_x * (self.len_y - 1)
        return horizontal + vertical
    
    @property
    def length_ratio(self):
        """
        Ratio between current number of edges and maximally possible numebr of edges
        """
        return self.total_length / self.max_length
    
    def RMSE(self, target):
        errors = []
        distribution = self.distribution
        names = self.condition_names
        for name in names:
            error = distribution[name] - target[name]
            errors.append(error)
        errors_squared = [x**2 for x in errors]
        return (sum(errors_squared) / len(errors_squared)) ** 0.5

    @property
    def condition_names(self):
        """
        Return all condition names
        """
        result = []
        for condition in self.conditions:
            result.append(condition.name)
        return result
    
    def generate(self, x_size, y_size, threashold=0.1, max_steps=None):
        """
        Generate a new lattice structure with a new shape that resembles the lattice
        """
        result = None
        target_distribution = self.distribution
        target_length_ratio = self.length_ratio
        if self.is_connected is False: # only generate when dealing with connected graph
            return result
        if max_steps is None:
            max_steps = SYMBOLS['inf']

        lattice = Lattice(x_size, y_size)
        counter = 0
        while lattice.RMSE(target_distribution) > threashold and \
            counter < max_steps:
            if lattice.length_ratio > target_length_ratio: # remove edge
                edges = lattice.edges
                edge = random.choice(edges)
                test_lattice = deepcopy(lattice)
                test_lattice.remove_edge(*edge)
                if test_lattice.RMSE(target_distribution) < lattice.RMSE(target_distribution) and \
                    test_lattice.is_connected:
                    lattice.remove_edge(*edge)
                    #print(edge, ' removed.')
            else: # add edge
                edges = lattice.missing_edges
                edge = random.choice(edges)
                test_lattice = deepcopy(lattice)
                test_lattice.add_edge(*edge)
                if test_lattice.RMSE(target_distribution) < lattice.RMSE(target_distribution) and \
                    test_lattice.is_connected:
                    lattice.add_edge(*edge)
                    #print(edge, ' added.')
            counter += 1
        #print('steps: ', counter)
        return lattice
    
    def to_pos(
        self,
        x_size: float = 1,
        y_size: float = 1,
        angle: float = 0,
        unit: str = 'degree',
        vector_zero: list = [0, 0]
    ):
        """
        Convert lattice edge to pos data
        """
        result = []
        edges = self.edges
        for edge in edges:
            pos_1 = np.array([edge[0][0] * x_size, edge[0][1] * y_size])
            pos_2 = np.array([edge[1][0] * x_size, edge[1][1] * y_size])
            pos_1 = pos_1 + np.array(vector_zero)
            pos_2 = pos_2 + np.array(vector_zero)
            pos_1 = rotate.z(pos_1, angle, unit, rotate='vector', ndarray=False)
            pos_1 = pos_1[:2]
            pos_2 = rotate.z(pos_2, angle, unit, rotate='vector', ndarray=False)
            pos_2 = pos_2[:2]
            result.append([pos_1, pos_2])
        return result
    
    def save(self, path, filename: str = 'sample'):
        """
        Save lattice to file
        """
        data = self.serialize()
        jsh.save(data, path, filename)
    
    def load(self, path, filename: str = 'sample'):
        """
        Load lattice from file
        """
        data = jsh.load(path, filename)
        self.deserialize(data)

    def serialize(self):
        dictionary = {}
        dictionary['len_x'] = self.len_x
        dictionary['len_y'] = self.len_y
        dictionary['G'] = nx.node_link_data(self.G)
        return dictionary
    
    def deserialize(self, dictionary):
        self.len_x = dictionary['len_x']
        self.len_y = dictionary['len_y']
        self.G = nx.node_link_graph(dictionary['G'])

    def show(self):
        pos_dictionary = {}
        nodes = self.nodes
        for node in nodes:
            pos_dictionary[node] = node
        nx.draw(
            self.G,
            pos=pos_dictionary,
            node_size=5
        )
        plt.gca().set_aspect('equal')
        plt.show()


if __name__ == '__main__':
    lattice = Lattice(2, 3)
    lattice.show()
