from piperabm.infrastructure_new.grammar.rules import *


class Grammar:

    def __init__(
            self,
            infrastructure,
            proximity_radius: float = 1,
            search_radius: float = None,
            save: bool = False,
            name: str = "infrastructure"
        ):
        self.infrastructure = infrastructure
        if search_radius is not None and \
        search_radius < proximity_radius:
            print("search radius should be bigger than proximity radius")
            raise ValueError
        else:
            self.search_radius = search_radius
        self.proximity_radius = proximity_radius
        self.save = save
        self.name = name

    def apply(self, report=False):
        if self.save is True:
            self.infrastructure.save(name=self.name)

        # Baking streets
        if self.infrastructure.baked_streets is False:
            self.apply_street_grammar(report=report)
            self.infrastructure.baked_streets = True

        # Baking neighborhood
        if self.infrastructure.baked_neighborhood is False:
            self.apply_neighborhood_grammar(report=report)
            self.infrastructure.baked_neighborhood = True

    def apply_street_grammar(self, report=False):
        """
        Apply all grammars based on a decision tree
            if a rule is not yielding any changes, it is ok to go the next rule.
            if not, all grammars rules start over.
            if no next rule is available, the program is over.
        """

        rules = [
            Rule_0(self.infrastructure, self.proximity_radius),
            Rule_1(self.infrastructure, self.proximity_radius),
            Rule_2(self.infrastructure, self.proximity_radius),
        ]

        i = 0
        while True:
            rule = rules[i]
            anything_happened = rule.find(report=report)

            if anything_happened is True:
                if self.save is True:
                    self.infrastructure.save(name=self.name)
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar

            if i == len(rules): # Done
                if self.save is True:
                    self.infrastructure.save(name=self.name)
                break  # exit if all grammars are applied without any changes

    def apply_neighborhood_grammar(self, report=False):

        rules = [
            Rule_3(self.infrastructure, search_radius=self.search_radius),
        ]

        i = 0
        while True:
            rule = rules[i]
            anything_happened = rule.find(report=report)

            if anything_happened is True:
                if self.save is True:
                    self.infrastructure.save(name=self.name)
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar

            if i == len(rules): # Done
                if self.save is True:
                    self.infrastructure.save(name=self.name)
                break  # exit if all grammars are applied without any changes


if __name__ == "__main__":

    from piperabm.infrastructure_new import Infrastructure, Home, Street

    infrastructure = Infrastructure()
    object_1 = Street(pos_1=[-10, 0], pos_2=[10, 0])
    object_2 = Street(pos_1=[0, -10], pos_2=[0, 10])
    object_3 = Home(pos=[5, 0.5])
    infrastructure.add(object_1)
    infrastructure.add(object_2)
    infrastructure.add(object_3)
    grammar = Grammar(infrastructure)
    grammar.apply(report=True)
    print(infrastructure.baked)