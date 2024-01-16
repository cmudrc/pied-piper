from piperabm.object import PureObject
from piperabm.economy import ExchangeRate


class DeltaMatter(PureObject):

    type = 'delta matter'

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
    
    def of_value(self, value, exchange_rate: ExchangeRate):
        """
        Amount based on value
        """
        price = exchange_rate.price(name=self.name)
        self.amount = value / price

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

    def add(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount + other
            return DeltaMatter(name=self.name, amount=new_amount)
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.add(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        
    def sub(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount - other
            return DeltaMatter(name=self.name, amount=new_amount)
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.sub(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        
    def mul(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            return DeltaMatter(name=self.name, amount=new_amount)
        elif isinstance(other, DeltaMatter):
            if other.name == self.name:
                return self.mul(other.amount)
            else:
                raise ValueError
        else:
            raise ValueError
        
    def truediv(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount / other
            return DeltaMatter(name=self.name, amount=new_amount)
        elif isinstance(other, DeltaMatter):
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
        

if __name__ == '__main__':
    delta_matter = DeltaMatter(
        name='food',
        amount=5
    )
    delta_matter.print
