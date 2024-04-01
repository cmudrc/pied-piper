import networkx as nx


class Paths:

    def __init__(self, infrastructure):
        self.G = nx.DiGraph()
        self.create(infrastructure)

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

    def calculate_adjusted_length(self, current_infrastructure, path):
        """
        Total adjusted_length of path
        """
        total = 0
        for i in range(1, len(path)):
            segment = [path[i-1], path[i]]
            edge = current_infrastructure.edges[*segment]
            total += edge['adjusted_length']
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

    def create(self, infrastructure):
        """
        Create graph *self.G* from *self.infrastructure*
        """
        current_infrastructure = infrastructure.current()
        nodes = infrastructure.nonjunctions
        for id_start in nodes:
            for id_end in nodes:
                if id_start != id_end:
                    path = self.find_path(current_infrastructure, id_start, id_end)
                    self.G.add_edge(
                        path[0], # From
                        path[-1], # To
                        path=path,
                        adjusted_length=self.calculate_adjusted_length(current_infrastructure, path),
                    )

    def find_path(self, current_infrastructure, id_start, id_end):
        """
        Find the shortest path for current_infrastructure between id_start and id_end
        """
        path = None
        if nx.has_path(
            current_infrastructure,
            source=id_start,
            target=id_end
        ):
            path = nx.dijkstra_path(
                current_infrastructure,
                source=id_start,
                target=id_end,
                weight="adjusted_length"
            )
        return path

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

    from piperabm.infrastructure_new.samples import infrastructure_1 as infrastructure

    paths = Paths(infrastructure)
    print(paths.path(id_start=1, id_end=2))
