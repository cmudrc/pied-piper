from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.infrastructure import Road
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
        intersection = line_line(edge_object.pos_1, edge_object.pos_2, other_edge_object.pos_1, other_edge_object.pos_2)

        # Check if the edges are not parallel
        if intersection is not None:
            distance_1 = ds.point_to_point(intersection, edge_object.pos_1)
            distance_2 = ds.point_to_point(intersection, edge_object.pos_2)
            other_distance_1 = ds.point_to_point(intersection, other_edge_object.pos_1)
            other_distance_2 = ds.point_to_point(intersection, other_edge_object.pos_2)
            length = edge_object.length_linear
            other_length = other_edge_object.length_linear

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
        
        return result
    
    def apply(self, report=False):
        '''
        def create_name(old_item, new_index):
            new_name = ""
            old_name = old_item.name
            if old_name != "":
                new_name = old_name + " " + str(new_index)
            return new_name
        '''
        anything_happened = False
        for edge_id in self.edges:
            for other_edge_id in self.edges:
                if edge_id != other_edge_id:
                    if self.check(edge_id, other_edge_id):
                        # Update the items based on their types
                        edge_object = self.get(edge_id)
                        other_edge_object = self.get(other_edge_id)
                        intersection = intersection = line_line(
                            edge_object.pos_1,
                            edge_object.pos_2,
                            other_edge_object.pos_1,
                            other_edge_object.pos_2
                        )
                        if edge_object.type == other_edge_object.type:

                            if report is True:
                                print(">>> remove: " + str(edge_object))
                                print(">>> remove: " + str(other_edge_object))

                            new_edge_object_1 = Road(
                                pos_1=edge_object.pos_1,
                                pos_2=intersection,
                                name=edge_object.name,
                                roughness=edge_object.roughness,
                                degradation=edge_object.degradation
                            )
                            new_edge_object_2 = Road(
                                pos_1=intersection,
                                pos_2=edge_object.pos_2,
                                name=edge_object.name,
                                roughness=edge_object.roughness,
                                degradation=edge_object.degradation
                            )
                            new_edge_object_3 = Road(
                                pos_1=other_edge_object.pos_1,
                                pos_2=intersection,
                                name=other_edge_object.name,
                                roughness=other_edge_object.roughness,
                                degradation=other_edge_object.degradation
                            )
                            new_edge_object_4 = Road(
                                pos_1=intersection,
                                pos_2=other_edge_object.pos_2,
                                name=other_edge_object.name,
                                roughness=other_edge_object.roughness,
                                degradation=other_edge_object.degradation
                            )
                            self.model.add(new_edge_object_1)
                            self.model.add(new_edge_object_2)
                            self.model.add(new_edge_object_3)
                            self.model.add(new_edge_object_4)
                            
                            self.model.remove(edge_id)
                            self.model.remove(other_edge_id)
                            ids = self.infrastructure.edge_ids(edge_id)
                            self.infrastructure.remove_edge(*ids)
                            ids = self.infrastructure.edge_ids(other_edge_id)
                            self.infrastructure.remove_edge(*ids)

                            if report is True:
                                print(">>> add: " + str(new_edge_object_1))
                                print(">>> add: " + str(new_edge_object_2))
                                print(">>> add: " + str(new_edge_object_3))
                                print(">>> add: " + str(new_edge_object_4))

                            anything_happened = True
                            break

            if anything_happened is True:
                break    

        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model

    model = Model(proximity_radius=1)
    object_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
    object_2 = Road(pos_1=[5, 5], pos_2=[5, -5])
    model.add(object_1, object_2)

    rule = Rule_2(model.infrastructure)
    rule.apply(report=True)
