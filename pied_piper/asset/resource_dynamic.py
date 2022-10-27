class DynamicSource:
    """
    Resource production/use rate.
    """

    def __init__(self, rate=0):
        """
        Args:
            rate: rate of production/use
        """
        self.rate = rate
        self.current_amount = None

    def refill(self, delta_t):
        max_charge = self.rate * delta_t
        self.current_amount = self.rate * delta_t

    def sub(self, amount:float):
        if amount > self.current_amount:
            amount -= self.current_amount
            self.current_amount = 0
        else:
            self.current_amount -= amount
            amount = 0
        return amount


class Use(DynamicSource):
    """
    A use node.
    """

    def __init__(self, rate=0):
        super().__init__(
            rate=rate
        )


class Produce(DynamicSource):
    """
    A produce node.
    """

    def __init__(self, rate=0):
        super().__init__(
            rate=rate
        )


if __name__ == "__main__":
    p = Produce(rate=5)
    p.refill(delta_t=2)
    print('self.current_amount: ', p.current_amount)

    amount = 9
    print('>>> sub amount: ', amount)
    remaining_amount = p.sub(amount=amount)
    print('remaining amount: ', remaining_amount)
    print('self.current_amount: ', p.current_amount)
