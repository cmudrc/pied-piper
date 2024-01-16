from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter.delta_matter import DeltaMatter
from piperabm.economy import ExchangeRate


class DeltaMatters(PureObject):

    type = 'delta matters'

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, DeltaMatter):
                self.add_delta_matter(arg)

    def add_delta_matter(self, delta_matter: DeltaMatter):
        """
        Add new delta_resource to the library
        """
        name = delta_matter.name
        if name != '' and name is not None:
            self.library[name] = delta_matter
        else:
            raise ValueError
        
    def zeros(self, names: list):
        """
        Load library of empty matter with corresponding names
        """
        for name in names:
            delta_matter = DeltaMatter(name)
            self.add_delta_matter(delta_matter)

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
            delta_matter = self.get(name)
            values[name] = delta_matter.value(exchange_rate)
        if total is True:
            result = 0
            for name in values:
                result += values[name]
        else:
            result = values
        return result
    
    def of_values(self, values: dict, exchange_rate: ExchangeRate):
        """
        Calculate the amount of each delta_matter based on value and exchange rate
        """
        names = list(values)
        for name in names:
            delta_matter = DeltaMatter(name)
            delta_matter.of_value(values[name], exchange_rate)
            self.add_delta_matter(delta_matter)

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
            item = DeltaMatter()
            item.deserialize(item_serialized)
            self.add_delta_matter(item)

    def add(self, other):
        if isinstance(other, DeltaMatter):
            if other.name in self.names:
                result = deepcopy(self)
                result.library[other.name] = self.get(other.name) + other
                return result
            else:
                result = deepcopy(self)
                result.library[other.name] = other
                return result
        elif isinstance(other, DeltaMatters):
            result = deepcopy(self)
            for name in other.names:
                other_delta_matter = other.get(name)
                result = result.add(other_delta_matter)
            return result
        else:
            raise ValueError
        
    def sub(self, other):
        if isinstance(other, DeltaMatter):
            if other.name in self.names:
                result = deepcopy(self)
                result.library[other.name] = self.get(other.name) - other
                return result
            else:
                result = deepcopy(self)
                result.library[other.name] = other * -1
                return result
        elif isinstance(other, DeltaMatters):
            result = deepcopy(self)
            for name in other.names:
                other_delta_matter = other.get(name)
                result = result.sub(other_delta_matter)
            return result
        else:
            raise ValueError
        
    def mul(self, other):
        if isinstance(other, (int, float)):
            result = deepcopy(self)
            for name in self.names:
                result.library[name] = self.get(name) * other
            return result
        elif isinstance(other, DeltaMatter):
            if other.name in self.names:
                result = deepcopy(self)
                result.library[other.name] = self.get(other.name) * other
                return result
            else:
                result = deepcopy(self)
                return result
        elif isinstance(other, DeltaMatters):
            result = deepcopy(self)
            for name in other.names:
                other_delta_matter = other.get(name)
                result = result.mul(other_delta_matter)
            return result
        else:
            raise ValueError
        
    def truediv(self, other):
        if isinstance(other, (int, float)):
            result = deepcopy(self)
            for name in self.names:
                result.library[name] = self.get(name) / other
            return result
        elif isinstance(other, DeltaMatter):
            if other.name in self.names:
                result = deepcopy(self)
                result.library[other.name] = self.get(other.name) / other
                return result
            else:
                result = deepcopy(self)
                return result
        elif isinstance(other, DeltaMatters):
            result = deepcopy(self)
            for name in other.names:
                other_delta_matter = other.get(name)
                result = result.truediv(other_delta_matter)
            return result
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

    from piperabm.matter.delta_matter.samples import delta_matter_0, delta_matter_1, delta_matter_2
    
    delta_matters = DeltaMatters(delta_matter_0, delta_matter_1, delta_matter_2)
    delta_matters.print