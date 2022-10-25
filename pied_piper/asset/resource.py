try:
    from .dynamic import Use, Produce
except:
    from dynamic import Use, Produce

try:
    from .static import Storage, Deficiency
except:
    from static import Storage, Deficiency


class Resource:

    def __init__(
        self,
        name:str,
        use:Use=None,
        produce:Produce=None,
        storage:Storage=None,
        deficiency:Deficiency=None
    ):
        self.name = name
        self.use = use
        self.produce = produce
        self.storage = storage
        self.deficiency = deficiency

    def refill(self):
        pass

    def solve(self):
        pass

    def add(self, amount:float):
        self.use 


class Asset:

    def __init__(
        self,
        resources:dict={},
    ):
        self.resources = resources

    def add_single(self, resource:Resource):
        self.resources[resource.name] = resource

    def add(self, *resources):
        for resource in resources:
            self.add_single(resource)


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

    a = Asset()
    a.add(food, water)
    print(a.resources)