from piperabm.infrastructure_new.grammar.rules.rule import Rule, Log
from piperabm.infrastructure_new.grammar.rules.rule_1 import Rule_1
from piperabm.infrastructure_new import Junction, Street, NeighborhoodAccess
from piperabm.tools.coordinate import distance as ds
from piperabm.tools.coordinate.intersect import line_line


class Rule_2(Rule):
    """
    Condition for edge to edge intersection
    """

    def __init__(self, infrastructure):
        name = "rule 2"
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
        object = Junction(pos=intersection)
        new_node_id = self.add(object)

        # Report
        if report is True:
            log = Log(self.infrastructure, new_node_id, 'added')
            logs.append(log)
            self.report(logs)

        rule_1 = Rule_1(self.infrastructure)
        rule_1.apply(node_id=new_node_id, edge_id=edge_id, report=report)
        rule_1.apply(node_id=new_node_id, edge_id=other_edge_id, report=report)
    
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
