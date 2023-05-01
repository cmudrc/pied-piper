from copy import deepcopy

from piperabm.object import Object
from piperabm.resource.dictionary_custom_arithmetic import dict_add, dict_sub, dict_mul, dict_truediv, dict_max, dict_min
from piperabm.resource.value import resource_value, total_resource_value


class Resource(Object):

    def __init__(
            self,
            current_resource={},
            max_resource: dict={},
            min_resource: dict={}
        ):
        super().__init__()
        self.current_resource, self.max_resource, self.min_resource = \
        self.refine_inputs(
            deepcopy(current_resource),
            deepcopy(max_resource),
            deepcopy(min_resource)
        )

    def refine_inputs(self, current_resource, max_resource, min_resource):
        """
        Refine input values
        """
        if isinstance(current_resource, list):
            resource_names = deepcopy(current_resource)
            current_resource = {}
            for key in resource_names:
                current_resource[key] = 0
        elif isinstance(current_resource, dict):
            resource_names = current_resource.keys()
        for key in resource_names:
            if key not in max_resource:
                max_resource[key] = None
            if key not in min_resource:
                min_resource[key] = 0
        return current_resource, max_resource, min_resource
    
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
        Amount of a certain resource based on its *name*
        """
        return self.current_resource[name]
    
    def amount_name(self, amount: float):
        """
        Name of the resource having the exact *amount*
        """
        for resource_name, resource_amount in self.current_resource.items():
            if resource_amount == amount:
                result = resource_name
                break
        return result
    
    def all_resource_names(self):
        """
        Return all different resource names
        """
        return self.current_resource.keys()
    
    def demand(self):
        """
        Calculate demand
        """
        result, _ = Resource(self.max_resource) - Resource(self.current_resource)
        return result

    def source(self):
        """
        Calculate source
        """
        result, _ = Resource(self.current_resource) - Resource(self.min_resource)
        return result
    
    def create_zeros(self, resource_names: list):
        """
        Create an empty resource instance with *resource_names*
        """
        for resource_name in resource_names:
            if resource_name not in self.current_resource:
                self.current_resource[resource_name] = 0
            if resource_name not in self.max_resource:
                self.max_resource[resource_name] = None
            if resource_name not in self.min_resource:
                self.min_resource[resource_name] = 0

    def is_zero(self, resource_names: list = []) -> bool:
        """
        Check if the *resource_names* are zero
        """
        if len(resource_names) == 0: # check all
            check_list = self.current_resource
        else:
            check_list = resource_names
        result = True
        for name in check_list:
            if name in self.current_resource and self.current_resource[name] > 0:
                result = False
                break
        return result

    def has_zero(self, resource_names: list = []) -> bool:
        """
        Check if any of resources in *resource_name* has zero value
        """
        result = False
        if len(resource_names) == 0: # check all
            names_list = self.all_resource_names()
        else:
            names_list = resource_names
        zero_resource_names = self.find_zeros()
        for name in names_list:
            if name in zero_resource_names:
                result = True
                break
        return result
    
    def find_zeros(self, resource_names: list = []) -> list:
        """
        Find resources that have zero amount left
        """
        result = []
        if len(resource_names) == 0: # check all
            names_list = self.all_resource_names()
        else:
            names_list = resource_names
        for resource_name in names_list:
            if self.current_resource[resource_name] == 0:
                result.append(resource_name)
        return result

    def val(self, property='current'):
        result = None
        if property == 'current':
            result = Resource(deepcopy(self.current_resource))
        elif property == 'max':
            result = Resource(deepcopy(self.max_resource))
        elif property == 'min':
            result = Resource(deepcopy(self.min_resource))
        return result

    def value(self, exchange_rate, property='current'):
        resource = self.val(property)
        return resource_value(resource, exchange_rate)
    
    def total_value(self, exchange_rate, property='current'):
        resource_value_dict = self.value(exchange_rate, property)
        return total_resource_value(resource_value_dict)
    
    def amount(self, name: str):
        """
        Amount of a certain resource
        """
        return self.current_resource[name]
    
    def max(self):
        """
        Max amount of all resources
        """
        return dict_max(self.current_resource)

    def min(self):
        """
        Min amount of all resources
        """
        return dict_min(self.current_resource)

    def to_dict(self) -> dict:
        return {
            'current': self.current_resource,
            'max': self.max_resource,
            'min': self.min_resource,
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.current_resource = dictionary['current']
        self.max_resource = dictionary['max']
        self.min_resource = dictionary['min']
    
    def __call__(self, name: str):
        return self.amount(name)

    def __eq__(self, other):
        result = True
        if self.current_resource != other.current_resource: result = False
        return result

    def __add__(self, other):
        result, remaining = None, None
        if isinstance(other, Resource):
            result_dict, remaining_dict = dict_add(
                main=self.current_resource,
                other=other.current_resource,
                max=self.max_resource
            )
            result = Resource(result_dict, self.max_resource, self.min_resource)
            remaining = Resource(remaining_dict, other.max_resource, other.min_resource)
            return deepcopy(result), deepcopy(remaining)
        elif isinstance(other, dict): # delta
            super().__add__(other)
    
    def __sub__(self, other):
        result, remaining = None, None
        if isinstance(other, Resource):
            result_dict, remaining_dict = dict_sub(
                main=self.current_resource,
                other=other.current_resource,
                min=self.min_resource
            )
            result = Resource(result_dict, self.max_resource, self.min_resource)
            remaining = Resource(remaining_dict, other.max_resource, other.min_resource)
            return deepcopy(result), deepcopy(remaining)
        elif isinstance(other, dict): # delta
            super().__sub__(other)
            #delta = super().__sub__(other)
            #return delta
    
    def __mul__(self, other):
        result = None
        if isinstance(other, (int, float)):
            result_dict = dict_mul(
                main=self.current_resource,
                other=other,
                max=self.max_resource
            )
            result = Resource(result_dict, self.max_resource, self.min_resource)
        elif isinstance(other, Resource):
            result_dict = dict_mul(
                main=self.current_resource,
                other=other.current_resource,
                max=self.max_resource
            )
            result = Resource(result_dict, self.max_resource, self.min_resource)
        return deepcopy(result)
    
    def __truediv__(self, other):
        result = None
        if isinstance(other, (int, float)):
            result_dict = dict_truediv(
                main=self.current_resource,
                other=other,
                max=self.max_resource
            )
            result = Resource(result_dict, self.max_resource, self.min_resource)
        elif isinstance(other, Resource):
            result_dict = dict_truediv(
                main=self.current_resource,
                other=other.current_resource,
                max=self.max_resource
            )
            result = Resource(result_dict, self.max_resource, self.min_resource)
        return deepcopy(result)


if __name__ == "__main__":
    r0 = Resource({'food': 5}, max_resource={'food': 7}, min_resource={'food': 2})
    dr = Resource({'food': 4})
    #print(r0, dr)
    #r0, dr = r0 - dr
    #print(r0, dr)
    #print(r0 * 2)
    #print(r0('food'))
    '''
    r1 = Resource(
        current_resource={
            'food': 5,
            'water': 2,
        },
        max_resource={
            'food': 10,
            'water': 10,
        },
        #min_resource=
    )
    
    r2 = Resource(
        current_resource={
            'food': 6,
            'energy': 7
        }
    )
    '''
    #print(r1, r2)
    #r1, r2 = r1 - r2
    #print(r1, r2)
    #print(r1.max_resource)
    #print(Resource(r1.max_resource) - Resource(r1.current_resource))
    #print(r1.demand())