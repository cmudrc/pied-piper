from typing import Any
from piperabm.object import PureObject
from piperabm.tools.symbols import SYMBOLS


class Resource(PureObject):

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

        if amount is None:
            amount = 0
        self.amount = amount

    @property
    def source(self):
        result = self.amount - self.min
        if result < 0:
            result = 0
        return result
    
    @property
    def demand(self):
        return self.max - self.amount
    
    def add(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount + other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.add(other.amount)
        
    def sub(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount - other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.sub(other.amount)

    def mul(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.mul(other.amount)
        
    def truediv(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount / other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.truediv(other.amount)
    
    def serialize(self) -> dict:
        return {
            'name': self.name,
            'max': self.max,
            'min': self.min,
            'amount': self.amount
        }

    def deserialize(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.amount = dictionary['amount']
        self.max = float(dictionary['max'])
        self.min = dictionary['min']


def calculate_remainder(amount, max, min):
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


if __name__ == "__main__":
    resource = Resource(
        name='food',
        amount=6,
        max=10
    )
    remainder = resource.truediv(0.5)
    print(resource)
    print(remainder)