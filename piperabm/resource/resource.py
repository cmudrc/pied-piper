from piperabm.object import Object
from piperabm.resource.matter import Matter
from piperabm.resource.container import Container
from piperabm.resource.resource_delta import ResourceDelta
from piperabm.tools.symbols import SYMBOLS


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

    def get_amount(self, name: str):
        return self.db[name].matter.amount

    def set_amount(self, name: str, amount: float):
        self.db[name].matter.amount = amount

    def all_names(self) -> list:
        """
        Return all different resource names
        """
        return list(self.db.keys())

    def find_zeros(self, resource_names: list = []) -> list:
        """
        Find resources that have zero amount left
        """
        result = []
        if len(resource_names) == 0: # check all
            names_list = self.all_names()
        else:
            names_list = resource_names
        for resource_name in names_list:
            if self.__call__(resource_name) <= SYMBOLS['eps']:
                result.append(resource_name)
        return result
    
    def to_resource_delta(self) -> ResourceDelta:
        """
        Create an equivalent ResourceDelta object from current Resource object
        Required for resource_sum module
        """
        resource_delta = ResourceDelta()
        dictionary = self.to_dict()
        new_dictionary = {}
        for name in dictionary:
            new_dictionary[name] = dictionary[name]['amount']
        resource_delta.from_dict(new_dictionary)
        return resource_delta
    
    def create_zeros(self, names: list):
        for name in names:
            self.create(name, amount=0)

    def __call__(self, name: str):
        return self.get_amount(name)
    
    def __gt__(self, other):
        rd_self = self.to_resource_delta()
        if isinstance(other, Resource):
            rd_other = other.to_resource_delta()
        elif isinstance(other, ResourceDelta):
            rd_other = other
        return rd_self > rd_other
    
    def __lt__(self, other):
        rd_self = self.to_resource_delta()
        if isinstance(other, Resource):
            rd_other = other.to_resource_delta()
        elif isinstance(other, ResourceDelta):
            rd_other = other
        return rd_self < rd_other
    
    def __add__(self, other):
        if isinstance(other, ResourceDelta): # resource arithmetic
            remainder = {}
            for key in other.db:
                if key in self.db:
                    remainder[key] = self.db[key] + other.db[key]
            return ResourceDelta(remainder)
        else: # delta arithmetic
            super().__add__(other)

    def __sub__(self, other):
        if isinstance(other, ResourceDelta): # resource arithmetic
            remainder = {}
            for key in other.db:
                if key in self.db:
                    remainder[key] = self.db[key] - other.db[key]
            return ResourceDelta(remainder)
        else: # delta arithmetic
            return super().__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            remainder = {}
            for key in self.db:
                resource = self.db[key]
                remainder[key] = resource * other
            return ResourceDelta(remainder)
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)): # resource arithmetic
            remainder = {}
            for key in self.db:
                resource = self.db[key]
                remainder[key] = resource / other
            return ResourceDelta(remainder)

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
    resource.create(name='food', amount=6, max=10, min=1)
    print(resource)
