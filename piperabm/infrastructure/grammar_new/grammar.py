from piperabm.infrastructure.grammar_new.rules import *


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
        rules = [
            Rule_0(self.model),
            Rule_1(self.model),
        ]

        i = 0
        while True:
            rule = rules[i]
            anything_happened = rule.apply()
            log = None

            if report is True:
                print(log)

            if anything_happened is True:
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar

            if i == len(rules):
                break  # exit if all grammars are applied without any changes
