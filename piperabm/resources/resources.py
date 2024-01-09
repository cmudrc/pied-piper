from copy import deepcopy

from piperabm.object import PureObject
from piperabm.resources import Resource
from piperabm.economy import ExchangeRate


class Resources(PureObject):

    type = 'resources'

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, Resource):
                self.add_resource(arg)

    def add_resource(self, resource: Resource):
        """
        Add new resource to the library
        """
        if resource.name != '' and \
            resource.name not in self.names:
            self.library[resource.name] = resource
        else:
            raise ValueError

    @property
    def names(self):
        """
        Return name of all resources
        """
        return self.library.keys()

    def __call__(self, name):
        return self.library[name].amount
    
    def get(self, name):
        """
        Get the resource object based on its name
        """
        return self.library[name]

    @property
    def source(self):
        """
        Calculate source
        """
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
        """
        Calcualte ideal demand
        """
        result = Resources()
        for name in self.library:
            demand = Resource(
                name=name,
                amount=self.library[name].demand
            )
            result.add_resource(demand)
        return result
    
    def demands_actual(self, exchange_rate: ExchangeRate, balance: float):
        """
        Calculate actual demand that is limited by the *balance*
        """
        demands = self.demand
        values = demands.value(exchange_rate)
        total = values.sum
        shares = deepcopy(values)
        shares.truediv(total)
        shares.mul(balance)
        real_demands = shares.values_to_amount(exchange_rate)
        for name in self.names:
            demand = demands.get(name)
            real_demand = real_demands.get(name)
            demand.cutoff(real_demand.amount)
        return demands
    
    @property
    def max(self):
        """
        Calcualte maximum possible
        """
        result = Resources()
        for name in self.library:
            resource_max = Resource(
                name=name,
                amount=self.library[name].max
            )
            result.add_resource(resource_max)
        return result

    def value(self, exchange_rate: ExchangeRate):
        """
        Calculate monetary value of resources based on exchange rate
        """
        result = Resources()
        for name in self.names:
            resource = self.get(name)
            value = resource.value(exchange_rate)
            result.add_resource(value)
        return result

    def values_to_amount(self, exchange_rate: ExchangeRate):
        """
        Calculate equivalent amount of resources when the initial unit was money
        """
        result = Resources()
        for name in self.names:
            resource = self.get(name)
            resource_amount = resource.value_to_amount(exchange_rate)
            result.add_resource(resource_amount)
        return result
    
    def cutoff(self, amount: float):
        """
        Limit the amount
        """
        for name in self.names:
            resource = self.get(name)
            resource.cutoff(amount)
    
    def check_empty(self, names: list):
        """
        Check whether resources *names* are empty
        """
        result = []
        for name in names:
            is_empty = self.library[name].is_empty
            if is_empty is True:
                result.append(name)
        return result
    
    @property
    def sum(self):
        """
        Return total amount
        """
        result = 0
        for name in self.names:
            result += self.__call__(name)
        return result

    @property
    def biggest(self):
        """
        Return biggest resource name
        """
        biggest_name = None
        biggest_amount = None
        for name in self.names:
            if biggest_amount is None or self.__call__(name) > biggest_amount:
                biggest_name = name
                biggest_amount = self.__call__(name)
        return biggest_name

    @property
    def is_all_zero(self):
        """
        Check whether all resources are zero        
        """
        result = True
        for name in self.library:
            is_empty = self.library[name].is_empty
            if is_empty is False:
                result = False
                break
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
