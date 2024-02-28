from piperabm.infrastructure.grammar.rules.rule import Rule, Log
from piperabm.infrastructure import Road
from piperabm.tools.coordinate import distance as ds
from piperabm.tools.coordinate.intersect import line_line


class Rule_2(Rule):
    """
    Condition for edge to edge intersection
    """

    def __init__(self, model):
        name = "rule 2"
        super().__init__(model, name)

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
        anything_happened = False
        for edge_id in self.edges:
            for other_edge_id in self.edges:
                if edge_id != other_edge_id:
                    if self.check(edge_id, other_edge_id) is True:
                        # Update
                        edge_object = self.get(edge_id)
                        other_edge_object = self.get(other_edge_id)
                        if edge_object.type == other_edge_object.type:
                            intersection = intersection = line_line(
                                edge_object.pos_1,
                                edge_object.pos_2,
                                other_edge_object.pos_1,
                                other_edge_object.pos_2
                            )
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
                            # Add
                            new_edge_id_1 = self.add(new_edge_object_1)
                            new_edge_id_2 = self.add(new_edge_object_2)
                            new_edge_id_3 = self.add(new_edge_object_3)
                            new_edge_id_4 = self.add(new_edge_object_4)
                            # Log
                            if report is True:
                                logs = []
                                # new_edge_id_1
                                log = Log(self.model, new_edge_id_1, 'added')
                                logs.append(log)
                                object = self.model.get(new_edge_id_1)
                                log = Log(self.model, object.id_1, 'added')
                                logs.append(log)
                                log = Log(self.model, object.id_2, 'added')
                                logs.append(log)
                                # new_edge_id_2
                                log = Log(self.model, new_edge_id_2, 'added')
                                logs.append(log)
                                object = self.model.get(new_edge_id_2)
                                log = Log(self.model, object.id_1, 'added')
                                logs.append(log)
                                log = Log(self.model, object.id_2, 'added')
                                logs.append(log)
                                # new_edge_id_3
                                log = Log(self.model, new_edge_id_3, 'added')
                                logs.append(log)
                                object = self.model.get(new_edge_id_3)
                                log = Log(self.model, object.id_1, 'added')
                                logs.append(log)
                                log = Log(self.model, object.id_2, 'added')
                                logs.append(log)
                                # new_edge_id_4
                                log = Log(self.model, new_edge_id_4, 'added')
                                logs.append(log)
                                object = self.model.get(new_edge_id_4)
                                log = Log(self.model, object.id_1, 'added')
                                logs.append(log)
                                log = Log(self.model, object.id_2, 'added')
                                logs.append(log)
                                # edge_id
                                log = Log(self.model, edge_id, 'removed')
                                logs.append(log)
                                # other_edge_id
                                log = Log(self.model, other_edge_id, 'removed')
                                logs.append(log)
                            self.remove(edge_id)
                            self.remove(other_edge_id)
                            # Report
                            if report is True:
                                self.report(logs)
                            # Inform an activity
                            anything_happened = True
                            break
            # Inform an activity
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model

    model = Model(proximity_radius=1)
    object_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
    object_2 = Road(pos_1=[5, 5], pos_2=[5, -5])
    model.add(object_1, object_2)

    rule = Rule_2(model)
    rule.apply(report=True)
