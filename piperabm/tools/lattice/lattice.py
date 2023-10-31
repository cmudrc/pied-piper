import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from copy import deepcopy

from piperabm.tools.lattice.conditions import *


class Lattice:

    def __init__(self, x, y, target=None):
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
        if target is None:
            target = self.distribution
        self.target = self.normalize(target)

    @property
    def nodes(self):
        return list(self.G.nodes())
    
    @property
    def edges(self):
        return list(self.G.edges())
    
    def remove_node(self, node):
        self.G.remove_node(node)
    
    def remove_edge(self, node_1, node_2):
        self.G.remove_edge(node_1, node_2)

    def add_edge(self, node_1, node_2):
        self.G.add_edge(node_1, node_2)

    def has_edge(self, node_1, node_2):
        return self.G.has_edge(node_1, node_2)
    
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
            
            result = np.zeros([3, 3]) # corners are 0
            result[1, 1] = 1 # center is 1

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
    
    def MSE(self):
        errors = []
        distribution = self.distribution
        names = self.condition_names
        for name in names:
            error = distribution[name] - self.target[name]
            errors.append(error)
        errors_squared = [x**2 for x in errors]
        return (sum(errors_squared) / len(errors_squared)) ** 0.5

    @property
    def condition_names(self):
        result = []
        for condition in self.conditions:
            result.append(condition.name)
        return result
    
    def optimize(self):
        threashold = 0.05
        while self.MSE() > threashold:
            new_lattice = deepcopy(self)
            edge = random.choice(new_lattice.edges)
            new_lattice.remove_edge(*edge)
            if new_lattice.MSE() < self.MSE():
                self.remove_edge(*edge)
                #print(edge, ' removed.')

    def show(self):
        pos_dictionary = {}
        nodes = self.nodes
        for node in nodes:
            pos_dictionary[node] = node
        nx.draw(
            self.G,
            pos=pos_dictionary
        )
        plt.show()


if __name__ == "__main__":
    target = {0: 0.08333333333333333, 1: 0.0, 2: 0.3333333333333333, 3: 0.25, 4: 0.3333333333333333, 5: 0.0}
    lattice = Lattice(5, 5, target)
    lattice.optimize()
    lattice.show()
