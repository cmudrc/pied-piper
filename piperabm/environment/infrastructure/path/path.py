import networkx as nx


class Path:

    def __init__(self, infrastructure):
        self.G = nx.DiGraph()
        self.infrastructure = infrastructure
        self.create()

    def get_item(self, index: int):
        """
        Get an item object based on its index from environment library
        """
        return self.infrastructure.get_item(index)

    def add_edge(self, path):
        self.G.add_edge(
            path[0],
            path[-1],
            path=path,
            adjusted_length=None
        )

    def create(self):
        """
        Create graph *G* from *self.infrastructure*
        """
        nodes = self.infrastructure.all_nodes(type="settlement")
        for index_start in nodes:
            for index_end in nodes:
                if index_start != index_end:
                    path = self.infrastructure.find_path(index_start, index_end)
                    self.add_edge(path)

    def path_to_pos(self, path):
        positions = []
        for node_index in path:
            node_item = self.get_item(node_index)
            pos = node_item.pos
            positions.append(pos)
        return positions
    
    def path_to_adjusted_length(self, path):
        adjusted_length = []
        pass
    

if __name__ == "__main__":

    from piperabm.environment.samples import environment_2 as environment

    infrastructure = environment.infrastrucure
    path_graph = Path(infrastructure)
    print(path_graph.G)