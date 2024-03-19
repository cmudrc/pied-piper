class PairSolver:
    """
    Solve a trade between two agents for a single resource in a fixed price
    """
    def __init__(self, price):
        self.price = price

    def add_buyer(self, id, resource, currency, critical):
        """
        Add buyer info
        """
        self.buyer = {
            'id': id,
            'resource': resource,
            'currency': currency,
            'critical': critical,
        }

    def add_seller(self, id, resource, currency, critical):
        """
        Add seller info
        """
        self.seller = {
            'id': id,
            'resource': resource,
            'currency': currency,
            'critical': critical,
        }

    def solve(self):
        """
        Solve the trade based on Nash Bargaining
        """
        # Seller
        willingness_to_sell = self.seller['resource'] - self.seller['critical']
        if willingness_to_sell < 0:
            willingness_to_sell = 0
        # Buyer
        willingness_to_buy_resource = self.buyer['critical'] - self.buyer['resource']
        if willingness_to_buy_resource < 0:
            willingness_to_buy_resource = 0
        ability_to_buy_resource = self.buyer['currency'] / self.price
        willingness_to_buy = min(willingness_to_buy_resource, ability_to_buy_resource)
        # Trade
        resource_amount = min(willingness_to_sell, willingness_to_buy)
        #trade_amount = trade_amount_resource * self.price
        #return trade_amount
        transaction = {
            'amount': resource_amount,
            'price': self.price
        }
        return transaction
    

if __name__ == "__main__":
    solver = PairSolver(price=1)
    solver.add_buyer(
        id=1,
        resource=5,
        currency=3,
        critical=8,
    )
    solver.add_seller(
        id=2,
        resource=5,
        currency=1,
        critical=3,
    )
    result = solver.solve()
    print(result)