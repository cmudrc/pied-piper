from copy import deepcopy

from piperabm.object import Object
from piperabm.resource.matter import Matter


class ResourceRate(Object):
    """
    Represent a physical storage unit
    """

    def __init__(self):
        super().__init__()
        self.db = {} # database

    def add_matter_object(self, name: str, matter: Matter):
        self.db[name] = matter

    def create(self, name, amount=None):
        matter = Matter(amount=amount)
        self.add_matter_object(name, matter)
    
    def __call__(self, name):
        return self.db[name]

    def __mul__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            for key in self.db:
                matter = self.db[key]
                matter * other
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            for key in self.db:
                matter = self.db[key]
                matter / other

    def to_dict(self) -> dict:
        dictionary = {}
        for key in self.db:            
            dictionary[key] = self.db[key].to_dict()
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        for key in dictionary:
            matter = Matter()
            matter.from_dict(dictionary[key])
            self.db[key] = matter
    

if __name__ == "__main__":
    resource_rate = ResourceRate()
    resource_rate.create(name='food', amount=6)
    resource_rate * 2
    print(resource_rate)
    #print(resource_rate('food'))
