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
        return {
            'name': self.name,
            'amount': self.amount,
        }
    
    def from_dict(self, dictionary: dict):
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
            new_amount = self.amount + other
            return Matter(name=self.name, amount=new_amount)
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
            return Matter(name=self.name, amount=new_amount)
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.__sub__(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            return Matter(name=self.name, amount=new_amount)
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.__mul__(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.amount / other
        elif isinstance(other, Matter):
            if other.name == self.name:
                return self.__truediv__(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        

if __name__ == '__main__':
    delta_matter = Matter(
        name='food',
        amount=5
    )
    delta_matter.print
