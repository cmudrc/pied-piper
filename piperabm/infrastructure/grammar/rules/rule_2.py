from piperabm.tools.coordinate import distance as ds
from piperabm.tools.coordinate import intersect
from piperabm.infrastructure.grammar.rules.rule_1 import Rule1


class Rule2:
    """
    Condition for node to edge proximity
    """

    name = "rule 2"

    def __init__(self, infrastructure, proximity_radius: float = 1):
        self.infrastructure = infrastructure
        self.proximity_radius = proximity_radius

    def check(self, edge_ids, other_edge_ids):
        result = False
        edge_pos_1 = self.infrastructure.get_pos(edge_ids[0])
        edge_pos_2 = self.infrastructure.get_pos(edge_ids[1])
        other_edge_pos_1 = self.infrastructure.get_pos(other_edge_ids[0])
        other_edge_pos_2 = self.infrastructure.get_pos(other_edge_ids[1])
        intersection = intersect.line_line(
            edge_pos_1,
            edge_pos_2,
            other_edge_pos_1,
            other_edge_pos_2
        )

        # Check if the edges are not parallel
        if intersection is not None:
            distance_1 = ds.point_to_point(intersection, edge_pos_1)
            distance_2 = ds.point_to_point(intersection, edge_pos_2)
            other_distance_1 = ds.point_to_point(intersection, other_edge_pos_1)
            other_distance_2 = ds.point_to_point(intersection, other_edge_pos_2)
            length = self.infrastructure.get_edge_attribute(ids=edge_ids, attribute='length')
            other_length = self.infrastructure.get_edge_attribute(ids=other_edge_ids, attribute='length')

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
    
    def apply(self, edge_ids, other_edge_ids, intersection, report=False):
        new_node_id = self.infrastructure.add_junction(pos=intersection, report=report)
        rule_1 = Rule1(self.infrastructure, proximity_radius=self.proximity_radius)
        rule_1.apply(node_id=new_node_id, edge_ids=edge_ids, report=report)
        rule_1.apply(node_id=new_node_id, edge_ids=other_edge_ids, report=report)    
    
    def find(self, report=False):
        anything_happened = False
        edges = self.infrastructure.edges
        for edge_ids in edges:
            for other_edge_ids in edges:
                if edge_ids != other_edge_ids:
                    result, intersection = self.check(edge_ids, other_edge_ids)
                    if result is True:
                        if report is True:
                            print(f"# {self.name}:")
                        self.apply(edge_ids, other_edge_ids, intersection, report)
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

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
    infrastructure.add_street(pos_1=[5, 5], pos_2=[5, -5])
    
    rule = Rule2(infrastructure, proximity_radius=1)
    rule.find(report=True)
    print(infrastructure)