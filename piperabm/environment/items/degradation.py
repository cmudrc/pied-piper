class Degradation:

    def __init__(
        self,
        total: int = float('inf'),
        current: int = 0
    ):
        self.total = total
        self.current = current

    def add(self, amount: int = 0):
        """ Add usage """
        self.current += amount

    @property
    def factor(self):
        """ Calculate degradation factor """
        return self.current / self.total


if __name__ == "__main__":
    degradation = Degradation(
        total=100,
        current=0
    )
    degradation.add(10)
    print(degradation.factor)
