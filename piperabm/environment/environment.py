import networkx as nx
import uuid

from piperabm.tools.coordinate import distance_point_to_point


class Environment:

    def __init__(self):
        self.G = nx.Graph()
        self.society = None  # used for binding
        self.proximity_radius = 0.1  # distance less than this amount is equal to zero
        self.type = 'environment'

    def check_node_node_interception(self, new_node_object, all_nodes: list):
        # check interception with other nodes
        result = None
        proximity = []
        new_pos = new_node_object.pos
        for node_index in all_nodes:
            node_object = self.get_node_object(node_index)
            node_pos = node_object.pos
            distance = distance_point_to_point(new_pos, node_pos)
            if distance < self.proximity_radius:
                proximity.append(True)
            else:
                proximity.append(False)
        if True in proximity:
            result = True
        else:
            result = False
        return result

    def add(self, object):
        if object.category == 'node':
            self.add_node(object)
        elif object.category == 'edge':
            self.add_edge(object)

    def add_node(
            self,
            object
        ):
        all_nodes = self.all_nodes()
        nodes_interception = self.check_node_node_interception(object, all_nodes)
        if nodes_interception is False:
            object.index = self.new_id()
            self.G.add_node(
                object.index,
                object=object
            )

    def add_edge(
            self,
            index_1: int,
            index_2: int,
            object
        ):
        self.G.add_edge(
            index_1,
            index_2,
            object
        )

    def new_id(self) -> int:
        return uuid.uuid4().int
    
    def get_node_object(self, index: int):
        result = None
        if self.G.has_node(index):
            node = self.G.nodes[index] 
            result = node['object']
        return result
    
    def get_edge_object(self, index_1: int, index_2: int):
        result = None
        if self.G.has_edge(index_1, index_2):
            edge = self.G.edges[index_1, index_2]
            result = edge['object']
        return result
    
    def all_nodes(self):
        all = list(self.G.nodes())
        return all


if __name__ == '__main__':
    from items import Junction

    env = Environment()
    item_1 = Junction(name='sample', pos=[0, 0])
    env.add_node(item_1)
    print(env.all_nodes())
    