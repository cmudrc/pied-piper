from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter.delta_matter import DeltaMatter
from piperabm.economy import ExchangeRate


class DeltaMatters(PureObject):
    """
    A container to contain DeltaMatter objects
    """

    type = 'delta matters'

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, DeltaMatter):
                self.add(arg)

    def add(self, delta_matter: DeltaMatter):
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
            self.add(delta_matter)

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
    
    def from_values(self, values: dict, exchange_rate: ExchangeRate):
        """
        Calculate the amount of each delta_matter based on value and exchange rate
        """
        names = list(values)
        for name in names:
            delta_matter = DeltaMatter(name)
            delta_matter.from_value(values[name], exchange_rate)
            self.add(delta_matter)

    def amounts(self):
        """
        Convert to dictionary
        """
        result = {}
        for name in self.names:
            result[name] = self.__call__(name)
        return result

    def from_amounts(self, amounts: dict):
        """
        Load from dictionary
        """
        for name in amounts:
            amount = amounts[name]
            delta_matter = DeltaMatter(name, amount)
            self.add(delta_matter)

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
            self.add(item)

    def __add__(self, other):

        if isinstance(other, dict):
            other_delta_matters = DeltaMatters()
            other_delta_matters.from_amounts(other)
            return self.__add__(other_delta_matters)
        
        elif isinstance(other, DeltaMatter):
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
                result = result.__add__(other_delta_matter)
            return result
        
        else:
            raise ValueError
        
    def __sub__(self, other):

        if isinstance(other, dict):
            other_delta_matters = DeltaMatters()
            other_delta_matters.from_amounts(other)
            return self.__sub__(other_delta_matters)
        
        elif isinstance(other, DeltaMatter):
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
                result = result.__sub__(other_delta_matter)
            return result
        
        else:
            raise ValueError
        
    def __mul__(self, other):

        if isinstance(other, (int, float)):
            result = deepcopy(self)
            for name in self.names:
                result.library[name] = self.get(name) * other
            return result
        
        elif isinstance(other, dict):
            other_delta_matters = DeltaMatters()
            other_delta_matters.from_amounts(other)
            return self.__mul__(other_delta_matters)
        
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
                result = result.__mul__(other_delta_matter)
            return result
        
        else:
            raise ValueError
        
    def __truediv__(self, other):

        if isinstance(other, (int, float)):
            result = deepcopy(self)
            for name in self.names:
                result.library[name] = self.get(name) / other
            return result
        
        elif isinstance(other, dict):
            other_delta_matters = DeltaMatters()
            other_delta_matters.from_amounts(other)
            return self.__truediv__(other_delta_matters)
        
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
                result = result.__truediv__(other_delta_matter)
            return result
        
        else:
            raise ValueError
        

if __name__ == '__main__':

    from piperabm.matter.delta_matter.samples import delta_matter_0, delta_matter_1, delta_matter_2
    
    delta_matters = DeltaMatters(delta_matter_0, delta_matter_1, delta_matter_2)
    delta_matters.print