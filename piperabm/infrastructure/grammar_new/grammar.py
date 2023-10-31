class Grammar:

    def __init__(self, model):
        self.model = model

    @property
    def nodes(self):
        return self.model.all_environment_nodes
    
    @property
    def edges(self):
        return self.model.all_environment_edges
    
    def get(self, index):
        return self.model.get(index)
    
    def remove(self, index):
        self.model.remove(index)
    
    def apply(self, report=True):
        """
        Apply all grammars based on a decision tree
            if a rule is not yielding any changes, it is ok to go the next rule.
            if not, all grammars rules start over.
            if no next rule is available, the program is over.
        """
        grammars = [
            rule_1,
            rule_2,
            rule_3,
            rule_4,
        ]

        i = 0
        while True:
            anything_happened, log = grammars[i]()

            if report is True:
                print(log)

            if anything_happened is True:
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar

            if i == len(grammars):
                break  # exit if all grammars are applied without any changes
