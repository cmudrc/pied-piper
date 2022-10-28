try:
    from .resource import Resource
except:
    from resource import Resource

try:
    from .resource_nodes import Use, Produce, Storage, Deficiency
except:
    from resource_nodes import Use, Produce, Storage, Deficiency


class Asset:

    def __init__(
        self,
        resources=None,
    ):
        self.resources = {}
        if resources is not None:
            for resource in resources:
                self.add_single(resource)

    def add_single(self, resource:Resource):
        self.resources[resource.name] = resource

    def add_resources(self, *resources):
        for resource in resources:
            self.add_single(resource)

    def refill(self, delta_t):
        for resource_name in self.resources.keys():
            resource = self.resources[resource_name]
            if resource.use is not None:
                resource.use.refill(delta_t)
            if resource.produce is not None:
                resource.produce.refill(delta_t)

    def add(self, resource_name, amount):
        return self.resources[resource_name].add(amount)

    def sub(self, resource_name, amount):
        return self.resources[resource_name].sub(amount)

    def source(self, resource_name):
        return self.resources[resource_name].source()

    def demand(self, resource_name):
        return self.resources[resource_name].demand()    


if __name__ == "__main__":

    food = Resource(
        name='food',
        use=Use(rate=5),
        produce=Produce(rate=1),
        storage=Storage(current_amount=10, max_amount=20),
        deficiency=Deficiency(current_amount=0, max_amount=20)
    )

    water = Resource(
        name='water',
        use=Use(rate=0.1),
        storage=Storage(current_amount=10, max_amount=10),
        deficiency=Deficiency(current_amount=0, max_amount=20)
    )

    #a = Asset()
    #a.add_resources(food, water)
    a = Asset([food, water])
    print(a.source('water'), a.demand('water'))
    print(a.source('food'), a.demand('food'))