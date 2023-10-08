import networkx as nx

from piperabm.object import PureObject
from piperabm.resource import Resource


class ExchangeRate(PureObject):
    """
    Save exchange rates and calculate (target = rate * source)
    """
    def __init__(self):
        self.G = nx.DiGraph()
        super().__init__()

    def __call__(self, source, target):
        return self.rate(source, target)

    def add(self, source, target, rate):
        """
        Add a new known exchange rate between *source* and *target*
        """
        self.G.add_edge(source, target, rate=rate)
        self.G.add_edge(target, source, rate=1/rate)

    def rate(self, source, target):
        """
        Calculate exchange rate between *source* and *target*
        """
        nodes = nx.shortest_path(self.G, source, target)
        rate = 1
        for i, _ in enumerate(nodes):
            if i != 0:
                rate *= self.G[nodes[i-1]][nodes[i]]['rate']
        return rate
    
    def value(self, resource: Resource, target='wealth') -> float:
        return resource.amount * self.rate(source=resource.name, target=target)
    
    def to_dict(self) -> list:
        G_prime = nx.Graph(self.G)
        dictionary = {}
        for edge in G_prime.edges():
            rate = self.rate(source=edge[0], target=edge[1])
            dictionary[edge[0]] = {
                'to': edge[1],
                'rate': rate,
            }
        return dictionary
    
    def from_dict(self, dictionary: list) -> None:
        self.G = nx.DiGraph() # reset
        for item in dictionary:
            source = item
            target = dictionary[source]['to']
            rate = dictionary[source]['rate']
            self.add(source, target, rate)


if __name__ == "__main__":
    exchange_rate = ExchangeRate()
    exchange_rate.add('food', 'wealth', 10)
    exchange_rate.add('water', 'wealth', 2)
    rate = exchange_rate('food', 'water')
    print(rate)
