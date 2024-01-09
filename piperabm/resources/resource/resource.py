from piperabm.object import PureObject
from piperabm.tools.symbols import SYMBOLS, serialize_symbol
from piperabm.economy import ExchangeRate


class Resource(PureObject):

    type = 'resource'

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
        '''
        Calculate source
        '''
        result = self.amount - self.min
        if result < 0:
            result = 0
        return result
    
    @property
    def demand(self):
        '''
        Calcualte ideal demand
        '''
        return self.max - self.amount
    
    def value(self, exchange_rate: ExchangeRate):
        '''
        Calculate monetary value of resources based on exchange rate
        '''
        amount = self.amount * exchange_rate.rate(source=self.name, target='currency')
        return Resource(name=self.name, amount=amount)
    
    def value_to_amount(self, exchange_rate: ExchangeRate):
        '''
        Calculate equivalent amount of resources when the initial unit was money
        '''
        amount = self.amount / exchange_rate.rate(source=self.name, target='currency')
        return Resource(name=self.name, amount=amount)
    
    def cutoff(self, amount: float):
        '''
        If amount is higher than cutoff, it will be equal to cutoff
        '''
        if self.amount > amount:
            self.amount = amount

    @property
    def is_empty(self):
        '''
        Check if the resource is empty
        '''
        result = False
        if self.amount == 0:
            result = True
        return result
    
    @property
    def is_full(self):
        '''
        Check if the resource is full
        '''
        result = False
        if self.amount == self.max:
            result = True
        return result
    
    def add(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount + other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Resource(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.add(other.amount)
        
    def sub(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount - other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Resource(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.sub(other.amount)

    def mul(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Resource(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.mul(other.amount)
        
    def truediv(self, other) -> (int, float):
        if isinstance(other, (int, float)):
            new_amount = self.amount / other
            self.amount, remainder = calculate_remainder(new_amount, self.max, self.min)
            remainder = Resource(
                name=self.name,
                amount=remainder
            )
            return remainder
        elif isinstance(other, Resource):
            if other.name == '' or other.name == self.name:
                return self.truediv(other.amount)
    
    def serialize(self) -> dict:
        return {
            'name': self.name,
            'max': serialize_symbol(self.max),
            'min': self.min,
            'amount': self.amount
        }

    def deserialize(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.amount = dictionary['amount']
        self.max = float(dictionary['max'])
        self.min = dictionary['min']


def calculate_remainder(amount, max, min):
    '''
    Calculate remainder of resource arithmetics
    '''
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
    resource = Resource(
        name='food',
        amount=6,
        max=10
    )
    remainder = resource.truediv(0.5)
    print(resource)
    print(remainder)