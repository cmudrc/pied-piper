from piperabm.object import PureObject
from piperabm.tools.symbols import serialize_symbol


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
        """
        Add usage
        """
        self.current += amount

    def sub(self, amount: int = 0):
        """
        Sub usage
        """
        if amount <= self.current:
            self.add(-amount)
        else:
            raise ValueError

    @property
    def factor(self):
        """
        Calculate degradation factor
        """
        return self.function(self.current, self.total)
    
    def function(self, current, total):
        """
        Default function
        """
        return current / total

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['current'] = self.current
        dictionary['total'] = serialize_symbol(self.total)
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.current = float(dictionary['current'])
        self.total = float(dictionary['total'])


if __name__ == "__main__":
    degradation = Degradation(
        total=100,
        current=0
    )
    degradation.add(10)
    print(degradation.factor)
