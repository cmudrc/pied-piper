import networkx as nx
import numpy as np

from piperabm.tools.coordinate import distance as ds
from piperabm.infrastructure.query.add import Add
from piperabm.infrastructure.query.get import Get
from piperabm.infrastructure.query.set import Set


class Query(Add, Get, Set):
    """
    Query network elements
    """

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
    
    '''
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
    '''
        
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
                    self.get_pos(new_edge_ids[0]),
                    self.get_pos(new_edge_ids[1])
                )
            adjustment_factor = self.calculate_adjustment_factor(
                usage_impact=data['usage_impact'],
                climate_impact=data['climate_impact']
            )
            data['adjusted_length'] = self.calculate_adjusted_length(
                length=data['length'],
                adjustment_factor=adjustment_factor,
            )
            self.G.add_edge(
                new_edge_ids[0],
                new_edge_ids[1],
                **data
            )
            if report is True:
                print(f">>> {type} edge at positions {self.get_pos(new_edge_ids[0])} - {self.get_pos(new_edge_ids[1])} added.")
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
            if self.get_node_type(id=id_1) == 'junction' and \
                self.is_isolate(id=id_1):
                self.remove_node(id=id_1)
            if self.get_node_type(id=id_2) == 'junction' and \
                self.is_isolate(id=id_2):
                self.remove_node(id=id_2)

    def random_edges(self, percent: float = 0):
        """
        Filter random edges by their length percentage
        """
        if percent > 100:
            raise ValueError("enter a value between 0 and 100")
        edges_ids = self.streets
        total_length = 0
        edges_info = []
        for edge_ids in edges_ids:
            length = self.get_edge_attribute(ids=edge_ids, attribute='length')
            total_length += length
            edge_info = {
                'ids': edge_ids,
                'length': length
            }
            edges_info.append(edge_info)
        remaining_length = (percent / 100) * total_length
        result = []
        np.random.shuffle(edges_info)
        for edge_info in edges_info:
            remaining_length -= edge_info['length']
            if remaining_length < 0:
                break
            else:
                result.append(edge_info['ids'])
        return result
    
    def remove_edge(self, ids: list = None, report: bool = False):
        """
        Remove edge
        """
        if report is True:
            print(f">>> {self.get_edge_type(ids=ids)} edge at {self.get_pos(ids[0])} - {self.get_pos(ids[1])} removed.")
        self.G.remove_edge(*ids)

    def remove_node(self, id: int, report: bool = False):
        """
        Remove node
        """
        if report is True:
            print(f">>> {self.get_node_type(id=id)} node at position {self.get_pos(id)} removed.")
        self.G.remove_node(id)
    
    def nodes_closer_than(self, id: int, search_radius: float = 0, nodes: list = None, include_self: bool = False):
        """
        Filter *nodes* that are within the *distance* from *id*
        """
        if nodes is None:
            nodes = self.nodes
        result = []
        for node_id in nodes:
            if search_radius >= self.heuristic_paths.estimated_distance(id_start=id, id_end=node_id):
                if include_self is False:
                    if node_id != id:
                        result.append(node_id)
                else:
                    result.append(node_id)
        return result
    
    @property
    def junctions(self) -> list:
        """
        Return all junction nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'junction']
        except:
            return []
        
    @property
    def nonjunctions(self) -> list:
        """
        Return all nonjunction nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') != 'junction']
        except:
            return []
        
    @property
    def homes(self) -> list:
        """
        Return all homes nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'home']
        except:
            return []

    @property
    def markets(self) -> list:
        """
        Return all market nodes
        """
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'market']
        except:
            return []
    
    @property
    def streets(self) -> list:
        """
        Return all street edges
        """
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'street']
        except:
            return []
    
    @property
    def neighborhood_accesses(self) -> list:
        """
        Return all neighborhood access edges
        """
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'neighborhood_access']
        except:
            return []