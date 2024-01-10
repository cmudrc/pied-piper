import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import json
from copy import deepcopy
import os

from piperabm.tools.lattice.conditions import *
from piperabm.tools.coordinate import rotate_point, move_point
from piperabm.tools.symbols import SYMBOLS


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
        return list(self.G.nodes())
    
    @property
    def edges(self):
        return list(self.G.edges())
    
    @property
    def not_edges(self):
        edges = []
        current_edges = self.edges
        full_lattice = Lattice(self.len_x, self.len_y)
        all_possible_edges = full_lattice.edges
        for edge in all_possible_edges:
            if edge not in current_edges:
                edges.append(edge)
        return edges
    
    def remove_node(self, node):
        self.G.remove_node(node)
    
    def remove_edge(self, node_1, node_2):
        self.G.remove_edge(node_1, node_2)

    def add_edge(self, node_1, node_2):
        self.G.add_edge(node_1, node_2)

    def has_edge(self, node_1, node_2):
        return self.G.has_edge(node_1, node_2)
    
    @property
    def components(self):
        all_components = nx.number_connected_components(self.G)
        return all_components - len(self.isolated_nodes)
    
    @property
    def is_connected(self):
        return self.components == 1

    @property
    def isolated_nodes(self):
        return [node for node, degree in dict(self.G.degree()).items() if degree == 0]
    
    def neighbor_value(self, node, neighbor):
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
        result = None
        for condition in self.conditions:
            output = condition.check(shape_matrix)
            if output is True:
                result = condition.name
                break
        return result
    
    @property
    def shape(self):
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
        total = 0
        for key in dictionary:
            total += dictionary[key]
        for key in dictionary:
            dictionary[key] /= total
        return dictionary
    
    @property
    def total_length(self):
        return len(self.edges)
    
    @property
    def max_length(self):
        horizontal = (self.len_x - 1) * self.len_y
        vertical = self.len_x * (self.len_y - 1)
        return horizontal + vertical
    
    @property
    def length_ratio(self):
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
        result = []
        for condition in self.conditions:
            result.append(condition.name)
        return result
    
    def generate(self, x_size, y_size, threashold=0.1, max_steps=None):
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
                    #print(edge, " removed.")
            else: # add edge
                edges = lattice.not_edges
                edge = random.choice(edges)
                test_lattice = deepcopy(lattice)
                test_lattice.add_edge(*edge)
                if test_lattice.RMSE(target_distribution) < lattice.RMSE(target_distribution) and \
                    test_lattice.is_connected:
                    lattice.add_edge(*edge)
                    #print(edge, " added.")
            counter += 1
        #print("steps: ", counter)
        return lattice
    
    def to_pos(
        self,
        x_size: float = 1,
        y_size: float = 1,
        rotation: float = 0,
        vector_zero: list = [0, 0]
    ):
        result = []
        edges = self.edges
        for edge in edges:
            pos_1 = np.array([edge[0][0] * x_size, edge[0][1] * y_size])
            pos_2 = np.array([edge[1][0] * x_size, edge[1][1] * y_size])
            pos_1 = move_point(pos_1, vector_zero)
            pos_2 = move_point(pos_2, vector_zero)
            pos_1 = list(pos_1)
            pos_2 = list(pos_2)
            pos_1 = rotate_point(pos_1, rotation)
            pos_2 = rotate_point(pos_2, rotation)
            result.append([pos_1, pos_2])
        return result
    
    def save(self, path, filename: str = "sample"):
        data = self.serialize()
        format = "." + "json"
        filename += format
        filepath = os.path.join(path, filename)
        with open(filepath, "w") as f:
            json.dump(data, f)
    
    def load(self, path, filename: str = "sample"):
        format = "." + "json"
        filename += format
        filepath = os.path.join(path, filename)
        with open(filepath, "r") as f:
            data = json.load(f)
        self.deserialize(data)

    def serialize(self):
        dictionary = {}
        dictionary["len_x"] = self.len_x
        dictionary["len_y"] = self.len_y
        dictionary["G"] = nx.node_link_data(self.G)
        return dictionary
    
    def deserialize(self, dictionary):
        self.len_x = dictionary["len_x"]
        self.len_y = dictionary["len_y"]
        self.G = nx.node_link_graph(dictionary["G"])

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
        plt.gca().set_aspect("equal")
        plt.show()


if __name__ == "__main__":
    target = {0: 0.08333333333333333, 1: 0.0, 2: 0.3333333333333333, 3: 0.25, 4: 0.3333333333333333, 5: 0.0}
    lattice = Lattice(2, 3)
    lattice.to_pos()
    #lattice.show()

