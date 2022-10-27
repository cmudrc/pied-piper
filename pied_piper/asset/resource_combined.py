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

    def refill(self, delta_t):
        self.use.refill(delta_t)
        self.produce.refill(delta_t)

    def solve(self):
        """
        Solve inner nodes within a resource with each other.
        """
        source = self.source()
        self.add(source)
        self.sub(source)

    def add(self, amount:float):
        """
        Add a certain amount to the resource.
        """
        if self.use is not None:
            amount = self.use.sub(amount)
        if self.deficiency is not None:
            amount = self.deficiency.sub(amount)
        if self.storage is not None:
            amount = self.storage.add(amount)
        return amount

    def sub(self, amount:float):
        """
        Subtract a certain amount from the resource.
        """
        if self.produce is not None:
            amount = self.produce.sub(amount)
        if self.storage is not None:
            amount = self.storage.sub(amount)
        return amount

    def source(self):
        """
        Calculate overall source.
        """
        source = 0
        if self.produce is not None:
            if self.produce.current_amount is not None:
                source += self.produce.current_amount
        if self.storage is not None:
            if self.storage.current_amount is not None:
                source += self.storage.current_amount
        return source
        
    def demand(self):
        """
        Calculate overall demand.
        """
        demand = 0
        if self.use is not None:
            if self.use.current_amount is not None:
                demand += self.use.current_amount
        if self.deficiency is not None:
            if self.deficiency.current_amount is not None:
                demand = self.deficiency.current_amount
        if self.storage is not None:
            if self.storage.current_amount is not None:
                demand += self.storage.max_amount - self.storage.current_amount
        return demand

    def __str__(self):
        txt = ''
        if self.use is not None:
            txt += 'use: ' + str(self.use.current_amount) + '\n'
        if self.produce is not None:
            txt += 'produce: ' + str(self.produce.current_amount) + '\n'
        if self.storage is not None:
            txt += 'storage: ' + str(self.storage.current_amount) + '\n'
        if self.deficiency is not None:
            txt += 'deficiency: ' + str(self.deficiency.current_amount) + '\n'
        return txt


if __name__ == "__main__":

    food = Resource(
        name='food',
        use=Use(rate=1),
        produce=Produce(rate=1),
        storage=Storage(current_amount=10, max_amount=20),
        deficiency=Deficiency(current_amount=5, max_amount=20)
    )

    ''' initial '''
    print('initial')
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)

    ''' refill '''
    print('refill')
    food.refill(10)
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)

    ''' solve '''
    print('solve')
    food.solve()
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)

    ''' add '''
    print('add')
    amount = 70
    remaining = food.add(amount)
    print('amount:', amount, '/', 'remaining:', remaining, '\n')
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)