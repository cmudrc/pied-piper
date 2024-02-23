from piperabm.infrastructure.grammar.rules.rule import Rule


class Rule_5(Rule):
    """
    Condition for small edge removal
    """

    def __init__(self, model):
        name = "rule 5"
        super().__init__(model, name)

    def check(self, edge_id):
        result = False
        edge_object = self.get(edge_id)
        if edge_object.length_linear < self.proximity_radius:
            result = True
        return result
    
    def apply(self, report=False):
        anything_happened = False
        for edge_id in self.edges:
            if self.check(edge_id):
                # Update
                self.remove(edge_id)
                # Inform an activity
                anything_happened = True
                # Report
                if report is True:
                    print(">>> remove: " + str(edge_id))
                break
        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Road

    model = Model(proximity_radius=1)
    object = Road(pos_1=[0, 0], pos_2=[0.5, 0])
    model.add(object)

    rule = Rule_5(model)
    rule.apply(report=True)
