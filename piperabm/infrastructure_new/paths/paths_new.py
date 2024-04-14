import networkx as nx

from piperabm.tools.coordinate import distance as ds


class Paths:

    def __init__(self, infrastructure):
        self.G = nx.Graph()  # Heuristic
        self.infrastructure = infrastructure
        self.current = None
        self.create()

    def add_node(self, id):
        object = self.infrastructure.get(id)
        node_type = object.type
        self.G.add_node(
            id,
            type=node_type
        )

    def add_edge(self, id_1, id_2):
        object_1 = self.infrastructure.get(id_1)
        pos_1 = object_1.pos
        object_2 = self.infrastructure.get(id_2)
        pos_2 = object_2.pos
        distance = ds.point_to_point(
            point_1=pos_1,
            point_2=pos_2
        )
        self.G.add_edge(
            id_1,
            id_2,
            distance=distance
        )

    @property
    def nodes(self):
        return list(self.G.nodes())
    
    def node_type(self, id):
        node = self.G.nodes[id]
        return node['type']

    def estimated_distance(self, id_start, id_end):
        edge = self.G.edges[id_start, id_end]
        result = edge['distance']
        return result

    def create(self):
        """
        Create graph *self.G* from *self.infrastructure*
        """
        nodes = self.infrastructure.nonjunctions
        for id_1 in nodes:
            # Nodes
            self.add_node(id=id_1)
            for id_2 in nodes:
                if id_1 != id_2:
                    # Edges
                    self.add_edge(id_1, id_2)

    def update(self):
        self.current = self.infrastructure.current()

    def path(self, id_start, id_end):
        result = None
        if nx.has_path(
            self.current,
            source=id_start,
            target=id_end
        ):
            result = nx.dijkstra_path(
                self.current,
                source=id_start,
                target=id_end,
                weight="adjusted_length"
            )
        return result
    
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

    from piperabm.infrastructure_new.samples import infrastructure_2 as infrastructure

    paths = Paths(infrastructure)
    paths.update()
    print(paths.path(id_start=1, id_end=2))
