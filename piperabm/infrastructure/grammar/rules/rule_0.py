from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.tools.coordinate import distance as ds


class Rule_0(Rule):
    """
    Condition for node to node proximity
    """

    def __init__(self, model):
        name = "rule 0"
        super().__init__(model, name)

    def check(self, node_item, other_node_item):
        result = False
        if node_item.type == "junction" or other_node_item.type == "junction":
            #print(node_item.pos, other_node_item.pos)
            distance = ds.point_to_point(
                point_1=node_item.pos,
                point_2=other_node_item.pos
            )
            if distance < self.proximity_radius:
                result = True
        return result
    
    def apply(self, report=False):
        anything_happened = False
        for node_index in self.nodes:
            for other_node_index in self.nodes:
                if node_index != other_node_index:
                    node_item = self.get(node_index)
                    other_node_item = self.get(other_node_index)
                    if self.check(node_item, other_node_item):
                        # Update the items based on their types
                        if node_item.type == 'junction':
                            node_to_remove = node_item
                        else:
                            node_to_remove = other_node_item
                        if report is True:
                            print(">>> remove: " + str(node_to_remove))
                        self.remove(node_to_remove.index)
                        anything_happened = True
                        break
                        
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