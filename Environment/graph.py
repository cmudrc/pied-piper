import numpy as np


class Node():
    ''' represents nodes in the graph '''
    def __init__(self, name=None, type=None, neighbors=None):
        self.name = name
        # indicating the type of node from the ('source', 'demand', 'storage'), useful when doing the simulation.
        self.type = type
        # self.neighbors is a dict containing all neighbors of the graph in form of {'name':value} pairs
        if neighbors and isinstance(neighbors, dict):
            self.neighbors = neighbors
        else:
            self.neighbors = dict()

    def add_neighbor(self, neighbor, value=0):
        self.neighbors[str(neighbor)] = value

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
            # Error must be raised
            print(
                "input type not supported, input must be an instance of either Node or Graph")


class Graph():
    ''' represents a directed graph '''

    def __init__(self, name=None):
        self.name = name
        self.nodes = list()  # a list containing all nodes of the graph
        self.all_nodes_names = list()  # a list containing names of self.nodes elements

    def add_node(self, node):
        ''' adds a single node '''
        if node.name in self.all_nodes_names:
            # raises an error, duplicate names
            print('An error must be raised')
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
        result_list = list()  # if all elements are True, the final result will be True
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

    def from_matrix(self, matrix, name=None, node_names=None):
        ''' creates the graph object of the matrix representation '''
        def validate_matrix_input(matrix, node_names=None):
            ''' validates the matrix and info input to make a graph object '''
            def shape_check(matrix):
                ''' checking the validity of the shape of matrix '''
                result = False
                row_shape, column_shape = matrix.shape
                if row_shape == column_shape:
                    result = True
                else:
                    result = False
                return result

            def duplicate_names_check(node_names):
                ''' checking the validity of the node names '''
                result = False
                if node_names:
                    visited = set()
                    dup = [x for x in node_names if x in visited or (
                        visited.add(x) or False)]
                    if len(dup) == 0:
                        result = True
                else:
                    result = True
                return result

            final_result = False
            if shape_check(matrix) and duplicate_names_check(node_names):
                final_result = True
            else:
                final_result = False
            return final_result

        if validate_matrix_input(matrix, node_names=node_names):
            self.name = name
            nodes = list()  # reset
            all_nodes_names = list()  # reset

            def create_name(all_nodes_names):
                default_name = 'node'
                counter = 1
                created_name = None
                while True:
                    possible_name = default_name + '_' + str(counter)
                    if possible_name not in all_nodes_names:
                        created_name = possible_name
                        break
                    else:
                        counter += 1
                return created_name

            if node_names:
                for node_name in node_names:
                    if node_name:
                        new_node = Node(name=str(node_name))
                        nodes.append(new_node)
                        all_nodes_names.append(str(new_node))
                    else:
                        node_name = create_name(all_nodes_names)
                        new_node = Node(name=str(node_name))
                        nodes.append(new_node)
                        all_nodes_names.append(str(new_node))
            else:
                for _ in range(matrix.shape[0]):
                    node_name = create_name(all_nodes_names)
                    new_node = Node(name=str(node_name))
                    nodes.append(new_node)
                    all_nodes_names.append(str(new_node))

            data = list()  # temperary list for calculations
            # for figuring out the connections between nodes
            for id, x in np.ndenumerate(matrix):
                if not np.isclose(x, 0):
                    data.append([id[0], id[1], x])
            for element in data:
                node = nodes[element[0]]
                new_neighbor = all_nodes_names[element[1]]
                value = element[2]
                node.add_neighbor(new_neighbor, value)

            self.nodes = nodes
            self.all_nodes_names = all_nodes_names

    def to_matrix(self):
        ''' creates the matrix representation of the graph '''
        matrix, info = None, None
        if self.validate_node_connections():
            ''' adding node names and other usable info to the info dictionary '''
            node_names = list()
            for node in self.nodes:
                node_names.append(node.name)
            info = {
                'length': len(self.nodes),
                'name': self.name,
                'node names': node_names,
            }
            ''' the matrix representation of graph '''
            matrix = np.zeros([info["length"], info["length"]])
            for id, node in enumerate(self.nodes):
                for neighbor in list(node.neighbors.keys()):
                    neighbor_id = self.find_neighbor_id(neighbor=neighbor)
                    matrix[id, neighbor_id] = node.neighbors[neighbor]
        return matrix, info

    def find_neighbor_id(self, neighbor):
        ''' finds neighboring node name in nodes_list, find its id '''
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
            # Error must be raised
            print(
                "input type not supported, input must be an instance of either Node or Graph")
            result = None
        return result


if __name__ == "__main__":
    from samples import n_1, n_2, n_3

    g = Graph(name='test')
    g.add_nodes([n_1, n_2, n_3])

    ''' checking to_matrix function '''
    m, i = g.to_matrix()
    print(m)

    ''' checking from_matrix function '''
    g = Graph()
    g.from_matrix(m, name=i['name'])
    m, i = g.to_matrix()
    print(m)
