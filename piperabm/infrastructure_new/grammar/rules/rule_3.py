import numpy as np

from piperabm.infrastructure_new.grammar.rules.rule import Rule, Log
from piperabm.infrastructure_new.grammar.rules.rule_1 import Rule_1
from piperabm.infrastructure_new import Junction, NeighborhoodAccess
from piperabm.tools.coordinate import distance as ds
from piperabm.tools.linear_algebra import vector as vc


class Rule_3(Rule):
    """
    Condition for connecting isolated non-junction items to the rest
    """

    def __init__(self, infrastructure, search_radius: float = None):
        name = "rule 3"
        self.search_radius = search_radius
        super().__init__(infrastructure, name)

    def check(self, node_id):
        result = False
        # Has to be isolated
        if self.infrastructure.is_isolate(node_id):
            result = True
        return result

    def apply(self, node_id, report: bool = False):
        logs = []
        node_object = self.get(node_id)

        # Find the smallest_distance_vector
        distances = []
        edges_id = self.infrastructure.edges_id
        if self.search_radius is None:
            edges_id_nearby = edges_id
        else:
            edges_id_nearby = self.infrastructure.edges_closer_than(
                pos=node_object.pos,
                max_distance=self.search_radius,
                edges_id=edges_id,
            )
        for edge_id in edges_id_nearby:
            edge_object = self.get(edge_id)
            # only perpendicular distance from edge
            distance_vector = ds.point_to_line(
                point=node_object.pos,
                line=[edge_object.pos_1, edge_object.pos_2],
                segment=True,
                vector=True
            )
            if distance_vector is not None:
                distances.append([edge_id, distance_vector])
            else:
                ids = self.infrastructure.edge_ids(edge_id)
                node_object_1 = self.get(ids[0])
                distance_vector_1 = ds.point_to_point(
                    point_1=node_object.pos,
                    point_2=node_object_1.pos,
                    vector=True
                )
                node_object_2 = self.get(ids[0])
                distance_vector_2 = ds.point_to_point(
                    point_1=node_object.pos,
                    point_2=node_object_2.pos,
                    vector=True
                )
                distance_1 = vc.magnitude(distance_vector_1)
                distance_2 = vc.magnitude(distance_vector_2)
                if distance_1 < distance_2:
                    distances.append([ids[0], distance_vector_1])
                else:
                    distances.append([ids[1], distance_vector_2])

        # Find the nearest edge
        smallest_distance = None
        target_id = None
        for id, distance_vector in distances:
            distance = vc.magnitude(distance_vector)
            if smallest_distance is None or \
            distance < smallest_distance:
                smallest_distance = distance
                smallest_distance_vector = distance_vector
                target_id = id
        
        # Create new objects
        target_object = self.get(target_id)
        # Node as target
        if target_object.category == 'node':
            pos_1 = node_object.pos
            pos_2 = target_object.pos
            new_object = NeighborhoodAccess(pos_1=pos_1, pos_2=pos_2)
            new_id = self.infrastructure.new_id
            self.infrastructure.library[new_id] = new_object
            self.infrastructure.G.add_edge(
                target_id,
                node_id,
                id=new_id
            )
            # Report
            if report is True:
                logs = []
                log = Log(self.infrastructure, new_id, 'added')
                logs.append(log)

        # Edge as target
        elif target_object.category == 'edge':
            pos_1 = node_object.pos
            pos_2 = list(np.array(pos_1) + np.array(smallest_distance_vector))
            junction = Junction(pos=pos_2)
            id = self.add(junction)
            self.infrastructure.baked_streets = True
            self.infrastructure.baked_neighborhood = True
            new_object = NeighborhoodAccess(pos_1=pos_1, pos_2=pos_2)
            new_id = self.infrastructure.new_id
            self.infrastructure.library[new_id] = new_object
            self.infrastructure.G.add_edge(
                id,
                node_id,
                id=new_id
            )
            
            # Rule 1
            rule_1 = Rule_1(self.infrastructure)
            rule_1.apply(node_id=id, edge_id=target_id, report=report)

            # Report
            if report is True:
                logs = []
                log = Log(self.infrastructure, new_id, 'added')
                logs.append(log)
                log = Log(self.infrastructure, id, 'added')
                logs.append(log)
        
        # Report
        if report is True:
            self.report(logs)
    
    def find(self, report=False):
        anything_happened = False
        nodes = self.infrastructure.nonjunctions
        for node_id in nodes:
            if self.check(node_id) is True:
                self.apply(node_id, report)
                # Inform an activity
                anything_happened = True
            # Inform an activity
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure, Street, Home

    infrastructure = Infrastructure(proximity_radius=1)
    object_1 = Street(pos_1=[0, 0], pos_2=[10, 0])
    object_2 = Home(pos=[5, 4])
    infrastructure.add(object_1)
    infrastructure.add(object_2)

    rule = Rule_3(infrastructure)
    rule.find(report=True)