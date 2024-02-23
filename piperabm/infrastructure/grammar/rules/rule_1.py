from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.infrastructure import Road
from piperabm.tools.coordinate import distance as ds


class Rule_1(Rule):
    """
    Condition for node to edge proximity
    """

    def __init__(self, infrastructure):
        name = "rule 1"
        super().__init__(infrastructure, name)

    def check(self, node_id, edge_id):
        node_object = self.get(node_id)
        edge_object = self.get(edge_id)
        distance = ds.point_to_line(
            point=node_object.pos,
            line=[edge_object.pos_1, edge_object.pos_2],
            segment=True
        )
        distance_1 = ds.point_to_point(
            point_1=node_object.pos,
            point_2=edge_object.pos_1
        )
        distance_2 = ds.point_to_point(
            point_1=node_object.pos,
            point_2=edge_object.pos_2
        )
        return distance is not None and \
            distance < self.proximity_radius and \
            distance_1 > self.proximity_radius and \
            distance_2 > self.proximity_radius
    
    def apply(self, report=False):
        anything_happened = False
        for node_id in self.nodes:
            for edge_id in self.edges:
                if self.check(node_id, edge_id):
                    # Update the items based on their types
                    node_object = self.get(node_id)
                    edge_object = self.get(edge_id)

                    if report is True:
                        print(">>> remove: " + str(edge_object))

                    if edge_object.type == "road":
                        new_edge_object_1 = Road(pos_1=edge_object.pos_1, pos_2=node_object.pos)
                        new_edge_object_2 = Road(pos_1=node_object.pos, pos_2=edge_object.pos_2)
                    self.model.add(new_edge_object_1)
                    self.model.add(new_edge_object_2)
                    self.model.remove(edge_id)
                    ids = self.infrastructure.edge_ids(edge_id)
                    self.infrastructure.remove_edge(*ids)

                    if report is True:
                        print(">>> add: " + str(new_edge_object_1))
                        print(">>> add: " + str(new_edge_object_2))

                    anything_happened = True

            if anything_happened is True:
                break

        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Junction

    model = Model(proximity_radius=1)
    object_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
    object_2 = Junction(pos=[5, 0.5])
    model.add(object_1, object_2)

    rule = Rule_1(model.infrastructure)
    rule.apply(report=True)