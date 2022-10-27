from resource_combined import Resource
from resource_static import Storage, Deficiency
from resource_dynamic import Use, Produce


class Asset:

    def __init__(
        self,
        resources=None,
    ):
        self.resources = {}
        if resources is not None:
            for resource in resources:
                self.add(resource)

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
    b = Asset([food, water])
    print(b.resources)