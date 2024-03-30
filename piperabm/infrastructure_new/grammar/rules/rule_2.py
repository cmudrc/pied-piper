from piperabm.infrastructure_new.grammar.rules.rule import Rule, Log
from piperabm.infrastructure_new import Street, NeighborhoodAccess
from piperabm.tools.coordinate import distance as ds
from piperabm.tools.coordinate.intersect import line_line


class Rule_2(Rule):
    """
    Condition for edge to edge intersection
    """

    def __init__(self, infrastructure):
        name = "rule 0"
        super().__init__(infrastructure, name)

    def check(self, edge_id, other_edge_id):
        result = False
        edge_object = self.get(edge_id)
        other_edge_object = self.get(other_edge_id)
        intersection = line_line(
            edge_object.pos_1,
            edge_object.pos_2,
            other_edge_object.pos_1,
            other_edge_object.pos_2
        )

        # Check if the edges are not parallel
        if intersection is not None:
            distance_1 = ds.point_to_point(intersection, edge_object.pos_1)
            distance_2 = ds.point_to_point(intersection, edge_object.pos_2)
            other_distance_1 = ds.point_to_point(intersection, other_edge_object.pos_1)
            other_distance_2 = ds.point_to_point(intersection, other_edge_object.pos_2)
            length = edge_object.length
            other_length = other_edge_object.length

            # Check if the intersection is inside the segments
            if distance_1 < length and \
                distance_2 < length and \
                other_distance_1 < other_length and \
                other_distance_2 < other_length:

                # Check if the intersection is out of the both ends of both edges
                if distance_1 > self.proximity_radius and \
                    distance_2 > self.proximity_radius and \
                    other_distance_1 > self.proximity_radius and \
                    other_distance_2 > self.proximity_radius:

                    result = True
        
        return result, intersection
    
    def apply(self, edge_id, other_edge_id, intersection, report=False):
        logs = []

        # Create new elements
        edge_object = self.get(edge_id)
        other_edge_object = self.get(other_edge_id)
        new_edge_1_kwargs = {
            'pos_1': edge_object.pos_1,
            'pos_2': intersection,
            'name': edge_object.name,
            'roughness': edge_object.roughness,
            'degradation': edge_object.degradation,
        }
        new_edge_2_kwargs = {
            'pos_1': intersection,
            'pos_2': edge_object.pos_2,
            'name': edge_object.name,
            'roughness': edge_object.roughness,
            'degradation': edge_object.degradation,
        }
        new_edge_3_kwargs = {
            'pos_1': other_edge_object.pos_1,
            'pos_2': intersection,
            'name': other_edge_object.name,
            'roughness': other_edge_object.roughness,
            'degradation': other_edge_object.degradation,
        }
        new_edge_4_kwargs = {
            'pos_1': intersection,
            'pos_2': other_edge_object.pos_2,
            'name': other_edge_object.name,
            'roughness': other_edge_object.roughness,
            'degradation': other_edge_object.degradation,
        }
        if edge_object.type == "street":
            new_edge_object_1 = Street()
            new_edge_object_2 = Street()
        elif edge_object.type == "neighborhood_access":
            new_edge_object_1 = NeighborhoodAccess()
            new_edge_object_2 = NeighborhoodAccess() 
        else:
            raise ValueError
        new_edge_object_1.deserialize(new_edge_1_kwargs)
        new_edge_object_2.deserialize(new_edge_2_kwargs)
        if other_edge_object.type == "street":
            new_edge_object_3 = Street()
            new_edge_object_4 = Street()
        elif other_edge_object.type == "neighborhood_access":
            new_edge_object_3 = NeighborhoodAccess()
            new_edge_object_4 = NeighborhoodAccess()
        else:
            raise ValueError
        new_edge_object_3.deserialize(new_edge_3_kwargs)
        new_edge_object_4.deserialize(new_edge_4_kwargs)

        # Add
        new_edge_id_1 = self.add(new_edge_object_1)
        new_edge_id_2 = self.add(new_edge_object_2)
        new_edge_id_3 = self.add(new_edge_object_3)
        new_edge_id_4 = self.add(new_edge_object_4)

        if report is True:
            log = Log(self.infrastructure, new_edge_id_1, 'added')
            logs.append(log)
            log = Log(self.infrastructure, new_edge_id_2, 'added')
            logs.append(log)
            log = Log(self.infrastructure, new_edge_id_3, 'added')
            logs.append(log)
            log = Log(self.infrastructure, new_edge_id_4, 'added')
            logs.append(log)
            log = Log(self.infrastructure, edge_id, 'removed')
            logs.append(log)
            log = Log(self.infrastructure, other_edge_id, 'removed')
            logs.append(log)

        # Remove
        self.infrastructure.remove_edge(edge_id)
        self.infrastructure.delete_object(edge_id)
        self.infrastructure.remove_edge(other_edge_id)
        self.infrastructure.delete_object(other_edge_id)

        # Report
        if report is True:
            self.report(logs)
    
    def find(self, report=False):
        anything_happened = False
        edges = self.infrastructure.edges_id
        for edge_id in edges:
            for other_edge_id in edges:
                if edge_id != other_edge_id:
                    result, intersection = self.check(edge_id, other_edge_id)
                    if result is True:
                        self.apply(edge_id, other_edge_id, intersection, report)
                        # Inform an activity
                        anything_happened = True
                # Inform an activity     
                if anything_happened is True:
                    break
            # Inform an activity     
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":
    
    from piperabm.infrastructure_new import Infrastructure, Street, NeighborhoodAccess

    infrastructure = Infrastructure(proximity_radius=1)
    object_1 = Street(pos_1=[0, 0], pos_2=[10, 0])
    object_2 = NeighborhoodAccess(pos_1=[5, 5], pos_2=[5, -5])
    infrastructure.add(object_1)
    infrastructure.add(object_2)
    
    rule = Rule_2(infrastructure)
    rule.find(report=True)
