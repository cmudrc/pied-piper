from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter import Matter, DeltaMatter, DeltaMatters
from piperabm.economy import ExchangeRate


class Matters(PureObject):
    """
    A container to contain Matter objects
    """

    type = 'resources'

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, Matter):
                self.add(arg)

    def add(self, matter: Matter):
        """
        Add new resource to the library
        """
        name = matter.name
        if name != '' and name is not None:
            if name not in self.names:
                self.library[name] = matter
            else:
                pass
        else:
            raise ValueError

    @property
    def names(self):
        """
        Return name of all resources
        """
        return self.library.keys()
    
    def get(self, name):
        """
        Get the resource object based on its name
        """
        return self.library[name]  
    
    def __call__(self, name):
        return self.library[name].amount

    def value(self, exchange_rate: ExchangeRate, total=True):
        """
        Calculate monetary value based on exchange rate
        """
        values = {}
        for name in self.names:
            matter = self.get(name)
            values[name] = matter.value(exchange_rate)
        if total is True:
            result = 0
            for name in values:
                result += values[name]
        else:
            result = values
        return result
    
    def to_delta_matters(self):
        """
        Convert Matter object to DeltaMatter object
        """
        delta_matters = DeltaMatters()
        for name in self.names:
            matter = self.get(name)
            delta_matter = matter.to_delta_matter()
            delta_matters.add(delta_matter)
        return delta_matters

    def serialize(self) -> dict:
        library_serialized = {}
        for name in self.names:
            item = self.get(name)
            library_serialized[name] = item.serialize()
        return {
            'library': library_serialized,
            'type': self.type,
        }

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        library_serialized = dictionary['library']
        for name in library_serialized:
            item_serialized = library_serialized[name]
            item = Matter()
            item.deserialize(item_serialized)
            self.add(item)
    
    def __add__(self, other):

        if isinstance(other, dict):
            other_delta_matters = DeltaMatters()
            other_delta_matters.from_amounts(other)
            return self.__add__(other_delta_matters)
        
        elif isinstance(other, DeltaMatter):
            if other.name in self.names:
                matter = self.get(other.name)
                remainder = matter.__add__(other)
                return remainder
            
        elif isinstance(other, DeltaMatters):
            remainders = DeltaMatters()
            for name in other.names:
                other_matter = other.get(name)
                remainder = self.__add__(other_matter)
                remainders.add(remainder)
            return remainders
        
        elif isinstance(other, Matter):
            other = other.to_delta_matter()
            return self.__add__(other)
        
        elif isinstance(other, Matters):
            other_delta_matters = other.to_delta_matters()
            return self.__add__(other_delta_matters)
        
        else:
            raise ValueError
        
    def __sub__(self, other):

        if isinstance(other, dict):
            other_delta_matters = DeltaMatters()
            other_delta_matters.from_amounts(other)
            return self.__sub__(other_delta_matters)
        
        elif isinstance(other, DeltaMatter):
            if other.name in self.names:
                matter = self.get(other.name)
                remainder = matter.__sub__(other)
                return remainder
            
        elif isinstance(other, DeltaMatters):
            remainders = DeltaMatters()
            for name in other.names:
                other_matter = other.get(name)
                remainder = self.__sub__(other_matter)
                remainders.add(remainder)
            return remainders
        
        elif isinstance(other, Matter):
            other = other.to_delta_matter()
            return self.__sub__(other)
        
        elif isinstance(other, Matters):
            other_delta_matters = other.to_delta_matters()
            return self.__sub__(other_delta_matters)
        
        else:
            raise ValueError

    def __mul__(self, other):
        
        if isinstance(other, dict):
            for name in other:
                matter = self.get(name)
                matter * other[name]
        
        else:
            raise ValueError
        
    def __truediv__(self, other):

        if isinstance(other, dict):
            result = {}
            for name in other:
                matter = self.get(name)
                result[name] = matter / other[name]
            return result
        
        elif isinstance(other, DeltaMatter):
            other = {other.name: other.amount}
            return self.__truediv__(other)
        
        elif isinstance(other, DeltaMatters):
            other = other.amounts()
            return self.__truediv__(other)
        
        elif isinstance(other, Matter):
            other = {other.name: other.amount}
            return self.__truediv__(other)
        
        elif isinstance(other, Matters):
            other = other.to_delta_matters()
            other = other.amounts()
            return self.__truediv__(other)
        
        else:
            raise ValueError
    

if __name__ == '__main__':

    from piperabm.matter.matter.samples import matter_0 as food
    from piperabm.matter.matter.samples import matter_1 as water
    from piperabm.matter.matter.samples import matter_2 as energy
    
    matters = Matters(food, water, energy)
    matters.print