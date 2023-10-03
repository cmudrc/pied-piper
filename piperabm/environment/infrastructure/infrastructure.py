import networkx as nx

from piperabm.object import PureObject
from piperabm.environment.infrastructure.grammar import Grammar
from piperabm.environment.infrastructure.graphics import Graphics


class Infrastructure(PureObject, Grammar, Graphics):

    def __init__(self, environment):
        super().__init__()
        self.G = nx.Graph()
        self.environment = environment

    @property
    def proximity_radius(self):
        """
        Retrieve *proximity_radius* from linked environment
        """
        return self.environment.proximity_radius

    def add_node(self, item_index):
        """
        Add a new node
        """
        self.G.add_node(
            item_index
        )

    def add_edge(self, index_1, index_2, item_index):
        """
        Add a new edge
        """
        self.G.add_edge(
            index_1,
            index_2,
            index=item_index
        )

    def get_node_item(self, index):
        """
        Get node object
        """
        return self.environment.item(index)
    
    def get_edge_item(self, index_1, index_2):
        """
        Get edge object
        """
        edge = self.G.edges[index_1, index_2]
        index = edge['index']
        return self.environment.item(index)
    
    def all_nodes(self):
        """
        Return all nodes
        """
        return list(self.G.nodes())
    
    def all_edges(self):
        """
        Return all edges
        """
        return list(self.G.edges())
    
    def remove_node(self, index):
        """
        Remove a node
        """
        self.G.remove_node(index)

    def remove_edge(self, index_1, index_2):
        """
        Remove an edge
        """
        self.G.remove_edge(index_1, index_2)

    def all_edges_linked_to_node(self, index):
        """
        Return all edges linkes to s specific node
        """
        return list(self.G.edges(index))

    def replace_node(self, old_index, new_index):
        """
        Replace a node with other node and relocate all linked edges
        """
        linked_edges = self.all_edges_linked_to_node(old_index)
        for edge in linked_edges:
            index_1_old = edge[0]
            index_2_old = edge[1]
            index_1_new = None
            index_2_new = None
            item = self.get_edge_item(index_1_old, index_2_old)
            item_index = item.index
            if index_1_old == old_index:
                index_1_new = new_index
                index_2_new = index_2_old
            elif index_2_old == old_index:
                index_1_new = index_1_old
                index_2_new = new_index
            self.add_edge(index_1_new, index_2_new, item_index)
            self.remove_edge(index_1_old, index_2_old)
        self.remove_node(old_index)
    

if __name__ == "__main__":

    from piperabm.environment.samples import environment_1 as env
    from piperabm.time import Date


    date_start = Date(2020, 1, 1)
    date_end = Date(2020, 1, 2)
    infrastructure = env.to_infrastrucure_graph(date_start, date_end)
    infrastructure.apply_grammars()
    infrastructure.show()