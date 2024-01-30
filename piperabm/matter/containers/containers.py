from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter import Matter, Matters, Container
from piperabm.economy import ExchangeRate


class Containers(PureObject):
    """
    A container to contain Matter objects
    """

    type = 'containers'

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, (Container, Matter)):
                self.add(arg)

    def add(self, item: (Container, Matter)):
        """
        Add new resource to the library
        """
        name = item.name
        if name != '' and name is not None:
            if isinstance(item, Container):
                self.library[name] = item
            elif isinstance(item, Matter):
                container = Container(item)
                self.add(container)
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
        return self.library[name].matter.amount

    def value(self, exchange_rate: ExchangeRate, total=True):
        """
        Calculate monetary value based on exchange rate
        """
        values = {}
        for name in self.names:
            container = self.get(name)
            values[name] = container.value(exchange_rate)
        if total is True:
            result = 0
            for name in values:
                result += values[name]
        else:
            result = values
        return result
    
    def check_empty(self, names: list='all'):
        """
        Check whether *names* are empty
        """
        result = []
        if names == 'all':
            names = self.names
        for name in names:
            if name in self.names:
                container = self.get(name)
                is_empty = container.is_empty
                if is_empty is True:
                    result.append(name)
            else:
                result.append(name)
        return result
    
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
            item = Container()
            item.deserialize(item_serialized)
            self.add(item)

    def to_matters(self):
        """
        Convert Matter object to DeltaMatter object
        """
        matters = Matters()
        for name in self.names:
            container = self.get(name)
            matter = deepcopy(container.matter)
            matters.add(matter)
        return matters

    def __add__(self, other):
        if isinstance(other, dict):
            """ Matters = Containers + dict """
            other_matters = Matters()
            other_matters.from_amounts(other)
            return self.__add__(other_matters)
        elif isinstance(other, Matter):
            """ Matter = Containers + Matter """
            if other.name in self.names:
                matter = self.get(other.name)
                remainder = matter.__add__(other)
                return remainder
        elif isinstance(other, Matters):
            """ Matters = Containers + Matters """
            remainders = Matters()
            for name in other.names:
                other_matter = other.get(name)
                remainder = self.__add__(other_matter)
                remainders.add(remainder)
            return remainders
        elif isinstance(other, Container):
            """ Containers = Containers + Container """
            new_containers = deepcopy(self)
            name = other.name
            if name in self.names:
                container = self.get(name)
                new_container = container + other
                new_containers.library[name] = new_container
            return new_containers
        elif isinstance(other, Containers):
            """ Containers = Containers + Containers """
            new_containers = deepcopy(self)
            for name in other.names:
                if name in self.names:
                    new_container = self.get(name) + other.get(name)
                else:
                    new_container = deepcopy(other.get(name))
                new_containers.library[name] = new_container
            return new_containers
        else:
            raise ValueError
       
    def __sub__(self, other):
        if isinstance(other, dict):
            """ Matters = Containers - dict """
            other_matters = Matters()
            other_matters.from_amounts(other)
            return self.__sub__(other_matters)
        elif isinstance(other, Matter):
            """ Matter = Containers - Matter """
            if other.name in self.names:
                matter = self.get(other.name)
                remainder = matter.__sub__(other)
                return remainder
        elif isinstance(other, Matters):
            """ Matters = Containers - Matters """
            remainders = Matters()
            for name in other.names:
                other_matter = other.get(name)
                remainder = self.__sub__(other_matter)
                remainders.add(remainder)
            return remainders
        elif isinstance(other, Container):
            """ Containers = Containers - Container """
            new_containers = deepcopy(self)
            name = other.name
            if name in self.names:
                container = self.get(name)
                new_container = container - other
                new_containers.library[name] = new_container
            return new_containers
        elif isinstance(other, Containers):
            """ Containers = Containers - Containers """
            new_containers = deepcopy(self)
            for name in other.names:
                if name in self.names:
                    new_container = self.get(name) - other.get(name)
                    new_containers.library[name] = new_container
                else:
                    pass
            return new_containers
        else:
            raise ValueError
     
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            """ Containers = Containers * (int, float) """
            new_containers = Containers()
            for name in self.names:
                container = self.get(name)
                new_container = container * other
                new_containers.add(new_container)
            return new_containers
        elif isinstance(other, dict):
            """ Containers = Containers * dict """
            new_containers = deepcopy(self)
            for name in other:
                if name in self.names:
                    container = self.get(name)
                    new_container = container * other[name]
                    new_containers.add(new_container)
            return new_containers
        else:
            raise ValueError
      
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            """ Containers = Containers / (int, float) """
            new_containers = self.__mul__(1 / other)
            return new_containers
        elif isinstance(other, dict):
            """ Containers = Containers / dict """
            new_containers = deepcopy(self)
            for name in other:
                if name in self.names:
                    container = self.get(name)
                    new_container = container / other[name]
                    new_containers.add(new_container)
            return new_containers
        elif isinstance(other, Matter):
            """ dict = Containers / Matter """
            ratio = 0
            if other.name in self.names:
                ratio = self.__call__(other.name) / other.amount
            return ratio
        elif isinstance(other, Matters):
            """ dict = Containers / Matters """
            ratios = {}
            for name in other.names:
                if name in self.names:
                    ratio = self.__call__(name) / other.__call__(name)
                    ratios[name] = ratio
                else:
                    ratios[name] = 0
            return ratios
        elif isinstance(other, Container):
            """ dict = Containers / Container """
            ratio = self.__truediv__(other.matter)
            return ratio
        elif isinstance(other, Containers):
            """ dict = Containers / Containers """
            other_matters = other.to_matters()
            ratios = self.__truediv__(other_matters)
            return ratios
        else:
            raise ValueError


if __name__ == '__main__':

    from piperabm.matter.container.samples import container_0 as food
    from piperabm.matter.container.samples import container_1 as water
    from piperabm.matter.container.samples import container_2 as energy
    
    containers = Containers(food, water, energy)
    containers.print