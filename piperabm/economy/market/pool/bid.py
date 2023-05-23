from copy import deepcopy


class Bid:
    """
    Represent agent participation in the pool in form of placing a bid
    """

    def __init__(self, agent: int, amount: float):
        self.agent = agent
        self.initial_amount = amount
        self.amount = deepcopy(amount)

    def to_delta(self, exchange_rate):
        return self.delta_amount(), self.delta_wallet(exchange_rate)

    def delta_amount(self):
        """
        Return diff between starting state and current state of bid
        """
        return self.amount - self.initial_amount

    def delta_wallet(self, exchange_rate):
        """
        Return diff between starting state and current state of bid
        """
        return self.delta_amount() * exchange_rate

    def __str__(self):
        txt = '>>> agent: ' + str(self.agent) + ' amount: ' + str(self.initial_amount) + ' new_amount: ' + str(self.amount)
        return txt

    def __eq__(self, other):
        result = False
        if self.agent == other.agent and self.amount == other.new_amount:
            result = True
        return result
    

if __name__ == "__main__":
    b = Bid(agent=1, amount=5)
    print(b)