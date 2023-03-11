from copy import deepcopy

try: from dictionary_custom_arithmetic import dict_add, dict_sub, dict_mul, dict_truediv, compare_keys, dict_max, dict_min
except: from .dictionary_custom_arithmetic import dict_add, dict_sub, dict_mul, dict_truediv, compare_keys, dict_max, dict_min
try: from value import resource_value, total_resource_value
except: from .value import resource_value, total_resource_value
#from piperabm.tools.storage_custom_arithmetic import add_function, sub_function


class Resource:

    def __init__(self, current_resource: dict={}, max_resource: dict={}, min_resource: dict={}):
        self.current_resource, self.max_resource, self.min_resource = \
        self.refine_inputs(
            deepcopy(current_resource),
            deepcopy(max_resource),
            deepcopy(min_resource)
        )

    def refine_inputs(self, current_resource, max_resource, min_resource):
        shared_cmax, uncommon_cmax = compare_keys(current_resource, max_resource)
        shared_cmin, uncommon_cmin = compare_keys(current_resource, min_resource)

        for key in current_resource:
            if key in uncommon_cmax['main']:
                max_resource[key] = None
            if key in uncommon_cmin['main']:
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
        Amount of a certain resource
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
        return self.current_resource.keys()
    
    def demand(self):
        result, _ = Resource(self.max_resource) - Resource(self.current_resource)
        return result

    def source(self):
        result, _ = Resource(self.current_resource) - Resource(self.min_resource)
        return result
    
    def is_zero(self):
        result = True
        for name in self.current_resource:
            if self.current_resource[name] > 0:
                result = False
                break
        return result

    def has_zero(self):
        result = False
        if len(self.current_resource) == 0: result = True
        for name in self.current_resource:
            if self.current_resource[name] <= 0:
                result = True
                break
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
        return dict_max(self.current_resource)

    def min(self):
        return dict_min(self.current_resource)

    def __str__(self):
        return str(self.current_resource)
    
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
        return result, remaining
    
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
        return result, remaining
    
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
        return result
    
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
        return result


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