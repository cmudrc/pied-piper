import networkx as nx


class Paths:

    def __init__(self, infrastructure):
        self.G = nx.DiGraph()
        self.infrastructure = infrastructure
        self.create()

    def get(self, id: int):
        """
        Get an item object based on its index from environment library
        """
        return self.infrastructure.get(id)

    def add_edge(self, path):
        """
        Add edge to *self.G*
        """
        self.G.add_edge(
            path[0],
            path[-1],
            path=path,
            adjusted_length=self.calculate_adjusted_length(path),
        )

    def calculate_adjusted_length(self, path):
        """
        Total adjusted_length of path
        """
        total = 0
        for i in range(1, len(path)):
            segment = [path[i-1], path[i]]
            total += self.infrastructure.adjusted_length(*segment)
        return total
    
    def adjusted_length(self, id_start: int, id_end: int):
        """
        Get edge id based on its id_start and id_end (both ends)
        """
        result = None
        if self.G.has_edge(id_start, id_end):
            edge = self.G.edges[id_start, id_end]
            result = edge['adjusted_length']
        return result

    @property
    def nodes(self):
        return self.infrastructure.nonjunctions_id
    
    def node_type(self, id):
        return self.infrastructure.node_type(id)

    def create(self):
        """
        Create graph *G* from *self.infrastructure*
        """
        nodes = self.nodes
        for id_start in nodes:
            for id_end in nodes:
                if id_start != id_end:
                    path = self.infrastructure.find_path(id_start, id_end)
                    self.add_edge(path)

    def path(self, id_start, id_end):
        edge = self.G.edges[id_start, id_end]
        return edge['path']
    
    def destinations(self, id_start, type='all'):
        """
        Return id of nodes that can be id_end of an edge starting from id_start
        """
        #result = list(self.G.predecessors(id_start))
        if type == 'all':
            nodes = self.nodes
            nodes.remove(id_start)
            result = nodes
        else:
            nodes = self.destinations(id_start, type='all')
            filtered_nodes = []
            for id in nodes:
                if self.node_type(id) == type:
                    filtered_nodes.append(id)
            result = filtered_nodes
        return result

    def __str__(self):
        return self.G.__str__()


if __name__ == "__main__":
    from piperabm.model.samples import model_1 as model

    model.create_infrastructure()
    infrastructure = model.infrastructure
    paths = infrastructure.paths
    print(paths)
