from copy import deepcopy

from piperabm.object import Object
from piperabm.resource.matter import Matter
from piperabm.resource.container import Container
from piperabm.resource.resource_rate import ResourceRate


class Resource(Object):
    """
    Represent resources located within physical storage unit (container)
    """

    def __init__(self):
        super().__init__()
        self.db = {} # database

    def add_container_object(self, name: str, container: Container):
        """
        Directly define a new resource by adding container object
        """
        self.db[name] = container

    def create(self, name, amount=None, max=None, min=None):
        """
        Define new resource
        """
        matter = Matter(amount=amount)
        container = Container(max=max, min=min)
        container.add_matter_object(matter)
        self.add_container_object(name, container)
    
    def __call__(self, name):
        return self.db[name].matter
    
    def __add__(self, other):
        remainder = {}
        if isinstance(other, ResourceRate): # resource arithmetic
            for key in other.db:
                if key in self.db:
                    remainder[key] = self.db[key] + other.db[key]
            return remainder
        else: # delta arithmetic
            super().__add__(other)

    def __sub__(self, other):
        remainder = {}
        if isinstance(other, ResourceRate): # resource arithmetic
            for key in other.db:
                if key in self.db:
                    remainder[key] = self.db[key] - other.db[key]
            return remainder
        else: # delta arithmetic
            super().__add__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            remainder = {}
            for key in self.db:
                resource = self.db[key]
                remainder[key] = resource * other
            return remainder
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            remainder = {}
            for key in self.db:
                resource = self.db[key]
                remainder[key] = resource / other
            return remainder

    def to_dict(self) -> dict:
        dictionary = {}
        for key in self.db:            
            dictionary[key] = self.db[key].to_dict()
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        for key in dictionary:
            container = Container()
            container.from_dict(dictionary[key])
            self.db[key] = container
    

if __name__ == "__main__":
    resource = Resource()
    resource.create(
        name='food',
        amount=6,
        max=10,
    )
    print(resource('food'))

    resource_rate = ResourceRate()
    resource_rate.create(name='food', amount=6)
    resource - resource_rate
    print(resource)
