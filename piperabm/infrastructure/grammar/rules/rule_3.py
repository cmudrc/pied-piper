from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.tools.coordinate import distance as ds


class Rule_3(Rule):
    """
    Condition for multi-edge
    """

    def __init__(self, model):
        name = "rule 3"
        super().__init__(model, name)

    def check(self, edge_id, other_edge_id):
        result = False
        edge_object = self.get(edge_id)
        other_edge_object = self.get(other_edge_id)
        
        edge_id_1 = edge_object.id_1
        edge_id_2 = edge_object.id_2
        other_edge_id_1 = other_edge_object.id_1
        other_edge_id_2 = other_edge_object.id_2

        if edge_id_1 == other_edge_id_1 and \
        edge_id_2 == other_edge_id_2:
            result = True
        elif edge_id_1 == other_edge_id_2 and \
        edge_id_2 == other_edge_id_1:
            result = True
        '''
        distance_1_1 = ds.point_to_point(
            point_1=edge_object.pos_1,
            point_2=other_edge_object.pos_1
        )
        distance_1_2 = ds.point_to_point(
            point_1=edge_object.pos_1,
            point_2=other_edge_object.pos_2
        )
        distance_2_1 = ds.point_to_point(
            point_1=edge_object.pos_2,
            point_2=other_edge_object.pos_1
        )
        distance_2_2 = ds.point_to_point(
            point_1=edge_object.pos_2,
            point_2=other_edge_object.pos_2
        )
        distances = [distance_1_1, distance_1_2, distance_2_1, distance_2_2]
        distances = sorted(distances)
        distances = distances[:2]
        if distances[0] < self.proximity_radius and \
        distances[1] < self.proximity_radius:
            result = True
        '''
        return result
    
    def apply(self, report=False):
        anything_happened = False
        for edge_id in self.edges:
            for other_edge_id in self.edges:
                if edge_id != other_edge_id:
                    if self.check(edge_id, other_edge_id) is True:
                        # Update
                        self.remove(other_edge_id)
                        # Report
                        if report is True:
                            print(">>> remove: " + str(other_edge_id))
                        # Inform an activity
                        anything_happened = True
            # Inform an activity
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Road

    model = Model(proximity_radius=1)
    item_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
    item_2 = Road(pos_1=[0, 0.5], pos_2=[9.5, 0])
    model.add(item_1, item_2)

    rule = Rule_3(model)
    rule.apply(report=True)