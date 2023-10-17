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
                self.add_edge(
                    index_1,
                    index_2,
                    item.index,
                    item.adjusted_length
                )

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
        Add a new edge, adjusted_length is used for path finding algorithm
        """
        self.G.add_edge(
            index_1,
            index_2,
            index=item_index,
            adjusted_length=adjusted_length
        )

    def find_edge_index(self, index_1, index_2):
        """
        Get edge index based on its index_1 and index_2 (both ends)
        """
        edge = self.G.edges[index_1, index_2]
        return edge['index']

    def all_nodes(self, type=None):
        """
        Return all nodes
        """
        result = None
        if type is None:
            result = list(self.G.nodes())
        else:
            result = []
            for index in self.all_nodes():
                item = self.get_item(index)
                if item.type == type:
                    result.append(index)
        return result

    def all_edges(self):
        """
        Return all edges
        """
        return list(self.G.edges())

    def find_path(self, index_1, index_2):
        """
        Find the shortest path between index_1 and index_2
        """

        def convert_path_to_edge_index(path):
            result = []
            for i in range(len(path)-1):
                index_1 = path[i]
                index_2 = path[i+1]
                edge_index = self.find_edge_index(index_1, index_2)
                result.append(edge_index)
            return result
        
        path = None

        if nx.has_path(
            self.G,
            source=index_1,
            target=index_2
        ):
            path = nx.dijkstra_path(
                self.G,
                source=index_1,
                target=index_2,
                weight='adjusted_length'
            )

        #return convert_path_to_edge_index(path)
        return path
    
    def find_nearest_node(self, pos: list):
        """
        Find the nearst node index to the *pos*
        """
        return self.environment.find_nearest_node(pos)


if __name__ == "__main__":

    from piperabm.environment.samples import environment_2 as environment

    infrastructure = environment.infrastrucure
    infrastructure.show()
