from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.infrastructure import Road
from piperabm.tools.coordinate.distance import point_to_point, point_to_line_segment


class Rule_1(Rule):
    """
    Condition for node to edge proximity
    """

    def __init__(self, model):
        name = "rule 1"
        super().__init__(model, name)

    def check(self, node_item, edge_item):
        distance = point_to_line_segment(node_item.pos, edge_item.pos_1, edge_item.pos_2)
        distance_1 = point_to_point(node_item.pos, edge_item.pos_1)
        distance_2 = point_to_point(node_item.pos, edge_item.pos_2)
        return distance is not None and \
            distance < self.proximity_radius and \
            distance_1 > self.proximity_radius and \
            distance_2 > self.proximity_radius
    
    def apply(self, report=False):
        anything_happened = False
        for node_index in self.nodes:
            for edge_index in self.edges:
                node_item = self.get(node_index)
                edge_item = self.get(edge_index)
                if self.check(node_item, edge_item):
                    # Update the items based on their types

                    if report is True:
                        print(">>> remove: " + str(edge_item))

                    if edge_item.type == "road":
                        new_edge_item_1 = Road(pos_1=edge_item.pos_1, pos_2=node_item.pos)
                        new_edge_item_2 = Road(pos_1=node_item.pos, pos_2=edge_item.pos_2)
                    self.add(new_edge_item_1)
                    self.add(new_edge_item_2)

                    self.remove(edge_index)

                    if report is True:
                        print(">>> add: " + str(new_edge_item_1))
                        print(">>> add: " + str(new_edge_item_2))

                    anything_happened = True

            if anything_happened is True:
                break

        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Junction

    model = Model(proximity_radius=1)
    item = Road(pos_1=[0, 0], pos_2=[10, 0])
    model.add(item)
    item = Junction(pos=[5, 0.5])
    model.add(item)

    rule = Rule_1(model)
    rule.apply(report=True)