from piperabm.graphics.plt.resource import use_to_plt, produce_to_plt


class FlowNode:
    """
    Resource production/use rate.
    """

    def __init__(self, rate=0):
        """
        Args:
            rate: rate of production/use
        """
        self.rate = rate
        self.current_amount = 0

    def refill(self, delta_t, mode='independent'):
        max_amount = self.rate * delta_t
        refill_amount = max_amount - self.current_amount
        if mode == 'independent':
            self.current_amount += refill_amount

    def sub(self, amount: float):
        if amount is None:
            amount = 0
        if amount > self.current_amount:
            amount -= self.current_amount
            self.current_amount = 0
        else:
            self.current_amount -= amount
            amount = 0
        return amount

    def to_dict(self):
        dictionary = {
            'rate': self.rate,
            'current_amount': self.current_amount,
        }
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.rate = d['rate']
        self.current_amount = d['current_amount']


class Use(FlowNode):
    """
    A use node.
    """

    def __init__(self, rate=0):
        super().__init__(
            rate=rate
        )

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        use_to_plt(self.to_dict(), ax)


class Produce(FlowNode):
    """
    A produce node.
    """

    def __init__(self, rate=0):
        super().__init__(
            rate=rate
        )

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        produce_to_plt(self.to_dict(), ax)


if __name__ == "__main__":
    p = Produce(rate=5)
    p.refill(delta_t=2)
    print('self.current_amount: ', p.current_amount)

    amount = 9
    print('>>> sub amount: ', amount)
    remaining_amount = p.sub(amount=amount)
    print('remaining amount: ', remaining_amount)
    print('self.current_amount: ', p.current_amount)
