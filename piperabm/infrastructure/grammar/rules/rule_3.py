from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.tools.coordinate.distance import point_to_point


class Rule_3(Rule):
    """
    Condition for multi-edge
    """

    def __init__(self, model):
        name = "rule 3"
        super().__init__(model, name)

    def check(self, edge_item, other_edge_item):
        distance_1_1 = point_to_point(edge_item.pos_1, other_edge_item.pos_1)
        distance_1_2 = point_to_point(edge_item.pos_1, other_edge_item.pos_2)
        distance_2_1 = point_to_point(edge_item.pos_2, other_edge_item.pos_1)
        distance_2_2 = point_to_point(edge_item.pos_2, other_edge_item.pos_2)
        distances = [distance_1_1, distance_1_2, distance_2_1, distance_2_2]
        distances = sorted(distances)
        distances = distances[:2]
        return distances[0] < self.proximity_radius and \
            distances[1] < self.proximity_radius
    
    def apply(self, report=False):
        anything_happened = False
        for edge_index in self.edges:
            for other_edge_index in self.edges:
                if edge_index != other_edge_index:
                    edge_item = self.get(edge_index)
                    other_edge_item = self.get(other_edge_index)

                    if self.check(edge_item, other_edge_item):
                        # Update the items based on their types

                        if report is True:
                            print(">>> remove: " + str(other_edge_item))

                        self.remove(other_edge_index)
                        
                        anything_happened = True

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