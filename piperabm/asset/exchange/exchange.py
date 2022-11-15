import networkx as nx


class Exchange:

    def __init__(self):
        self.G = nx.DiGraph()

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


if __name__ == "__main__":
    exchange = Exchange()
    exchange.add('food', 'wealth', 10)
    exchange.add('water', 'wealth', 2)
    rate = exchange.rate('food', 'water')
    print(rate)