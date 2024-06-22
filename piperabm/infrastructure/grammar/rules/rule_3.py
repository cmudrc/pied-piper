import numpy as np

from piperabm.tools.coordinate import distance as ds
from piperabm.tools.vector import vector as vc
from piperabm.infrastructure.grammar.rules.rule_1 import Rule1


class Rule3:
    """
    Condition for connecting isolated non-junction items to the rest
    """

    name = "rule 3"

    def __init__(self, infrastructure, proximity_radius: float = 1, search_radius: float = None):
        self.infrastructure = infrastructure
        self.search_radius = search_radius
        self.proximity_radius = proximity_radius

    def check(self, node_id):
        result = False
        # Has to be isolated
        if self.infrastructure.is_isolate(node_id) and \
            len(self.infrastructure.edges) > 0:
            result = True
        return result
    
    def apply(self, node_id, report: bool = False):
        node_pos = self.infrastructure.get_pos(node_id)
        edges_ids = self.infrastructure.edges
        distances_info = []
        # Filter edges
        if self.search_radius is None:
            edges_ids_nearby = edges_ids
        else:
            edges_ids_nearby = self.infrastructure.edges_closer_than(
                pos=node_pos,
                max_distance=self.search_radius,
                edges_ids=edges_ids,
            )
        # Find the best location to target in the filtered edges
        for edge_ids in edges_ids_nearby:
            # Only perpendicular distance from edge
            distance_vector_edge = ds.point_to_line(
                point=node_pos,
                line=[
                    self.infrastructure.get_pos(edge_ids[0]),
                    self.infrastructure.get_pos(edge_ids[1])
                ],
                segment=True,
                vector=True,
                perpendicular_only=True,
            )
            edge_info = None
            if distance_vector_edge is not None:
                edge_info = {
                    'id': edge_ids,
                    'vector': distance_vector_edge,
                    'distance': vc.magnitude(distance_vector_edge),
                    'type': 'edge',
                }
            id_1 = edge_ids[0]
            distance_vector_node_1 = ds.point_to_point(
                point_1=node_pos,
                point_2=self.infrastructure.get_pos(id_1),
                vector=True
            )
            node_info_1 = {
                'id': id_1,
                'vector': distance_vector_node_1,
                'distance': vc.magnitude(distance_vector_node_1),
                'type': 'node',
            }
            id_2 = edge_ids[1]
            distance_vector_node_2 = ds.point_to_point(
                point_1=node_pos,
                point_2=self.infrastructure.get_pos(id_2),
                vector=True
            )
            node_info_2 = {
                'id': id_2,
                'vector': distance_vector_node_2,
                'distance': vc.magnitude(distance_vector_node_2),
                'type': 'node',
            }
            if node_info_1['distance'] < node_info_2['distance']:
                possible_top_node_info = node_info_1
            else:
                possible_top_node_info = node_info_2
            if edge_info is None:
                possible_target_info = possible_top_node_info
            elif edge_info['distance'] < possible_top_node_info['distance']:
                possible_target_info = edge_info
            else:
                possible_target_info = possible_top_node_info
            distances_info.append(possible_target_info)

        # Top target info
        target_info = None
        for possible_target_info in distances_info:
            if target_info is None or \
                possible_target_info['distance'] < target_info['distance']:
                target_info = possible_target_info

        # Node as target
        if target_info['type'] == 'node':
            self.infrastructure.add_neighborhood_access(
                node_id,
                target_info['id'],
                report=report
            )
        # Edge as target
        elif target_info['type'] == 'edge':
            pos_1 = self.infrastructure.get_pos(node_id)
            pos_2 = list(np.array(pos_1) + np.array(target_info['vector']))
            new_node_id = self.infrastructure.add_junction(pos=pos_2, report=report)
            self.infrastructure.add_neighborhood_access(
                node_id,
                new_node_id,
                report=report
            )
            rule_1 = Rule1(self.infrastructure, proximity_radius=self.proximity_radius)
            rule_1.apply(node_id=new_node_id, edge_ids=target_info['id'], report=report)
        self.infrastructure.baked_streets = True
    
    def find(self, report=False):
        anything_happened = False
        nodes = self.infrastructure.nonjunctions
        for node_id in nodes:
            if self.check(node_id) is True:
                if report is True:
                    print(f"# {self.name}:")
                self.apply(node_id, report)
                # Inform an activity
                anything_happened = True
            # Inform an activity
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
    infrastructure.add_home(pos=[5, 4], id=1)

    rule = Rule3(infrastructure, proximity_radius=1, search_radius=None)
    rule.find(report=True)
    print(infrastructure)