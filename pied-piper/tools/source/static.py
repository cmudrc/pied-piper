from copy import deepcopy


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

    def sub(self, amount: float):
        if amount > self.current_amount:
            amount -= self.current_amount
            self.current_amount = 0
        else:
            self.current_amount -= amount
            amount = 0
        return amount


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
    current_amount = 0
    max_amount = 10
    s = Storage(
        current_amount=0,
        max_amount=10
    )
    #print(p.current_amount)