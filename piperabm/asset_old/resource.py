import matplotlib.pyplot as plt

from piperabm.resource import Use, Produce, Storage, Deficiency
from piperabm.graphics.plt.resource import resource_to_plt


class Resource:

    def __init__(
        self,
        name:str='',
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
        """
        Refill the nodes that charge by flow (use and produce)
        """
        if self.use is not None:
            self.use.refill(delta_t)
        if self.produce is not None:
            self.produce.refill(delta_t)

    def allocate_internal(self):
        """
        Solve inner nodes within a resource with each other.
        """
        source = self.source()
        demand = self.demand()
        amount = min([source, demand])
        remaining = self.sub(amount)
        if remaining > 0:
            print("Error in solving internally")
        remaining = self.add(amount)
        if remaining > 0:
            print("Error in solving internally")


    def finalize(self):
        """
        Finalize the calculation in the end of step
        """
        if self.deficiency is not None:
            if self.use is not None:
                self.deficiency.add(self.use.current_amount)
        if self.use is not None:
            self.use.current_amount = 0
        if self.produce is not None:
            self.produce.current_amount = 0

    def is_alive(self):
        """
        Check whether the resource is alive
        """
        result = True
        if self.deficiency is not None:
            result = self.deficiency.is_alive()
        return result

    def add(self, amount:float):
        """
        Add a certain amount to the resource and return remaining
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
        Subtract a certain amount from the resource and return remaining
        """
        if self.produce is not None:
            amount = self.produce.sub(amount)
        if self.storage is not None:
            amount = self.storage.sub(amount)
        return amount

    def source(self):
        """
        Calculate total value for source
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
        Calculate value for demand
        """
        demand = 0
        if self.use is not None:
            if self.use.current_amount is not None:
                demand += self.use.current_amount
        if self.deficiency is not None:
            if self.deficiency.current_amount is not None:
                demand += self.deficiency.current_amount
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

    def to_dict(self):
        dictionary = {
            'name': self.name,
            'use': None,
            'produce': None,
            'storage': None,
            'deficiency': None
        }
        if self.use is not None: dictionary['use'] = self.use.to_dict(),
        if self.produce is not None: dictionary['produce'] = self.produce.to_dict(),
        if self.storage is not None: dictionary['storage'] = self.storage.to_dict(),
        if self.deficiency is not None: dictionary['deficiency'] = self.deficiency.to_dict(),
        
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.name = d['name']
        self.use = Use().from_dict(d['use'])
        self.produce = Produce().from_dict(d['produce'])
        self.storage = Storage().from_dict(d['storage'])
        self.deficiency = Deficiency().from_dict(d['deficiency'])

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        resource_to_plt(self.to_dict(), ax)

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title(self.name)
        self.to_plt(ax)
        plt.show()


if __name__ == "__main__":

    food = Resource(
        name='food',
        use=Use(rate=1),
        produce=Produce(rate=1),
        storage=Storage(current_amount=10, max_amount=20),
        deficiency=Deficiency(current_amount=5, max_amount=20)
    )
    
    ''' initial '''
    print('>>> initial')
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)
    
    ''' refill '''
    print('>>> refill')
    food.refill(10)
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)

    food.show()

    ''' solve '''
    print('>>> solve')
    food.allocate_internal()
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)

    ''' add '''
    print('>>> add')
    amount = 70
    remaining = food.add(amount)
    print('amount:', amount, '/', 'remaining:', remaining, '\n')
    print('source:', food.source(), '/', 'demand:', food.demand())
    print(food)