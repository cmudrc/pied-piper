import networkx as nx


class Paths:

    def __init__(self, infrastructure):
        self.G = nx.DiGraph()
        self.infrastructure = infrastructure
        self.model = self.infrastructure.model
        self.create()

    def get(self, id: int):
        """
        Get an item object based on its index from environment library
        """
        return self.model.get(id)

    def add_edge(self, path):
        """
        Add edge to *self.G*
        """
        self.G.add_edge(
            path[0],
            path[-1],
            path=path,
            #adjusted_length=self.path_to_total_adjusted_length(path)
        )

    def create(self):
        """
        Create graph *G* from *self.infrastructure*
        """
        nodes = self.model.settlement_nodes
        for id_start in nodes:
            for id_end in nodes:
                if id_start != id_end:
                    path = self.infrastructure.find_path(id_start, id_end)
                    self.add_edge(path)
    '''
    def path_to_pos(self, path):
        """
        Covert *path* to list of positions
        """
        positions = []
        for node_index in path:
            node_item = self.get(node_index)
            pos = node_item.pos
            positions.append(pos)
        return positions
    '''
    '''
    def path_to_total_adjusted_length(self, path):
        """
        Convert *path* to total adjusted length
        """
        adjusted_lengths = []
        for i in range(len(path)-1):
            index_start = path[i]
            index_end = path[i+1]
            edge = self.infrastructure.G[index_start][index_end]
            adjusted_length = edge['adjusted_length']
            adjusted_lengths.append(adjusted_length)
        return sum(adjusted_lengths)
    '''
    def __str__(self):
        return self.G.__str__()


if __name__ == "__main__":
    from piperabm.model.samples import model_1 as model

    model.create_infrastructure()
    infrastructure = model.infrastructure
    print(infrastructure.paths)

