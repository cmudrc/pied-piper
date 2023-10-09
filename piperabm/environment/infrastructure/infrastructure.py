import networkx as nx

from piperabm.environment.infrastructure.graphics import Graphics


class Infrastructure(Graphics):

    def __init__(self, environment):
        super().__init__()
        self.G = nx.Graph()
        self.environment = environment
        self.create()

    def create(self):
        """
        Create graph *G* from *self.environment*
        """
        items = self.environment.all_items
        for item_index in items:
            item = self.get_item(item_index)
            if item.category == 'node':
                self.add_node(item.index)
            elif item.category == 'edge':
                index_1 = self.environment.find_nearest_node(item.pos_1, items)
                index_2 = self.environment.find_nearest_node(item.pos_2, items)
                self.add_edge(index_1, index_2, item.index, item.adjusted_length)

    def get_item(self, index: int):
        """
        Get an item object based on its index from environment library
        """
        return self.environment.get_item(index)

    def add_node(self, item_index):
        """
        Add a new node
        """
        self.G.add_node(
            item_index
        )

    def add_edge(self, index_1, index_2, item_index, adjusted_length):
        """
        Add a new edge, weight is used for path finding algorithm
        """

        self.G.add_edge(
            index_1,
            index_2,
            index=item_index,
            weight=adjusted_length
        )

    def find_edge_index(self, index_1, index_2):
        """
        Get edge index based on its index_1 and index_2 (both ends)
        """
        edge = self.G.edges[index_1, index_2]
        return edge['index']

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


if __name__ == "__main__":

    from piperabm.environment.samples import environment_2 as env

    infrastructure = env.to_infrastrucure_graph()
    infrastructure.show()
