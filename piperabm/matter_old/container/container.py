from piperabm.object import PureObject
from piperabm.matter.matter import Matter
from piperabm.tools.symbols import SYMBOLS, serialize_symbol
from piperabm.economy import ExchangeRate


class Container(PureObject):
    """
    Represent a physical medium containing matter
    """

    type = 'container'

    def __init__(
        self,
        matter: Matter = None,
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

        if matter is None:
            matter = Matter(name='', amount=0)
        if matter.amount > self.max:
            raise ValueError
        self.matter = matter

    @property
    def name(self):
        return self.matter.name
    
    @property
    def amount(self):
        return self.matter.amount

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
    
    def value(self, exchange_rate: ExchangeRate):
        """
        Calculate monetary value of matters based on exchange rate
        """
        return self.matter.value(exchange_rate)

    @property
    def is_empty(self):
        """
        Check if the Matter is empty
        """
        result = False
        if self.amount <= SYMBOLS['eps']:
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
            'max': serialize_symbol(self.max),
            'min': self.min,
            'matter': self.matter.serialize(),
            'type': self.type,
        }

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.matter = Matter()
        self.matter.deserialize(dictionary['matter'])
        self.max = float(dictionary['max'])
        self.min = dictionary['min']

    def __add__(self, other):
        if isinstance(other, (int, float)):
            """ Matter = Container + (int, flaot) """
            new_amount = self.amount + other
            self.matter.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Matter(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, Matter):
            """ Matter = Container + Matter """
            if other.name == self.name:
                remainder = self.__add__(other.amount)
                return remainder
            else:
                raise ValueError
        elif isinstance(other, Container):
            """ Container = Container + Container """
            if other.name == self.name:
                new_container = Container(
                    matter=self.matter+other.matter,
                    max=self.max+other.max,
                    min=self.min+other.min
                )
                return new_container
            else:
                raise ValueError
        else:
            raise ValueError
        
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            """ Matter = Container - (int, flaot) """
            new_amount = self.amount - other
            self.matter.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Matter(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, Matter):
            """ Matter = Container - Matter """
            if other.name == self.name:
                remainder = self.__sub__(other.amount)
                return remainder
            else:
                raise ValueError
        elif isinstance(other, Container):
            """ Container = Container - Container """
            if other.name == self.name:
                new_container = Container(
                    matter=self.matter-other.matter,
                    max=self.max-other.max,
                    min=self.min-other.min
                )
                return new_container
            else:
                raise ValueError
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            """ Container = Container * (int, flaot) """
            new_matter = Matter(
                name=self.name,
                amount=self.amount*other
            )
            new_container = Container(
                matter=new_matter,
                min=self.min*other,
                max=self.max*other
            )
            return new_container
        else:
            raise ValueError
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            """ Container = Container / (int, flaot) """
            new_container = self.__mul__(1 / other)
            return new_container
        elif isinstance(other, Matter):
            """ (int, float) = Container / Matter """
            if other.name == self.name:
                ratio = self.amount / other.amount
                return ratio
            else:
                raise ValueError
        elif isinstance(other, Container):
            """ (int, float) = Container / Container """
            if other.name == self.name:
                ratio = self.__truediv__(other.matter)
                return ratio
            else:
                raise ValueError
        else:
            raise ValueError


def calculate_remainder(amount, max, min):
    """
    Calculate remainder
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
        amount=6
    )
    container = Container(
        matter,
        max=10,
        min=2
    )
    print(container)
