from other import *

''' node represents a major producer/user of resources, such as cities '''
class Node():
    def __init__(
        self,
        name = None,
        location = [0, 0],
        source = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        demand = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        neighbors = list()
            ):
        self.name = str(name) # node's name
        self.location = location # a list in form of [x, y], representing the location of the node on the map
        self.source = source # a dictionary including the amount of source for {water, energy, food} in node
        self.demand = demand # a dictionary including the amount of demand for {water, energy, food} in node
        self.neighbors_list = neighbors # a list of neighboring nodes

    def __str__(self):
        return self.name

''' main class '''
class Model():
    def __init__(self):
        self.nodes = list() # a list containing all nodes of the graph
        self.all_nodes_names = list() # a list containing names of self.nodes elements

    def add_node(self, node):
        ''' adds single node '''
        self.nodes.append(node)
        self.all_nodes_names.append(node.name)

    def add_nodes(self, nodes=list()):
        ''' add nodes in batch '''
        for node in nodes:
            self.add_node(node)

    def validate_nodes(self):
        ''' checks for the validity of nodes connections '''
        final_result = False
        result_list = list() # if all elements are True, the final result will be True
        for node in self.nodes:
            for node_neighbor_name in node.neighbors_list:
                if node_neighbor_name in self.all_nodes_names:
                    result_list.append(True)
                else:
                    print(
                        node_neighbor_name +
                        " is not a valid neighbor for " +
                        node.name
                    )
                    result_list.append(False)
        if False in result_list:
            final_result = False
        return final_result

    def save(self, model_name):
        ### to be added
        pass

    def load(self, model_name):
        ### to be added
        pass


if __name__ == "__main__":
    n_1 = Node(
        name = 'city_1',
        location = [0.1, 0.2],
        source = {
            'water' : 0.5,
            'energy' : 2.5,
            'food' : 2.5
            },
        demand = {
            'water' : 1,
            'energy' : 2,
            'food' : 2.5
            },
        neighbors = [
            'city_2'
            ],
        )
    n_2 = Node(
        name = 'city_2',
        location = [-0.4, 0.3],
        source = {
            'water' : 0.5,
            'energy' : 2.5,
            'food' : 2.5
            },
        demand = {
            'water' : 1,
            'energy' : 2,
            'food' : 2.5,
            },
        neighbors = [
            'city_1'
            ],
        )
    
    m = Model()
    m.add_node(n_1)
    m.add_node(n_2)
    m.validate_nodes()
    #print(m.all_nodes_names)
