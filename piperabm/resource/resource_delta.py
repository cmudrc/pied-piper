from piperabm.object import Object
from piperabm.resource.matter import Matter
from piperabm.tools.symbols import SYMBOLS


class ResourceDelta(Object):
    """
    Represent a physical storage unit
    """

    def __init__(self, from_dict: dict = None):
        super().__init__()
        self.db = {} # database
        if from_dict is not None:
            self.from_dict(from_dict)

    def all_names(self) -> list:
        """
        Return all different resource names
        """
        return list(self.db.keys())

    def add_matter_object(self, name: str, matter: Matter):
        self.db[name] = matter

    def create(self, name, amount=None):
        matter = Matter(amount=amount)
        self.add_matter_object(name, matter)

    def create_zeros(self, names: list):
        for name in names:
            self.create(name, amount=0)

    def get_amount(self, name: str):
        return self.db[name].amount

    def set_amount(self, name: str, amount: float):
        self.db[name].amount = amount
        
    def is_all_zero(self):
        """
        Check if all the resource names have zero amount
        """
        results = []

        for name in self.all_names():
            amount = self.get_amount(name)
            if amount <= SYMBOLS['eps']:
                results.append(True)
            else:
                results.append(False)

        if False in results:
            return False
        else:
            return True
    
    def __call__(self, name):
        return self.get_amount(name)

    def __gt__(self, other):
        if isinstance(other, ResourceDelta):
            rd_other = other
        else:
            rd_other = other.to_resource_delta()
        results = []
        for resource_name in rd_other.db:
            if resource_name in self.db:
                self_amount = self.db[resource_name].amount                
            else:
                self_amount = 0
            other_amount = rd_other.db[resource_name].amount
            result = self_amount >= other_amount
            results.append(result)
        if False in results:
            return False
        else:
            return True
        
    def __lt__(self, other):
        if isinstance(other, ResourceDelta):
            rd_other = other
        else:
            rd_other = other.to_resource_delta()
        results = []
        for resource_name in rd_other.db:
            if resource_name in self.db:
                self_amount = self.db[resource_name].amount
            else:
                self_amount = 0
            other_amount = rd_other.db[resource_name].amount
            result = self_amount <= other_amount
            results.append(result)
        if False in results:
            return False
        else:
            return True

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
    resource_rate = ResourceDelta()
    resource_rate.create(name='food', amount=6)
    print(resource_rate)
