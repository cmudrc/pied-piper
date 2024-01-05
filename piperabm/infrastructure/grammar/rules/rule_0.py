from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.tools.coordinate.distance import point_to_point


class Rule_0(Rule):
    """
    Condition for node to node proximity
    """

    def __init__(self, model):
        name = "rule 0"
        super().__init__(model, name)

    def check(self, node_item, other_node_item):
        distance = point_to_point(node_item.pos, other_node_item.pos)
        return distance < self.proximity_radius
    
    def apply(self, report=False):
        anything_happened = False
        for node_index in self.nodes:
            for other_node_index in self.nodes:
                if node_index != other_node_index:
                    node_item = self.get(node_index)
                    other_node_item = self.get(other_node_index)
                    if self.check(node_item, other_node_item):
                        # Update the items based on their types

                        if node_item.type == "junction" and other_node_item.type != "junction":
                            if report is True:
                                print(">>> remove: " + str(node_item))
                            self.remove(node_item.index)
                            anything_happened = True
                            break

                        elif node_item.type == "junction" and other_node_item.type == "junction":
                            if report is True:
                                print(">>> remove: " + str(node_item))
                            self.remove(node_item.index)
                            anything_happened = True
                            break

                        elif node_item.type != "junction" and other_node_item.type == "junction":
                            if report is True:
                                print(">>> remove: " + str(other_node_item))
                            self.remove(other_node_item.index)
                            anything_happened = True
                            break

                        elif node_item.type != "junction" and other_node_item.type != "junction":
                            print("close items are not resolved")
                            raise ValueError
                        
            if anything_happened is True:
                break    

        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Junction

    model = Model(proximity_radius=1)
    item_1 = Junction(pos=[0, 0])
    item_2 = Junction(pos=[0.5, 0])
    model.add(item_1, item_2)

    rule = Rule_0(model)
    rule.apply(report=True)