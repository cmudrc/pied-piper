from piperabm.infrastructure.grammar.rules.rule import Rule, Log
#from piperabm.tools.coordinate import distance as ds


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
        return result
    
    def apply(self, report=False):
        anything_happened = False
        for edge_id in self.edges:
            for other_edge_id in self.edges:
                if edge_id != other_edge_id:
                    if self.check(edge_id, other_edge_id) is True:
                        # Update
                        # Log
                        if report is True:
                            logs = []
                            log = Log(self.model, other_edge_id, 'removed')
                            logs.append(log)
                        # Remove
                        self.remove(other_edge_id)
                        # Report
                        if report is True:
                            self.report(logs)
                        # Inform an activity
                        anything_happened = True
            # Inform an activity
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Road
    from piperabm.infrastructure.grammar.rules.rule_0 import Rule_0

    model = Model(proximity_radius=1)
    item_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
    item_2 = Road(pos_1=[0, 0.5], pos_2=[9.5, 0])
    model.add(item_1, item_2)

    rule = Rule_0(model)
    rule.apply(report=True)
    rule.apply(report=True)
    rule = Rule_3(model)
    rule.apply(report=True)