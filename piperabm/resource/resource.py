from copy import deepcopy

from piperabm.tools.dictionary_custom_arithmetic import dict_add, dict_sub, dict_mul, dict_truediv, compare_keys
from piperabm.tools.storage_custom_arithmetic import add_function, sub_function


class Resource:
    """
    Represent (storage for) resources
    """
    def __init__(self, current_resource: dict={}, max_resource: dict={}):
        self.current_resource, self.max_resource = self.refine_inputs(current_resource, max_resource)

    def refine_inputs(self, current_resource: dict={}, max_resource: dict={}): #############
        shared_keys, uncommon_keys = compare_keys(main=current_resource, other=max_resource)
        if len(uncommon_keys['other']) == 0:
            if len(uncommon_keys['main']) > 0:
                for key in uncommon_keys['main']:
                    max_resource[key] = None
        else:
            raise ValueError
        #print(shared_keys, uncommon_keys)
        if len(current_resource) != len(max_resource):
            print("the length of *current_resource* must be equal to the length of *max_resource*")
            #print("length of *current_resource* is ", len(current_resource))
            #print("length of *max_resource* is ", len(max_resource))
            raise ValueError
        if len(current_resource) != 0 or len(max_resource) != 0:
            for key in current_resource:
                if max_resource[key] is not None:
                    if current_resource[key] > max_resource[key]:
                        raise ValueError
        return current_resource, max_resource

    def to_delta_resource(self):
        """
        Convert current_resource into a DeltaResource object
        """
        return DeltaResource(
            batch=deepcopy(self.current_resource)
        )

    def resource_exists(self, name: str):
        """
        Check if the resource name exists
        """
        result = False
        if name in self.current_resource:
            result = True
        return result

    def amount(self, name: str):
        """
        Amount of a certain resource
        """
        return self.current_resource[name]

    def demand(self):
        """
        Calculate demand
        """
        result, remaining = DeltaResource(self.max_resource) - DeltaResource(self.current_resource)
        return result

    def source(self):
        """
        Calculate source
        """
        return DeltaResource(self.current_resource)

    def add_new(self, name: str, current_amount: float=0, max_amount: float=None):
        """
        Add a new resource to the class
        """
        result = None
        if name not in self.current_resource:
            self.current_resource[name] = current_amount
            self.max_resource[name] = max_amount
        else:
            print("item already exists")
            raise ValueError
        return result
    
    def all_resource_names(self):
        shared_keys, uncommon_keys = compare_keys(main=self.current_resource, other=self.max_resource)
        return shared_keys, uncommon_keys

    def add_amount(self, name: str, amount: float=0):
        """
        Add amount to the already existing resource
        """
        if self.resource_exists(name) is True:
            new_current_amount, remaining = add_function(amount, self.current_resource[name], self.max_resource[name])
            self.current_resource[name] = new_current_amount
        else:
            print("resource name not defined")
            raise ValueError
        return remaining

    def sub_amount(self, name: str, amount: float=0):
        """
        Subtract amount from the already existing resource
        """
        if self.resource_exists(name) is True:
            new_current_amount, remaining = sub_function(amount, self.current_resource[name])
            self.current_resource[name] = new_current_amount
        else:
            print("resource name not defined")
            raise ValueError
        return remaining
    
    '''
    def _aggregate_keys(self, other=None):
        """
        Combine all resource names from both self and other
        """
        result = []
        for name in self.current_resource:
            if name not in result: result.append(name)
        if other is not None:
            if isinstance(other, DeltaResource):
                for name in other.batch:
                    if name not in result: result.append(name)
            elif isinstance(other, Resource):
                for name in other.current_resource:
                    if name not in result: result.append(name)
        return result
    '''

    def value(self, exchange_rate):
        return value(
            resource_dict=self.current_resource,
            exchange_rate=exchange_rate
        )

    def __add__(self, other):
        result = None
        remaining = None
        main_dict = self.current_resource
        main_max_dict = self.max_resource
        if isinstance(other, DeltaResource):
            other_dict = other.batch
            max_dict = main_max_dict
        elif isinstance(other, Resource):
            other_dict = other.current_resource
            max_dict, _ = dict_add(main_max_dict, other.max_resource)
        elif isinstance(other, dict):
            other_dict = other
            max_dict = main_max_dict
        result, remaining = dict_add(main_dict, other_dict, max_dict)
        return Resource(result, max_dict), DeltaResource(remaining)

    def __sub__(self, other):
        result = None
        remaining = None
        main_dict = self.current_resource
        if isinstance(other, DeltaResource):
            other_dict = other.batch
        elif isinstance(other, Resource):
            other_dict = other.current_resource
        elif isinstance(other, dict):
            other_dict = other
        result, remaining = dict_sub(main_dict, other_dict)
        return Resource(result, self.max_resource), DeltaResource(remaining)

    def __truediv__(self, other):
        result = None
        main_dict = self.current_resource
        if isinstance(other, (float, int)):
            other = other
        elif isinstance(other, dict):
            other = other
        elif isinstance(other, Resource):
            other = other.current_resource
        elif isinstance(other, DeltaResource):
            other = other.batch
        result = dict_truediv(main_dict, other)
        return result

    def __mul__(self, other):
        result = None
        main_dict = self.current_resource
        main_max_dict = self.max_resource
        if isinstance(other, (float, int)):
            other = other
            max_dict = main_max_dict
            result = dict_mul(main_dict, other, max_dict)
            result = Resource(result)
        elif isinstance(other, dict):
            other = other
            max_dict = main_max_dict
            result = dict_mul(main_dict, other, max_dict)
            result = DeltaResource(result)
        elif isinstance(other, Resource):
            other = other.current_resource
            max_dict = dict_mul(main_max_dict, other.max_resource)
            result = dict_mul(main_dict, other, max_dict)
            result = DeltaResource(result)
        elif isinstance(other, DeltaResource):
            other = other.batch
            max_dict = main_max_dict
            result = dict_mul(main_dict, other, max_dict)
            result = DeltaResource(result)
        return result

    def __str__(self):
        return str(self.current_resource)


class DeltaResource:
    """
    Respresent a delta between two resources
    """
    def __init__(self, batch: dict={}):
        self.batch = batch # {name: amount,} pairs

    def __call__(self, name: str):
        return self.batch[name]

    def is_empty(self):
        result = True
        for name in self.batch:
            if self.batch[name] > 0:
                result = False
                break
        return result

    def value(self, exchange_rate):
        return value(
            resource_dict=self.batch,
            exchange_rate=exchange_rate
        )

    def __add__(self, other):
        result = None
        remaining = None
        main_dict = self.batch
        if isinstance(other, DeltaResource):
            other_dict = other.batch
            max_dict = None
        elif isinstance(other, Resource):
            other_dict = other.current_resource
            max_dict = None
        elif isinstance(other, dict):
            other_dict = other
            max_dict = None
        result, remaining = dict_add(main_dict, other_dict, max_dict)
        return DeltaResource(result), DeltaResource(remaining)

    def __sub__(self, other):
        result = None
        remaining = None
        main_dict = self.batch
        if isinstance(other, DeltaResource):
            other_dict = other.batch
        elif isinstance(other, Resource):
            other_dict = other.current_resource
        elif isinstance(other, dict):
            other_dict = other
        result, remaining = dict_sub(main_dict, other_dict)
        return DeltaResource(result), DeltaResource(remaining)

    def __mul__(self, other):
        result = None
        main_dict = self.batch
        if isinstance(other, (float, int)):
            other = other
        elif isinstance(other, dict):
            other = other
        elif isinstance(other, Resource):
            other = other.current_resource
        elif isinstance(other, DeltaResource):
            other = other.batch
        result = dict_mul(main_dict, other)
        return DeltaResource(result)

    def __truediv__(self, other):
        result = None
        main_dict = self.batch
        if isinstance(other, (float, int)):
            other = other
        elif isinstance(other, dict):
            other = other
        elif isinstance(other, Resource):
            other = other.current_resource
        elif isinstance(other, DeltaResource):
            other = other.batch
        result = dict_truediv(main_dict, other)
        return DeltaResource(result)

    def __str__(self):
        return str(self.batch)


def value(resource_dict: dict, exchange_rate):
    """
    Calculate the value of each resource in unit of currency
    """
    result = {}
    for name in resource_dict:
        er = exchange_rate.rate(
            source=name,
            target='wealth'
        )
        amount = resource_dict[name]
        result[name] = er * amount
    return result


def total_value(resource_dict: dict, exchange_rate):
    """
    Calculate the total value of resources in unit of currency
    """
    value_dict = value(resource_dict, exchange_rate)
    total_value = 0
    for key in value_dict:
        total_value += value_dict[key]
    return total_value


if __name__ == "__main__":

    r1 = Resource(
        current_resource={
            'food': 5,
            'water': 2,
        },
        max_resource={
            'food': 10,
            'water': 10,
        }
    )

    dr1 = DeltaResource({
        'food': 4,
        'water': 2,
    })
    dr2 = DeltaResource({
        'food': 6,
    })
    dr, remaining = dr2-dr1
    
    #print(r1)
    #print(dr)
    r, remaining = r1-dr
    print(r)
    print(remaining)
