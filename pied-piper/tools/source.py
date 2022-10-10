from copy import deepcopy


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
        self.current_amount = self.rate * delta_t

    def sub(self, amount):
        self.current_amount -= amount
        if self.current_amount < 0:
            self.current_amount = 0


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


class StaticSource:
    """
    Resource static storage.
    """

    def __init__(self, current_amount=0, max_amount=0):
        """
        Args:
            current_amount: current amount
            max_amount: maximum amount
        """

        self.current_amount = current_amount
        self.max_amount = max_amount

    def add(self, amount):
        self.current_amount += amount
        if self.current_amount > self.max_amount:
            self.current_amount = deepcopy(self.max_amount)

    def sub(self, amount):
        self.current_amount -= amount
        if self.current_amount < 0:
            self.current_amount = 0


class Deficiency(StaticSource):
    """
    Represent deficiency like a storage unit.
    """

    def __init__(self, current_amount=0, max_amount=0):
        super().__init__(
            current_amount=current_amount,
            max_amount=max_amount
        )

    def is_alive(self):
        if self.current_amount >= self.max_amount:
            return False
        else:
            return True


class Storage(StaticSource):
    """
    Simple storage unit.
    """

    def __init__(self, current_amount=0, max_amount=0):
        super().__init__(
            current_amount=current_amount,
            max_amount=max_amount
        )


if __name__ == "__main__":
    from unit import Unit

    rate = Unit(5, 'ton/day').to('kg/second').val
    p = Produce(rate=rate)
    delta_t=Unit(2, 'day').to('second').val
    p.refill(delta_t=delta_t)
    print(p.current_amount)
