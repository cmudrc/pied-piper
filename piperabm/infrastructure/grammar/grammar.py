from piperabm.infrastructure.grammar.rules import *


class Grammar:

    def __init__(self, model, save=False):
        self.model = model
        self.save = save
    
    def apply(self, report=False):
        """
        Apply all grammars based on a decision tree
            if a rule is not yielding any changes, it is ok to go the next rule.
            if not, all grammars rules start over.
            if no next rule is available, the program is over.
        """

        rules = [
            Rule_0(self.model),
            Rule_1(self.model),
            Rule_2(self.model),
            Rule_3(self.model),
            Rule_4(self.model),
            Rule_5(self.model),
        ]

        if self.save is True:
            self.model.save_initial()

        i = 0
        while True:
            rule = rules[i]
            if report is True:
                print(rule.name + ":")
            anything_happened = rule.apply(report=report)

            if anything_happened is True:
                if self.save is True:
                    self.model.save_initial()
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar

            if i == len(rules):
                self.model.baked = True
                break  # exit if all grammars are applied without any changes
