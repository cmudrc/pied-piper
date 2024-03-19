import networkx as nx

from piperabm.economy.trade.pair_solver import PairSolver


class MultiSolver:
    """
    Solve a trade between multiple agents for a single resource in a fixed price
    """
    def __init__(self, price):
        self.price = price
        self.library = {}
        self.trades = nx.DiGraph()

    def add(self, id, resource, currency, critical):
        for other_id in self.library:
            # Add as seller
            self.trades.add_edge(id, other_id)
            # Add as buyer
            self.trades.add_edge(other_id, id)
        # Add to library
        self.library[id] = {
            'resource': resource,
            'currency': currency,
            'critical': critical,
        }

    @property
    def possible_pairs(self):
        return list(self.trades.edges())
    
    def attribute(self, pair, attribute):
        return self.trades.edges[pair][attribute]
    
    def value(self, pair):
        price = self.attribute(pair, 'price')
        amount = self.attribute(pair, 'amount')
        return price * amount
    
    @property
    def max_trade(self):
        max_transaction_value = None
        max_pair = None
        for pair in self.possible_pairs:
            transaction_value = self.value(pair)
            if max_transaction_value is None or \
            transaction_value > max_transaction_value:
                max_pair = pair
                max_transaction_value = transaction_value
        return {
            'amount': self.attribute(max_pair, 'amount'),
            'price': self.attribute(max_pair, 'price'),
            'seller': max_pair[0],
            'buyer': max_pair[1],
        }

    def solve(self):
        # Assuming price is fixed and both parties are rational and looking to maximize their utilities
        for pair in self.possible_pairs:
            seller_id = pair[0]
            buyer_id = pair[1]
            solver = PairSolver(self.price)
            agent = self.library[seller_id]
            solver.add_seller(
                id=seller_id,
                resource=agent['resource'],
                currency=agent['currency'],
                critical=agent['critical']
            )
            agent = self.library[buyer_id]
            solver.add_buyer(
                id=buyer_id,
                resource=agent['resource'],
                currency=agent['currency'],
                critical=agent['critical']
            )
            transaction = solver.solve()
            self.trades.edges[pair]['amount'] = transaction['amount']
            self.trades.edges[pair]['price'] = transaction['price']
        return self.max_trade
    

if __name__ == "__main__":
    solver = MultiSolver(price=1)
    solver.add(
        id=1,
        resource=5,
        currency=3,
        critical=8,
    )
    solver.add(
        id=2,
        resource=5,
        currency=1,
        critical=3,
    )
    solver.add(
        id=3,
        resource=5,
        currency=3,
        critical=5,
    )
    result = solver.solve()
    print(result)