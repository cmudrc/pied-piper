import networkx as nx

from piperabm.tools.coordinate import distance as ds
from piperabm.tools.nx_serializer import nx_serialize, nx_deserialize


class HeuristicPaths:
    """
    A network to capture the Eucledean distance between all nodes
    """

    type = "heuristic paths"

    def __init__(self):
        self.G = nx.Graph()  # Heuristic

    def estimated_distance(self, id_start, id_end):
        """
        Return estimated distance between two nodes
        """
        edge = self.G.edges[id_start, id_end]
        result = edge['distance']
        return result

    def create(self, infrastructure):
        """
        Create graph
        """
        self.G = nx.Graph()  # Reset
        nodes = infrastructure.nodes
        for id_1 in nodes:
            for id_2 in nodes:
                if id_1 == id_2:
                    distance = 0
                else:
                    distance = ds.point_to_point(
                        point_1=infrastructure.get_pos(id_1),
                        point_2=infrastructure.get_pos(id_2)
                    )
                self.G.add_edge(id_1, id_2, distance=distance)
    
    def serialize(self):
        """
        Serialize
        """
        dictionary = {
            'G': nx_serialize(self.G),
            'type': self.type,
        }
        return dictionary
    
    def deserialize(self, dictionary):
        """
        Deserialize
        """
        self.G = nx_deserialize(dictionary['G'])

    def __str__(self):
        return self.G.__str__()


if __name__ == "__main__":

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
    infrastructure.add_home(pos=[0, 0], id=1)
    infrastructure.add_home(pos=[10, 0], id=2)
    infrastructure.bake()

    # Test elements count
    junctions = infrastructure.stat['node']['junction']
    homes = infrastructure.stat['node']['home']
    total_nodes = junctions + homes
    print("Expected nodes: ", total_nodes)
    print("Expected edges: ", (total_nodes + 1) * (total_nodes / 2))
    print("Resulting nodes and edges: ", infrastructure.heuristic_paths)

    # Test functionality
    print(infrastructure.heuristic_paths.estimated_distance(id_start=1, id_end=2))