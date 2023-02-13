from copy import deepcopy

try: from .add import add_function
except: from add import add_function
try: from .sub import sub_function
except: from sub import sub_function
try: from .exchange import Exchange
except: from exchange import Exchange


class Resource:
    """
    Represent (storage for) resources
    """
    def __init__(self, current_resource: dict={}, max_resource: dict={}):
        if len(current_resource) != len(max_resource):
            print("the length of *current_resource* must be equal to the length of *max_resource*")
            #print("length of *current_resource* is ", len(current_resource))
            #print("length of *max_resource* is ", len(max_resource))
            raise ValueError
        if len(current_resource) != 0 or len(max_resource) != 0:
            for key in current_resource:
                if current_resource[key] > max_resource[key]:
                    raise ValueError
        self.current_resource = current_resource # {name: amount,}
        self.max_resource = max_resource # {name: amount,}

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
        result = {}
        for name in self._aggregate_keys():
            if self.max_resource[name] is None:
                pass
            else:
                result[name] = self.max_resource[name] - self.current_resource[name]
        return DeltaResource(batch=result)

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
        return result

    def value(self, exchange_rate: Exchange):
        return value(
            resource_dict=self.current_resource,
            exchange_rate=exchange_rate
        )

    def __add__(self, other):
        if isinstance(other, DeltaResource):
            new_current_amount_dict = {}
            new_max_amount_dict = deepcopy(self.max_resource)
            new_remaining_dict = {}
            for name in self._aggregate_keys(other):
                if self.resource_exists(name) is True:
                    if name in other.batch:
                        amount = other.batch[name]
                        if amount > 0:
                            new_current_amount, remaining = add_function(
                                amount=other.batch[name],
                                current_amount=self.current_resource[name],
                                max_amount=self.max_resource[name]
                            )
                        else:
                            new_current_amount, remaining = sub_function(
                                amount=-amount,
                                current_amount=self.current_resource[name]
                            )
                    else:
                        new_current_amount, remaining = add_function(
                            amount=0,
                            current_amount=self.current_resource[name],
                            max_amount=self.max_resource[name]
                        )
                else:
                    amount = other.batch[name]
                    if amount > 0:
                        new_current_amount, remaining = add_function(
                            amount=amount,
                            current_amount=0,
                            max_amount=None
                        )
                    else:
                        new_current_amount, remaining = sub_function(
                            amount=-amount,
                            current_amount=0
                        )
                new_remaining_dict[name] = remaining
                new_current_amount_dict[name] = new_current_amount
            result = Resource(
                current_resource=new_current_amount_dict,
                max_resource=new_max_amount_dict
                )
            result_remaining = DeltaResource(new_remaining_dict)
        else:
            txt = "ERROR: " + str(type(other)) + " type not acceptible."
            print(txt)
            raise ValueError
        return result, result_remaining

    def __sub__(self, other):
        if isinstance(other, DeltaResource):
            new_current_amount_dict = {}
            new_max_amount_dict = deepcopy(self.max_resource)
            new_remaining_dict = {}
            for name in self._aggregate_keys(other):
                if self.resource_exists(name) is True:
                    if name in other.batch:
                        amount = other.batch[name]
                        if amount > 0:
                            new_current_amount, remaining = sub_function(
                                amount=amount,
                                current_amount=self.current_resource[name]
                            )
                        else:
                            new_current_amount, remaining = add_function(
                                amount=-amount,
                                current_amount=self.current_resource[name],
                                max_amount=self.max_resource[name]
                            )
                    else:
                        new_current_amount, remaining = sub_function(
                            amount=0,
                            current_amount=self.current_resource[name]
                        )
                else:
                    amount = other.batch[name]
                    if amount > 0:
                        new_current_amount, remaining = sub_function(
                            amount=amount,
                            current_amount=0
                        )
                    else:
                        new_current_amount, remaining = add_function(
                            amount=-amount,
                            current_amount=0,
                            max_amount=None
                        )                      
                new_remaining_dict[name] = remaining
                new_current_amount_dict[name] = new_current_amount
            result = Resource(
                current_resource=new_current_amount_dict,
                max_resource=new_max_amount_dict
                )
            result_remaining = DeltaResource(new_remaining_dict)
        else:
            raise ValueError
        return result, result_remaining

    def __truediv__(self, other):
        result = {}
        if isinstance(other, DeltaResource):
            for name in other.batch:
                if name in self._aggregate_keys():
                    result[name] = self.current_resource[name] / other.batch[name]
        elif isinstance(other, Resource):
            for name in other.current_amount:
                if name in self._aggregate_keys():
                    result[name] = self.current_resource[name] / other.current_resource[name]
        elif isinstance(other, (float, int)):
            for name in self._aggregate_keys():
                result[name] = self.current_resource[name] / other
        elif isinstance(other, dict):
            for name in self._aggregate_keys():
                if name in other:
                    result[name] = self.current_resource[name] / other[name]
        return result

    def __mul__(self, other):
        result = {}
        if isinstance(other, (float, int)):
            for name in self._aggregate_keys():
                result[name] = self.current_resource[name] * other
        elif isinstance(other, dict):
            for name in self._aggregate_keys():
                if name in other:
                    result[name] = self.current_resource[name] * other[name]
        return result

    def __str__(self):
        return str(self.current_resource)


class DeltaResource:
    """
    Respresent a delta between two resources
    """
    def __init__(self, batch: dict={}):
        self.batch = batch # {name: amount,} pairs

    def is_empty(self):
        result = True
        for name in self.batch:
            if self.batch[name] > 0:
                result = False
                break
        return result

    def value(self, exchange_rate: Exchange):
        return value(
            resource_dict=self.batch,
            exchange_rate=exchange_rate
        )

    def __add__(self, other):
        result = None
        if isinstance(other, DeltaResource):
            result_dict = {}
            for key in self.batch:
                if key in other.batch:
                    result_dict[key] = self.batch[key] + other.batch[key]
                else:
                    result_dict[key] = self.batch[key]
            for key in other.batch:
                if key not in self.batch:
                    result_dict[key] = other.batch[key]
            result = DeltaResource(result_dict)
        elif isinstance(other, Resource):
            new_current_amount_dict = {}
            new_max_amount_dict = other.max_resource
            new_remaining_dict = {}
            for name in self.batch:
                if other.resource_exists(name) is True:
                    new_current_amount, remaining = add_function(
                        amount=self.batch[name],
                        current_amount=other.current_resource[name],
                        max_amount=other.max_resource[name]
                        )
                    new_remaining_dict[name] = remaining
                    new_current_amount_dict[name] = new_current_amount
            result = Resource(
                current_resource=new_current_amount_dict,
                max_resource=new_max_amount_dict
                )
            self.batch = new_remaining_dict
        return result

    def __sub__(self, other):
        if isinstance(other, DeltaResource):
            result_dict = {}
            for key in self.batch:
                if key in other.batch:
                    result_dict[key] = self.batch[key] - other.batch[key]
                else:
                    result_dict[key] = self.batch[key]
            for key in other.batch:
                if key not in self.batch:
                    result_dict[key] = -other.batch[key]
            result = DeltaResource(result_dict)
        elif isinstance(other, Resource):
            new_current_amount_dict = {}
            new_max_amount_dict = other.max_resource
            new_remaining_dict = {}
            for name in self.batch:
                if other.resource_exists(name) is True:
                    new_current_amount, remaining = add_function(
                        amount=self.batch[name],
                        current_amount=-other.current_resource[name],
                        max_amount=other.max_resource[name]
                        )
                    new_remaining_dict[name] = remaining
                    new_current_amount_dict[name] = new_current_amount
            result = Resource(
                current_resource=new_current_amount_dict,
                max_resource=new_max_amount_dict
                )
            self.batch = new_remaining_dict
        return result

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            new_batch = deepcopy(self.batch)
            for name in new_batch:
                new_batch[name] = new_batch[name] * other
            result = DeltaResource(new_batch)
        return result

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            new_batch = deepcopy(self.batch)
            for name in new_batch:
                new_batch[name] = new_batch[name] / other
            result = DeltaResource(new_batch)
        return result

    def __str__(self):
        return str(self.batch)


def value(resource_dict: dict, exchange_rate: Exchange):
    """
    Calculate the value of resources in unit of currency
    """
    result = {}
    for name in resource_dict:
        er = exchange_rate.rate(
            source=name,
            target='wealth'
        )
        amount = resource_dict[name]
        result[name] = er * amount
    return DeltaResource(result)


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
        #'food': 4,
        'water': 2,
    })
    dr2 = DeltaResource({
        'food': 6,
    })
    dr = dr2-dr1
    
    print(r1)
    print(dr)
    r, remaining = r1-dr
    print(r)
    print(remaining)
