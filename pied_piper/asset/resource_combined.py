try:
    from .resource_dynamic import Use, Produce
except:
    from resource_dynamic import Use, Produce

try:
    from .resource_static import Storage, Deficiency
except:
    from resource_static import Storage, Deficiency


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
        amount = self.use.sub(amount)
        amount = self.storage.add(amount)
        self.deficiency

    def sub(self, amount:float):
        amount = self.produce.sub(amount)
        amount = self.storage.sub(amount)
        return amount
    

    """
            use:Use=Use(rate=0),
        produce:Produce=Produce(rate=0),
        storage:Storage=Storage(current_amount=0, max_amount=0),
        deficiency:Deficiency=Deficiency(current_amount=0, max_amount=0)
    """




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