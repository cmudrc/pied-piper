class Node():
    def __init__(self, name=None, type=None, neighbors=None):
        self.name = name
        # indicating the type of node from the ('source', 'demand', 'storage'), useful when doing the simulation.
        self.type = type
        # self.neighbors is a dict containing all neighbors of the graph in form of {'name':value} pairs
        if neighbors and isinstance(neighbors, dict):
            self.neighbors = neighbors
        else:
            self.neighbors = list()

    def add_neighbor(self, neighbor, value=0):
        if neighbor.type is not None:
            unique_name = neighbor.name + '_' + neighbor.type
        else:
            unique_name = neighbor.name
        self.neighbors.append(
            {
                'value': value,
                'name': neighbor.name,
                'type': neighbor.type,
                'unique_name': unique_name
            }
        )

    def __str__(self):
        result = None
        if self.type is not None:
            result = self.name + '_' + self.type  # unique name for each node
        else:
            result = self.name
        return result

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
        if str(node) in self.all_nodes_names:
            # raises an error, duplicate names
            print('An error must be raised')
        else:
            self.nodes.append(node)
            self.all_nodes_names.append(str(node))

    def add_nodes(self, nodes):
        ''' add entities in batch '''
        for node in nodes:
            self.add_node(node)

    def validate_node_connections(self):
        ''' checks for the validity of nodes connections '''
        final_result = False
        result_list = list()  # if all elements are True, the final result will be True
        for node in self.nodes:
            for neighbor in node.neighbors:
                if neighbor['unique_name'] in self.all_nodes_names:
                    result_list.append(True)
                else:
                    print(
                        neighbor['unique_name'] +
                        " is not a valid neighbor for " +
                        str(node)
                    )
                    result_list.append(False)
        if False not in result_list:
            final_result = True
        return final_result


if __name__ == "__main__":
    from samples import n_1, n_2, n_3

    g = Graph(name='test')
    g.add_nodes([n_1, n_2, n_3])
    g.validate_node_connections()
