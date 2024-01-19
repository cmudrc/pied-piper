from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter.matter import Matter
from piperabm.economy import ExchangeRate


class Matters(PureObject):
    """
    A container to contain DeltaMatter objects
    """

    type = 'matters'

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, Matter):
                self.add(arg)
            elif isinstance(arg, list):
                self.zeros(names=arg)

    def add(self, matter: Matter):
        """
        Add new delta_resource to the library
        """
        name = matter.name
        if name != '' and name is not None:
            self.library[name] = matter
        else:
            raise ValueError
        
    def zeros(self, names: list):
        """
        Load library of empty matter with corresponding names
        """
        for name in names:
            matter = Matter(name)
            self.add(matter)

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
    
    def from_values(self, values: dict, exchange_rate: ExchangeRate):
        """
        Calculate the amount of each delta_matter based on value and exchange rate
        """
        names = list(values)
        for name in names:
            matter = Matter(name)
            matter.from_value(values[name], exchange_rate)
            self.add(matter)

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
            matter = Matter(name, amount)
            self.add(matter)

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
            """ Matters = Matters + dict """
            other_matters = Matters()
            other_matters.from_amounts(other)
            new_matters = self.__add__(other_matters)
            return new_matters
        elif isinstance(other, Matter):
            """ Matters = Matters + Matter """
            if other.name in self.names:
                result = deepcopy(self)
                result.library[other.name] = self.get(other.name) + other
                return result
            else:
                result = deepcopy(self)
                result.library[other.name] = other
                return result
        elif isinstance(other, Matters):
            """ Matters = Matters + Matters """
            result = deepcopy(self)
            for name in other.names:
                other_matter = other.get(name)
                result = result.__add__(other_matter)
            return result
        else:
            raise ValueError
    
    def __sub__(self, other):
        if isinstance(other, dict):
            """ Matters = Matters - dict """
            other_matters = Matters()
            other_matters.from_amounts(other)
            return self.__sub__(other_matters)
        elif isinstance(other, Matter):
            """ Matters = Matters - Matter """
            if other.name in self.names:
                result = deepcopy(self)
                result.library[other.name] = self.get(other.name) - other
                return result
            else:
                result = deepcopy(self)
                result.library[other.name] = other
                return result
        elif isinstance(other, Matters):
            """ Matters = Matters - Matters """
            result = deepcopy(self)
            for name in other.names:
                other_matter = other.get(name)
                result = result.__sub__(other_matter)
            return result
        else:
            raise ValueError
      
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            """ Matters = Matters * (int, flaot) """
            result = Matters()
            for name in self.names:
                new_amount = self.__call__(name) * other
                matter = Matter(name, new_amount)
                result.add(matter)
            return result
        elif isinstance(other, dict):
            """ Matters = Matters * dict """
            result = Matters()
            for name in other:
                new_amount = self.__call__(name) * other[name]
                matter = Matter(name, new_amount)
                result.add(matter)
            return result
        elif isinstance(other, Matter):
            """ Matters = Matters * Matter """
            result = deepcopy(self)
            if other.name in self.names:
                result.library[other.name] = self.get(other.name) * other
            return result
        elif isinstance(other, Matters):
            """ Matters = Matters * Matters """
            result = deepcopy(self)
            for name in other.names:
                other_delta_matter = other.get(name)
                result = result.__mul__(other_delta_matter)
            return result
        else:
            raise ValueError
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            """ Matters = Matters / (int, flaot) """
            result = Matters()
            for name in self.names:
                new_amount = self.__call__(name) / other
                matter = Matter(name, new_amount)
                result.add(matter)
            return result
        elif isinstance(other, dict):
            """ Matters = Matters / dict """
            result = Matters()
            for name in other:
                new_amount = self.__call__(name) / other[name]
                matter = Matter(name, new_amount)
                result.add(matter)
            return result
        elif isinstance(other, Matter):
            """ (int, float) = Matters / Matter """
            if other.name in self.names:
                return self.get(other.name).amount / other.amount
            else:
                return 0
        elif isinstance(other, Matters):
            """ dict = Matters / Matters """
            result = {}
            for name in other.names:
                other_matter = other.get(name)
                result[name] = self.__truediv__(other_matter)
            return result
        else:
            raise ValueError
        

if __name__ == '__main__':

    from piperabm.matter.matter.samples import matter_0 as food
    from piperabm.matter.matter.samples import matter_1 as water
    from piperabm.matter.matter.samples import matter_2 as energy
    
    matters = Matters(food, water, energy)
    matters.print