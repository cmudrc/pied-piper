from copy import deepcopy


class Bid:
    """
    Represent agent participation in the pool in form of placing a bid
    """

    def __init__(self, agent: int, amount: float):
        self.agent = agent
        self.amount = amount
        self.new_amount = deepcopy(amount)

    def delta_amount(self):
        """
        Return diff between starting state and current state of bid
        """
        return self.new_amount - self.amount

    def delta_wallet(self, exchange_rate):
        """
        Return diff between starting state and current state of bid
        """
        return self.delta_amount() * exchange_rate

    def __str__(self):
        txt = '>>> agent: ' + str(self.agent) + ' amount: ' + str(self.amount) + ' new_amount: ' + str(self.new_amount)
        return txt

    def __eq__(self, other):
        result = False
        if self.agent == other.agent and self.new_amount == other.new_amount:
            result = True
        return result
    

if __name__ == "__main__":
    b = Bid(agent=1, amount=5)