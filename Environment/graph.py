import numpy as np

''' represents a directed graph '''
class Graph():
    def __init__(self, name=None):
        self.name = name
        self.nodes = list() # a list containing all nodes of the graph
        self.all_nodes_names = list() # a list containing names of self.nodes elements
    
    def add_node(self, node):
        ''' adds a single node '''
        if node.name in self.all_nodes_names:
            print('An error must be raised') # raises an error, duplicate names
        else:
            self.nodes.append(node)
            self.all_nodes_names.append(node.name)

    def add_nodes(self, nodes):
        ''' add entities in batch '''
        for node in nodes:
            self.add_node(node)

    def validate_node_connections(self):
        ''' checks for the validity of nodes connections '''
        final_result = False
        result_list = list() # if all elements are True, the final result will be True
        for node in self.nodes:
            for neighbor in list(node.neighbors.keys()):
                if neighbor in self.all_nodes_names:
                    result_list.append(True)
                else:
                    print(
                        neighbor +
                        " is not a valid neighbor for " +
                        node.name
                    )
                    result_list.append(False)
        if False not in result_list:
            final_result = True
        return final_result

    def to_matrix(self):
        matrix, info = None, None
        if self.validate_node_connections():
            info = {
                'length' : len(self.nodes),
            }
            matrix = np.zeros([info["length"], info["length"]])

            for id, node in enumerate(self.nodes):
                for neighbor in list(node.neighbors.keys()):
                    neighbor_id = self.find_neighbor_id(neighbor=neighbor, nodes_list=enumerate(self.nodes))
                    matrix[id, neighbor_id] = node.neighbors[neighbor]
        return matrix, info

    def find_neighbor_id(self, neighbor, nodes_list):
        ''' finds neighboring node name in nodes_list, find it's id '''
        result = None
        for id, node in enumerate(self.nodes):
            if node.name == neighbor:
                result = id
        return result

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Graph):
            for node in other.nodes:
                if node.name not in self.all_nodes_names:
                    self.add_node(node)
            result = self

        elif isinstance(other, Node):
            self.add_node(other)
            result = self
        else:
            print("input type not supported, input must be an instance of either Node or Graph") ### Error must be raised
            result = None
        return result


''' represents nodes in the graph '''
class Node():
    def __init__(self, name=None, type=None, neighbors=dict()):
        self.name = name
        self.type = type # indicating the type of node from the ('source', 'demand', 'storage'), useful when doing the simulation.
        self.neighbors = neighbors # a dict containing all neighbors of the graph in form of {'name':value} pairs

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Graph):
            other.add_node(self)
            return other
        elif isinstance(other, Node):
            g = Graph()
            g.add_node(self)
            g.add_node(other)
            return g
        else:
            print("input type not supported, input must be an instance of either Node or Graph") ### Error must be raised


if __name__ == "__main__":
    from samples import n_1, n_2, n_3
    
    ''' method 1 '''
    #g = Graph(name='test')
    #g.add_node(n_1)
    #g.add_node(n_2)
    #g.add_node(n_3)

    ''' method 2 '''
    #g = Graph(name='test')
    #g.add_nodes([n_1, n_2, n_3])

    ''' method 3 '''
    g = n_1 + n_2
    g = n_3 + g

    m, i = g.to_matrix()
    print(m)