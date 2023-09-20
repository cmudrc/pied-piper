from piperabm.object import PureObject


class Degradation(PureObject):

    def __init__(
        self,
        total: float = float('inf'),
        current: float = 0
    ):
        super().__init__()
        self.total = total
        self.current = current

    def add(self, amount: int = 0):
        """ Add usage """
        self.current += amount

    @property
    def factor(self):
        """ Calculate degradation factor """
        return self.current / self.total
    
    def serialize(self) -> dict:
        dictionary = {}
        dictionary['current'] = self.current
        dictionary['total'] = self.total
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.current = dictionary['current']
        self.total = dictionary['total']


if __name__ == "__main__":
    degradation = Degradation(
        total=100,
        current=0
    )
    degradation.add(10)
    print(degradation.factor)
