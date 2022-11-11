import matplotlib.pyplot as plt

from piperabm.asset import Resource
from piperabm.asset import Use, Produce, Storage, Deficiency
from piperabm.search import find_element


class Asset:

    def __init__(
        self,
        resources=[],
    ):
        self.resources = resources

    def refill(self, delta_t):
        for resource in self.resources:
            if resource.use is not None:
                resource.use.refill(delta_t)
            if resource.produce is not None:
                resource.produce.refill(delta_t)
    
    def resource(self, resource_name):
        return find_element(resource_name, self.resources)

    def add(self, resource_name, amount):
        resource = self.resource(resource_name)
        return resource.add(amount)

    def sub(self, resource_name, amount):
        resource = self.resource(resource_name)
        return resource.sub(amount)

    def source(self, resource_name):
        resource = self.resource(resource_name)
        return resource.source()

    def demand(self, resource_name):
        resource = self.resource(resource_name)
        return resource.demand()    

    def __str__(self):
        txt = ''
        for resource in self.resources:
            txt += '\n'
            txt += ' # ' + resource.name + '\n'
            txt += resource.__str__()
        return txt

    def to_dict(self):
        dictionary = {}
        for resource in self.resources:
            dictionary[resource.name] = resource.to_dict()
        return dictionary

    def from_dict(self, dictionary:dict):
        d = dictionary
        resources = []
        for resource_name in d:
            resource = Resource().from_dict(d[resource_name])
            resources.append(resource)
        self.resources = resources

    def show(self):
        # Subplots are organized in a Rows x Cols Grid
        # Tot and Cols are known
        Tot = len(self.resources)
        Cols = Tot
        # Compute Rows required
        Rows = Tot // Cols 
        #     EDIT for correct number of rows:
        #     If one additional row is necessary -> add one:
        if Tot % Cols != 0:
            Rows += 1
        # Create a Position index
        Position = range(1,Tot + 1)
        fig = plt.figure()
        for k in range(Tot):
            ax = fig.add_subplot(Rows, Cols, Position[k])
            self.resources[k].to_plt(ax)
        plt.show()


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

    a = Asset([food, water])
    print(a)