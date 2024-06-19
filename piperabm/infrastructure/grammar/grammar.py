from piperabm.infrastructure.grammar.rules import *


class Grammar:
    """
    Manage and apply gramamr rules
    """

    def __init__(
            self,
            infrastructure,
            proximity_radius: float = 1,
            search_radius: float = None,
        ):
        self.infrastructure = infrastructure
        if search_radius is not None and \
        search_radius < proximity_radius:
            print("search radius should be bigger than proximity radius")
            raise ValueError
        self.search_radius = search_radius
        self.proximity_radius = proximity_radius

    def apply(self, report=False):
        """
        Apply all grammar rules
        """
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
        Apply all street grammar rules
            if a rule is not yielding any changes, it is ok to go the next rule.
            if not, all grammars rules start over.
            if no next rule is available, the program is over.
        """

        rules = [
            Rule0(self.infrastructure, self.proximity_radius),
            Rule1(self.infrastructure, self.proximity_radius),
            Rule2(self.infrastructure, self.proximity_radius),
        ]

        i = 0
        while True:
            rule = rules[i]
            anything_happened = rule.find(report=report)
            if anything_happened is True:
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar
            if i == len(rules): # Done
                break

    def apply_neighborhood_grammar(self, report=False):
        """
        Apply all neighborhood grammar rules
            if a rule is not yielding any changes, it is ok to go the next rule.
            if not, all grammars rules start over.
            if no next rule is available, the program is over.
        """

        rules = [
            Rule3(self.infrastructure, proximity_radius=self.proximity_radius, search_radius=self.search_radius),
        ]

        i = 0
        while True:
            rule = rules[i]
            anything_happened = rule.find(report=report)
            if anything_happened is True:
                i = 0  # reset the loop
            else:
                i += 1  # move to the next grammar
            if i == len(rules): # Done
                break


if __name__ == "__main__":

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[-10, 0], pos_2=[10, 0])
    infrastructure.add_street(pos_1=[0, -10], pos_2=[0, 10])
    infrastructure.add_home(pos=[5, 0.5])
    grammar = Grammar(infrastructure)
    grammar.apply(report=True)
    print(infrastructure.baked)
