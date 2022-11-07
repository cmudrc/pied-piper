from copy import deepcopy
from pr.graphics.plt.resource import storage_to_plt, deficiency_to_plt


class StaticSource:
    """
    Resource static storage.
    """

    def __init__(self, current_amount=0, max_amount=None):
        """
        Args:
            current_amount: current amount
            max_amount: maximum amount
        """

        self.current_amount = current_amount
        self.max_amount = max_amount

    def add(self, amount: float):
        if amount is None: amount = 0
        if amount < 0: raise ValueError
        if self.max_amount is None:
            self.current_amount += amount
            amount = 0
        else:
            gap = self.max_amount - self.current_amount
            if gap > amount:
                self.current_amount += amount
                amount = 0
            else:
                self.current_amount = deepcopy(self.max_amount)
                amount = amount - gap
        return amount

    def sub(self, amount: float):
        if amount is None: amount = 0
        if amount < 0: raise ValueError
        if amount > self.current_amount:
            amount -= self.current_amount
            self.current_amount = 0
        else:
            self.current_amount -= amount
            amount = 0
        return amount

    def __str__(self):
        txt = ''
        txt += 'current: ' + str(self.current_amount) + ' '
        txt += 'max: ' + str(self.max_amount)
        return txt

    def to_dict(self):
        dictionary = {
            'current_amount': self.current_amount,
            'max_amount': self.max_amount,
        }
        return dictionary

    def from_dict(self, dictionary:dict):
        d = dictionary
        self.current_amount = d['current_amount']
        self.max_amount = d['current_amount']


class Deficiency(StaticSource):
    """
    Represent deficiency like a storage unit.
    """

    def __init__(self, max_amount, current_amount=0):
        super().__init__(
            current_amount=current_amount,
            max_amount=max_amount
        )

    def is_alive(self):
        if self.current_amount >= self.max_amount:
            return False
        else:
            return True

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        deficiency_to_plt(self.to_dict(), ax)


class Storage(StaticSource):
    """
    Simple storage unit.
    """

    def __init__(self, current_amount=0, max_amount=None):
        super().__init__(
            current_amount=current_amount,
            max_amount=max_amount
        )

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        storage_to_plt(self.to_dict(), ax)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)

    s = Storage(
        current_amount=1,
        max_amount=15
    )
    s.to_plt()
    plt.show()

    print(s)
    amount = 20
    print('add: ', amount)
    remaining = s.add(amount)
    print('remaining: ', remaining)
    print(s)