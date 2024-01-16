from piperabm.object import PureObject
from piperabm.matter.delta_matter import DeltaMatter
from piperabm.tools.symbols import SYMBOLS, serialize_symbol
#from piperabm.economy import ExchangeRate


class Matter(PureObject):

    type = 'matter'

    def __init__(
        self,
        name: str = '',
        amount: float = 0,
        max: float = SYMBOLS['inf'],
        min: float = 0
    ):
        super().__init__()

        self.name = name

        if max < 0:
            raise ValueError
        self.max = max

        if min < 0:
            raise ValueError
        self.min = min

        if self.max < self.min:
            raise ValueError

        self.amount = amount

    @property
    def source(self):
        """
        Calculate source
        """
        result = self.amount - self.min
        if result < 0:
            result = 0
        return result
    
    @property
    def demand(self):
        """
        Calcualte ideal demand
        """
        return self.max - self.amount
    
    def value(self, exchange_rate):
        """
        Calculate monetary value of matters based on exchange rate
        """
        amount = self.amount * exchange_rate.price(self.name)
        return amount
        #return Matter(name=self.name, amount=amount)

    @property
    def is_empty(self):
        """
        Check if the Matter is empty
        """
        result = False
        if self.amount == 0:
            result = True
        return result
    
    @property
    def is_full(self):
        """
        Check if the Matter is full
        """
        result = False
        if self.amount == self.max:
            result = True
        return result
    
    def serialize(self) -> dict:
        return {
            'name': self.name,
            'max': serialize_symbol(self.max),
            'min': self.min,
            'amount': self.amount,
            'type': self.type,
        }

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.name = dictionary['name']
        self.amount = dictionary['amount']
        self.max = float(dictionary['max'])
        self.min = dictionary['min']

    def add(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount + other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Matter(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.add(other.amount)
            else:
                raise ValueError
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.add(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        
    def sub(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount - other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Matter(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.sub(other.amount)
            else:
                raise ValueError
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.sub(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError

    def mul(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Matter(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.mul(other.amount)
            else:
                raise ValueError
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.mul(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        
    def truediv(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount / other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Matter(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.truediv(other.amount)
            else:
                raise ValueError
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.truediv(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
            
    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)
        
    def __truediv__(self, other):
        return self.truediv(other)


def calculate_remainder(amount, max, min):
    """
    Calculate remainder of Matter arithmetics
    """
    if max < min:
        raise ValueError
    remainder = 0
    if amount > max:
        remainder = amount - max
        amount = max
    elif amount < min:
        remainder = min - amount
        amount = min
    return amount, remainder


if __name__ == '__main__':
    matter = Matter(
        name='food',
        amount=6,
        max=10
    )
    remainder = matter + 5
    print(matter)
    print(remainder)