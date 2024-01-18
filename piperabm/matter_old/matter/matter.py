from piperabm.object import PureObject
from piperabm.matter.matter import Matter
from piperabm.tools.symbols import SYMBOLS, serialize_symbol
#from piperabm.economy import ExchangeRate


class Container(PureObject):
    """
    Represent matter (in a physical medium)
    """

    type = 'matter'

    def __init__(
        self,
        name: str = '',
        amount: float = 0,
        max: float = SYMBOLS['inf'],
        min: float = 0
    ):
        super().__init__()

        if max < 0:
            raise ValueError
        self.max = max

        if min < 0:
            raise ValueError
        self.min = min

        if self.max < self.min:
            raise ValueError


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
        return self.amount * exchange_rate.price(self.name)

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
    
    def to_delta_matter(self):
        """
        Convert Matter object to DeltaMatter object
        """
        return DeltaMatter(
            name=self.name,
            amount=self.amount
        )
    
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

    def __add__(self, other):

        if isinstance(other, (int, float)):
            new_amount = self.amount + other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = DeltaMatter(
                name=self.name,
                amount=remainder
            )
            return remainder
        
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.__add__(other.amount)
            else:
                raise ValueError
            
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.__add__(other.amount)
            else:
                raise ValueError
            
        else:
            raise ValueError
        
    def __sub__(self, other):

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
                return self.__sub__(other.amount)
            else:
                raise ValueError
            
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.__sub__(other.amount)
            else:
                raise ValueError
            
        else:
            raise ValueError

    def __mul__(self, other):

        if isinstance(other, (int, float)):
            self.amount *= other
            self.min *= other
            self.max *= other

        else:
            raise ValueError
        
    def __truediv__(self, other) -> (int, float):

        if isinstance(other, (int, float)):
            return self.amount / other
        
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.__truediv__(other.amount)
            else:
                raise ValueError
            
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.__truediv__(other.amount)
            else:
                raise ValueError
            
        else:
            raise ValueError


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