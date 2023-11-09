from piperabm.infrastructure.grammar_new.rules.rule import Rule
from piperabm.infrastructure import Road
from piperabm.tools.coordinate.distance import distance_point_to_point, distance_point_to_line


class Rule_2(Rule):
    """
    Condition for edge to edge intersection
    """

    def __init__(self, model):
        name = "rule 2"
        super().__init__(model, name)

    def check(self, node_item, edge_item):
        distance = distance_point_to_line(node_item.pos, edge_item.pos_1, edge_item.pos_2)
        distance_1 = distance_point_to_point(node_item.pos, edge_item.pos_1)
        distance_2 = distance_point_to_point(node_item.pos, edge_item.pos_2)
        return distance is not None and \
            distance < self.proximity_radius and \
            distance_1 > self.proximity_radius and \
            distance_2 > self.proximity_radius
    
    def apply(self):
        anything_happened = False
        for edge_index in self.edges:
            for other_edge_index in self.edges:
                if edge_index != other_edge_index:
                    edge_item = self.get(edge_index)
                    other_edge_item = self.get(other_edge_index)
                    if self.check(edge_item, other_edge_item):
                        ''' update the items based on their types '''
                        intersection = [0, 0] #######
                        if edge_item.type == 'road' and other_edge_item.type == 'road':
                            new_edge_item_1 = Road(pos_1=edge_item.pos_1, pos_2=intersection)
                            new_edge_item_2 = Road(pos_1=intersection, pos_2=edge_item.pos_2)
                            new_edge_item_3 = Road(pos_1=other_edge_item.pos_1, pos_2=intersection)
                            new_edge_item_4 = Road(pos_1=intersection, pos_2=other_edge_item.pos_2)
                            self.add(new_edge_item_1)
                            #report.append(str(new_edge_item_1) + ' added.')
                            self.add(new_edge_item_2)
                            #report.append(str(new_edge_item_2) + ' added.')
                            self.add(new_edge_item_3)
                            #report.append(str(new_edge_item_3) + ' added.')
                            self.add(new_edge_item_4)
                            #report.append(str(new_edge_item_4) + ' added.')
                            self.remove(edge_index)
                            #report.append(str(edge_item) + ' removed.')
                            self.remove(other_edge_index)
                            #report.append(str(other_edge_item) + ' removed.')
                            anything_happened = True
            if anything_happened is True:
                break      
        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model.samples import model_2 as model

    rule = Rule_2(model)