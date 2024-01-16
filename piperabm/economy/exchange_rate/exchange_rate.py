import networkx as nx

from piperabm.object import PureObject


class ExchangeRate(PureObject):
    """
    Save exchange rates and calculate (target = rate * source)
    """
    def __init__(self):
        self.G = nx.DiGraph()
        super().__init__()

    def add(self, source, target="currency", rate=1):
        """
        Add a new known exchange rate between *source* and *target*
        """
        self.G.add_edge(source, target, rate=rate)
        self.G.add_edge(target, source, rate=1/rate)

    def rate(self, source, target="currency"):
        """
        Calculate exchange rate between *source* and *target*
        """
        nodes = nx.shortest_path(self.G, source, target)
        rate = 1
        for i, _ in enumerate(nodes):
            if i != 0:
                rate *= self.G[nodes[i-1]][nodes[i]]["rate"]
        return rate
    
    def price(self, name: str):
        """
        Return price of the source
        """
        return self.rate(source=name, target='currency')

    @property
    def names(self):
        """
        Return name of all resources
        """
        return list(self.G.nodes())
    
    def __call__(self, source, target):
        return self.rate(source, target)
    
    def serialize(self) -> dict:
        dictionary = {}
        names = self.names
        names.remove("currency")
        for name in names:
            dictionary[name] = self.rate(source=name, target="currency")
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.G = nx.DiGraph()
        for name in dictionary:
            source = name
            target = "currency"
            rate = dictionary[source]
            self.add(source, target, rate)


if __name__ == "__main__":
    exchange_rate = ExchangeRate()
    exchange_rate.add(source="food", rate=10)
    exchange_rate.add(source="water", rate=2)
    rate = exchange_rate("food", "water")
    print(rate)
