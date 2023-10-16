from piperabm.object import PureObject
from piperabm.resources import Resource


class Resources(PureObject):

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, Resource):
                self.add_resource(arg)

    def add_resource(self, resource: Resource):
        self.library[resource.name] = resource

    def __call__(self, name):
        return self.library[name].amount

    @property
    def source(self):
        result = Resources()
        for name in self.library:
            source = Resource(
                name=name,
                amount=self.library[name].source
            )
            result.add_resource(source)
        return result
    
    @property
    def demand(self):
        result = Resources()
        for name in self.library:
            demand = Resource(
                name=name,
                amount=self.library[name].demand
            )
            result.add_resource(demand)
        return result

    def add(self, other):
        if isinstance(other, Resources):
            remainders = Resources()
            for name in self.library:
                remainder = self.library[name].add(other.library[name])
                remainders.add_resource(remainder)
            return remainders
        elif isinstance(other, Resource):
            if other.name in self.library:
                remainder = self.library[name].add(other)
                return remainder
        else:
            raise ValueError

    def sub(self, other):
        if isinstance(other, Resources):
            remainders = Resources()
            for name in self.library:
                remainder = self.library[name].sub(other.library[name])
                remainders.add_resource(remainder)
            return remainders
        elif isinstance(other, Resource):
            if other.name in self.library:
                remainder = self.library[name].sub(other)
                return remainder
        else:
            raise ValueError

    def mul(self, other):
        if isinstance(other, (float, int)):
            remainders = Resources()
            for name in self.library:
                remainder = self.library[name].mul(other)
                remainders.add_resource(remainder)
            return remainders
        else:
            raise ValueError

    def truediv(self, other):
        if isinstance(other, (float, int)):
            remainders = Resources()
            for name in self.library:
                remainder = self.library[name].truediv(other)
                remainders.add_resource(remainder)
            return remainders
        else:
            raise ValueError

    def serialize(self):
        dictionary = {}
        for name in self.library:
            dictionary[name] = self.library[name].serialize()     
        return dictionary  
    
    def deserialize(self, dictionary: dict) -> None:
        for name in dictionary:
            resource = Resource()
            resource.deserialize(dictionary[name])
            self.add_resource(resource)


if __name__ == "__main__":
    from piperabm.resources.samples import resources_0 as resources

    resources.print
