from piperabm.object import Object
from piperabm.resource.matter import Matter
from piperabm.tools.symbols import SYMBOLS


class Container(Object):

    def __init__(
        self,
        amount: float = None,
        max: float = None,
        min: float = None,
    ):
        super().__init__()

        if max is None:
            max = SYMBOLS['inf']
        if max < 0:
            raise ValueError
        self.max = max

        if min is None:
            min = 0
        if min < 0:
            raise ValueError
        self.min = min

        if amount is None:
            amount = 0
        self.matter = Matter(amount)

    def add_matter_object(self, matter: Matter):
        self.matter = matter

    @property
    def source(self):
        return self.matter.amount
    
    @property
    def demand(self):
        return self.max - self.matter.amount
    
    def __add__(self, other):
        matter = self.matter
        if isinstance(other, (int, float, Matter)): # resource arithmetic
            matter + other
            matter, remainder = remainder_calc(matter, self.max, self.min)
            return remainder
        
    def __sub__(self, other):
        matter = self.matter
        if isinstance(other, (int, float, Matter)): # resource arithmetic
            matter - other
            matter, remainder = remainder_calc(matter, self.max, self.min)
            return remainder

    def __mul__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            matter = self.matter
            matter * other
            matter, remainder = remainder_calc(matter, self.max, self.min)
            return remainder
        
    def __trudiv__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            matter = self.matter
            matter / other
            matter, remainder = remainder_calc(matter, self.max, self.min)
            return remainder
    
    def to_dict(self) -> dict:
        return {
            'max': self.max,
            'min': self.min,
            'matter': self.matter.to_dict(),
        }

    def from_dict(self, dictionary: dict) -> None:
        matter = Matter()
        matter.from_dict(dictionary['matter'])
        self.matter = matter
        self.max = float(dictionary['max'])
        self.min = float(dictionary['min'])


def remainder_calc(matter, max, min):
    if max < min:
        raise ValueError
    remainder = 0
    if matter.amount > max:
        remainder = matter.amount - max
        matter.amount = max
    elif matter.amount < min:
        remainder = min - matter.amount
        matter.amount = min
    return matter, remainder


if __name__ == "__main__":
    container = Container(
        amount=6,
        max=10
    )
    remainder = container * 2
    print(container)
    print(remainder)