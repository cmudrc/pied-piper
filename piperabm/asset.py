from copy import deepcopy


class Asset:

    def __init__(
        self,
        resources=[],
    ):
        self.resources = resources

    def find(self, name:str):
        """
        Find a resource based on its name
        """
        result = None
        for resource in self.resources:
            if resource.name == name:
                result = resource
                break
        return result

    def add_resource(self, resource):
        """
        Add a new resource to the asset
        """
        self.resources.append(resource)

    def add(self, name:str, amount:float):
        """
        Add a certain amount to the resource and return remaining
        """
        resource = self.find(name)
        if resource is not None:
            if amount >= 0:
                remaining = resource.add(amount)
            else:
                remaining = -resource.sub(-amount)
        return remaining

    def add_batch(self, batch: dict):
        remaining = {}
        for key in batch:
            remaining[key] = self.add(name=key, amount=batch[key])
        return remaining

    def show(self):
        result = {}
        if len(self.resources) > 0:
            for resource in self.resources:
                result = {**result, **resource.show()} 
        return result


class Resource:

    def __init__(
        self,
        name: str,
        current_amount: float = 0,
        max_amount: float = None
    ):
        self.name = name
        self.max_amount = max_amount
        if max_amount is not None:
            if current_amount < max_amount:
                self.current_amount = current_amount
            else:
                raise ValueError
        else:
            self.current_amount = current_amount

    def add(self, amount: float):
        """
        Add a certain amount to the resource and return remaining
        """
        remaining = None
        capacity = self.max_amount - self.current_amount
        if capacity >= amount:
            self.current_amount += amount
            remaining = 0
        else:
            self.current_amount = deepcopy(self.max_amount)
            remaining = amount - capacity
        return remaining

    def sub(self, amount:float):
        """
        Subtract a certain amount from the resource and return remaining
        """
        remaining = None
        if amount <= self.current_amount:
            self.current_amount -= amount
            remaining = 0
        else:
            remaining = amount - self.current_amount
            self.current_amount = 0
        return remaining

    def show(self):
        return {self.name: self.current_amount,}


if __name__ == "__main__":
    r1 = Resource('food', 5, 10)
    r2 = Resource('water', 2, 4)
    a = Asset()
    a.add_resource(r1)
    a.add_resource(r2)
    print(a.show())
    batch = {'food': 7, 'water': -3}
    remaining = a.add_batch(batch)
    print("remaining: :", remaining)
    print(a.show())
