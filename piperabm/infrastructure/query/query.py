import networkx as nx

from piperabm.tools.coordinate import distance as ds
from piperabm.infrastructure.query.add import Add
from piperabm.infrastructure.query.get import Get
from piperabm.infrastructure.query.set import Set


class Query(Add, Get, Set):
    """
    Query network elements
    """

    def __init__(self):
        super().__init__()

    def has_node(self, id: int) -> bool:
        """
        Check whether the network already contains the node
        """
        return self.G.has_node(id)

    def has_edge(self, ids: list) -> bool:
        """
        Check whether the network already contains the edge
        """
        return self.G.has_edge(*ids)

    def is_isolate(self, id: int) -> bool:
        """
        Check if the node is isolated
        """
        return nx.is_isolate(self.G, id)
    
    def filter_nodes_closer_than(self, id: int, distance: float, nodes: list = None) -> list:
        """
        Filter *nodes* that are within the *distance* from *id*
        """
        result = []
        if nodes is None:
            nodes = self.nodes
        for node_id in nodes:
            if distance >= self.heuristic_paths.estimated_distance(id_start=id, id_end=node_id):
                result.append(node_id)
        return result
    
    def replace_node(self, id: int, new_id: int, report: int = False) -> None:
        """
        Replace a node with another node
        """
        # Find all adjacent edges
        edges_ids = self.edges_from(id)
        # Apply change to adjacent edges
        for edge_ids in edges_ids:
            # Create new edge
            if edge_ids[0] == id:
                new_edge_ids = [new_id, edge_ids[1]]
            else:
                new_edge_ids = [edge_ids[0], new_id]
            data = self.get_edge_attributes(ids=edge_ids)
            data['length'] = ds.point_to_point(
                    self.pos(new_edge_ids[0]),
                    self.pos(new_edge_ids[1])
                )
            data['adjusted_length'] = self.calculate_adjusted_length(
                length=data['length'],
                usage_impact=data['usage_impact'],
                weather_impact=data['weather_impact']
            )
            self.G.add_edge(
                new_edge_ids[0],
                new_edge_ids[1],
                **data
            )
            if report is True:
                print(f">>> {type} edge at positions {self.pos(new_edge_ids[0])} - {self.pos(new_edge_ids[1])} added.")
            # Remove old edge
            self.remove_edge(ids=edge_ids, report=report)
        # Remove old node
        self.remove_node(id, report=report)

    def impact(self, edges: list = []):
        """
        Impact the network by removing a list of edges
        """
        if self.baked is False:
            print("First bake the model")
            raise ValueError
        for ids in edges:
            self.remove_edge(ids=ids)
            id_1 = ids[0]
            id_2 = ids[1]
            if self.node_type(id=id_1) == 'junction' and \
                self.is_isolate(id=id_1):
                self.remove_node(id=id_1)
            if self.node_type(id=id_2) == 'junction' and \
                self.is_isolate(id=id_2):
                self.remove_node(id=id_2)
    
    def remove_edge(self, ids: list = None, report: bool = False):
        """
        Remove edge
        """
        if report is True:
            print(f">>> {self.edge_type(ids=ids)} edge at {self.pos(ids[0])} - {self.pos(ids[1])} removed.")
        self.G.remove_edge(*ids)

    def remove_node(self, id: int, report: bool = False):
        """
        Remove node
        """
        if report is True:
            print(f">>> {self.node_type(id=id)} node at position {self.pos(id)} removed.")
        self.G.remove_node(id)