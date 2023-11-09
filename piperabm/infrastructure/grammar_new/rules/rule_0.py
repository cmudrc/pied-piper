from piperabm.infrastructure.grammar_new.rules.rule import Rule
from piperabm.tools.coordinate.distance import distance_point_to_point


class Rule_0(Rule):
    """
    Condition for node to node proximity
    """

    def __init__(self, model):
        name = "rule 0"
        super().__init__(model, name)

    def check(self, node_item, other_node_item):
        distance = distance_point_to_point(node_item.pos, other_node_item.pos)
        return distance < self.proximity_radius
    
    def apply(self):
        anything_happened = False
        for node_index in self.nodes:
            for other_node_index in self.nodes:
                if node_index != other_node_index:
                    node_item = self.get(node_index)
                    other_node_item = self.get(other_node_index)
                    if self.check(node_item, other_node_item):
                        ''' update the items based on their types '''
                        if node_item.type == 'junction' and other_node_item.type != 'junction':
                            self.remove(node_item.index)
                            #self.report.append(str(node_item) + ' removed.')
                            anything_happened = True
                            break
                        elif node_item.type == 'junction' and other_node_item.type == 'junction':
                            self.remove(node_item.index)
                            #self.report.append(str(node_item) + ' removed.')
                            anything_happened = True
                            break
                        elif node_item.type != 'junction' and other_node_item.type == 'junction':
                            self.remove(other_node_item.index)
                            #self.report.append(str(other_node_item) + ' removed.')
                            anything_happened = True
                            break
                        elif node_item.type != 'junction' and other_node_item.type != 'junction':
                            print("close items are not resolved")
                            raise ValueError
            if anything_happened is True:
                break      
        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model.samples import model_2 as model

    rule = Rule_0(model)