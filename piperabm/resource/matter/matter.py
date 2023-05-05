from piperabm.object import Object
from piperabm.tools.symbols import SYMBOLS


class Matter(Object):

    def __init__(
        self,
        amount: float = None
    ):
        super().__init__()
        if amount is None:
            amount = 0
        if amount < 0:
            raise ValueError
        self.amount = amount

    def to_dict(self):
        #return {
        #    'amount': self.amount
        #}
        return self.amount
    
    def from_dict(self, dictionary) -> None:
        #self.amount = float(dictionary['amount'])
        self.amount = float(dictionary)

    def __call__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            self.amount += other
        elif isinstance(other, dict): # delta arithmetic
            return super().__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            self.amount -= other
        elif isinstance(other, Matter): # delta arithmetic
            return super().__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            self.amount *= other
        elif isinstance(other, Matter): # resource arithmetic
            other = other.amount
            return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            if other == 0:
                self.amount = SYMBOLS['inf']
            else:
                self.amount /= other
        elif isinstance(other, Matter): # resource arithmetic
            other = other.amount
            return self.__truediv__(other)
        
    
if __name__ == "__main__":
    matter = Matter(amount=6)
    matter * 2
    print(matter)