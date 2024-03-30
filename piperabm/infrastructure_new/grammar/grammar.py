from piperabm.infrastructure_new.grammar.rules import *


class Grammar:

    def __init__(self, infrastructure, save=False):
        self.infrastructure = infrastructure
        self.save = save
    
    def apply(self, report=False):
        """
        Apply all grammars based on a decision tree
            if a rule is not yielding any changes, it is ok to go the next rule.
            if not, all grammars rules start over.
            if no next rule is available, the program is over.
        """

        rules = [
            Rule_0(self.infrastructure),
            Rule_1(self.infrastructure),
            Rule_2(self.infrastructure),
            Rule_3(self.infrastructure),
        ]

        if self.save is True:
            self.infrastructure.save()

        i = 0
        while True:
            rule = rules[i]
            anything_happened = rule.find(report=report)

            if anything_happened is True:
                if self.save is True:
                    self.infrastructure.save()
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar

            if i == len(rules): # Done
                self.infrastructure.baked = True
                if self.save is True:
                    self.infrastructure.save()
                break  # exit if all grammars are applied without any changes


if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure, Home, Street

    infrastructure = Infrastructure(proximity_radius=1)
    object_1 = Street(pos_1=[-10, 0], pos_2=[10, 0])
    object_2 = Street(pos_1=[0, -10], pos_2=[0, 10])
    object_3 = Home(pos=[5, 0.5])
    infrastructure.add(object_1)
    infrastructure.add(object_2)
    infrastructure.add(object_3)
    grammar = Grammar(infrastructure)
    grammar.apply(report=True)