from other import *

''' node represents city or resources '''
class Node():
    def __init__(
        self,
        name = None,
        location = [0, 0],
        demand = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        neighboors = None
            ):
        self.name = str(name) # node's name
        self.location = location # a list in form of [x, y], representing the location of the node on the map
        self.demand = demand # a dictionary in form of {water, energy, food}, representing the demand/source for each resource
        self.neighboors_list = list() # a list of neighbouring nodes

    def __str__(self):
        return self.name

''' main class '''
class Model():
    def __init__(self, nodes=list()):
        if self.validate_neighbours:
            self.nodes = nodes # a list containing all nodes of the graph
        else:
            ### an error must be raised
            print("no such neighbour")

    def validate_neighbours(self, nodes):
        ''' checks for the validity of neighbouring nodes list '''
        ### to be added
        return True

    def save(self, model_name):
        ### to be added
        pass

    def recall(self, model_name):
        ### to be added
        pass


if __name__ == "__main__":
    n_1 = Node(
        name = 'city_1',
        location = [0.1, 0.2],
        demand = {
            'water' : 1,
            'energy' : 2,
            'food' : 2.5,
        }
        )
    print(n_1)
