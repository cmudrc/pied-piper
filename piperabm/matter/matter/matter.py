from piperabm.object import PureObject
from piperabm.economy import ExchangeRate


class Matter(PureObject):
    """
    Represent a change in matter
    """

    type = 'matter'

    def __init__(
        self,
        name: str = '',
        amount: float = 0
    ):
        self.name = name
        self.amount = amount

    def value(self, exchange_rate: ExchangeRate):
        """
        Calculate monetary value of resources based on exchange rate
        """
        return self.amount * exchange_rate.price(name=self.name)
    
    def from_value(self, value, exchange_rate: ExchangeRate):
        """
        Amount based on value
        """
        price = exchange_rate.price(name=self.name)
        self.amount = value / price

    def dict(self):
        """
        Return dictionary representation
        """
        return {
            'name': self.name,
            'amount': self.amount,
        }
    
    def from_dict(self, dictionary: dict):
        """
        Load from dictionary representation
        """
        self.name = dictionary['name']
        self.amount = dictionary['amount']

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'amount': self.amount,
            'type': self.type,
        }

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.name = dictionary['name']
        self.amount = dictionary['amount']

    def __add__(self, other):
        if isinstance(other, (int, float)):
            """ Matter = Matter + (int, flaot) """
            new_amount = self.amount + other
            new_matter = Matter(name=self.name, amount=new_amount)
            return new_matter
        elif isinstance(other, Matter):
            """ Matter = Matter + Matter """
            if other.name == self.name:
                new_matter = self.__add__(other.amount)
                return new_matter
            else:
                raise ValueError
        else:
            raise ValueError
        
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            """ Matter = Matter - (int, flaot) """
            new_amount = self.amount - other
            new_matter = Matter(name=self.name, amount=new_amount)
            return new_matter
        elif isinstance(other, Matter):
            """ Matter = Matter - Matter """
            if other.name == self.name:
                new_matter = self.__sub__(other.amount)
                return new_matter
            else:
                raise ValueError
        else:
            raise ValueError
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            """ Matter = Matter * (int, flaot) """
            new_amount = self.amount * other
            return Matter(name=self.name, amount=new_amount)
        elif isinstance(other, Matter):
            """ Matter = Matter * Matter """
            if other.name == self.name:
                new_amount = self.__mul__(other.amount)
                return new_amount
            else:
                raise ValueError
        else:
            raise ValueError
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            """ (int, flaot) = Matter / (int, flaot) """
            ratio = self.amount / other
            return ratio
        elif isinstance(other, Matter):
            if other.name == self.name:
                """ (int, flaot) = Matter / Matter """
                ratio = self.__truediv__(other.amount)
                return ratio
            else:
                raise ValueError
        else:
            raise ValueError
        

if __name__ == '__main__':
    matter = Matter(
        name='food',
        amount=5
    )
    matter.print
