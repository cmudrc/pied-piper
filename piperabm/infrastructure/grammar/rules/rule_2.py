from piperabm.infrastructure.grammar.rules.rule import Rule
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

    def check(self, edge_item, other_edge_item):
        result = False
        intersection = line_line(edge_item.pos_1, edge_item.pos_2, other_edge_item.pos_1, other_edge_item.pos_2)

        # Check if the edges are not parallel
        if intersection is not None:
            distance_1 = ds.point_to_point(intersection, edge_item.pos_1)
            distance_2 = ds.point_to_point(intersection, edge_item.pos_2)
            other_distance_1 = ds.point_to_point(intersection, other_edge_item.pos_1)
            other_distance_2 = ds.point_to_point(intersection, other_edge_item.pos_2)
            length = edge_item.length_linear
            other_length = other_edge_item.length_linear

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

        def create_name(old_item, new_index):
            new_name = ""
            old_name = old_item.name
            if old_name != "":
                new_name = old_name + " " + str(new_index)
            return new_name

        anything_happened = False
        for edge_index in self.edges:
            for other_edge_index in self.edges:
                if edge_index != other_edge_index:
                    edge_item = self.get(edge_index)
                    other_edge_item = self.get(other_edge_index)
                    if self.check(edge_item, other_edge_item):
                        # Update the items based on their types

                        intersection = intersection = line_line(edge_item.pos_1, edge_item.pos_2, other_edge_item.pos_1, other_edge_item.pos_2)
                        if edge_item.type == "road" and other_edge_item.type == "road":

                            if report is True:
                                print(">>> remove: " + str(edge_item))
                                print(">>> remove: " + str(other_edge_item))

                            new_edge_item_1 = Road(
                                pos_1=edge_item.pos_1,
                                pos_2=intersection,
                                name=create_name(edge_item, 1),
                                roughness=edge_item.roughness
                            )
                            new_edge_item_2 = Road(
                                pos_1=intersection,
                                pos_2=edge_item.pos_2,
                                name=create_name(edge_item, 2),
                                roughness=edge_item.roughness
                            )
                            new_edge_item_3 = Road(
                                pos_1=other_edge_item.pos_1,
                                pos_2=intersection,
                                name=create_name(other_edge_item, 1),
                                roughness=other_edge_item.roughness
                            )
                            new_edge_item_4 = Road(
                                pos_1=intersection,
                                pos_2=other_edge_item.pos_2,
                                name=create_name(other_edge_item, 2),
                                roughness=other_edge_item.roughness
                            )
                            self.add(new_edge_item_1)
                            self.add(new_edge_item_2)
                            self.add(new_edge_item_3)
                            self.add(new_edge_item_4)
                            
                            self.remove(edge_index)
                            self.remove(other_edge_index)

                            if report is True:
                                print(">>> add: " + str(new_edge_item_1))
                                print(">>> add: " + str(new_edge_item_2))
                                print(">>> add: " + str(new_edge_item_3))
                                print(">>> add: " + str(new_edge_item_4))

                            anything_happened = True
                            break

            if anything_happened is True:
                break    

        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model

    model = Model(proximity_radius=1)
    item_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
    item_2 = Road(pos_1=[5, 5], pos_2=[5, -5])
    model.add(item_1, item_2)

    rule = Rule_2(model)
    rule.apply(report=True)
