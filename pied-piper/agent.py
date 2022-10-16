from tools import Entity
from transportation import Foot
#from resource import Resource
        

class Agent(Entity):
    """
    Representes an agent.
    """

    def __init__(self, name, pos, resources, settlement, transportations):
        super().__init__(
            name=name,
            pos=pos
        )
        """
        Args:
            name: name
            pos: position
            resources: a list containing all resources that the agent use, produce, or store
            settlement: the name the settlement that agent resides
            transportations: a list of possible transportation methods
        """

        self.transportations = transportations
        self.resources = resources
        self.settlement = settlement

    def decide(self):
        pass


class Human(Agent):
    """
    Representes a human as a sample.
    """

    def __init__(self, name, pos, vehicles=[]):
        """
        Args:
            name: name
            pos: position
            vehicles: a list of vehicles (in the future, public transport systems may be included)
        """
        transportations = []
        transportations.append(Foot())
        for vehicle in vehicles:
            transportations.append(vehicle)

        food = Resource(
            name='food',
            use=0.1, # kg/h
            produce=0.5, # kg/h
            storage_current=0, # kg
            storage_max=10, # kg
            deficiency_current=0, # kg
            decificiency_max=10 # kg
        )
        water = Resource(
            name='water',
            use=0.1, # kg/h, liter/h
            produce=0, # kg/h, liter/h
            storage_current=10, # kg, liter
            storage_max=10, # kg, liter
            deficiency_current=0, # kg, liter
            decificiency_max=10 # kg, liter
        )
        energy = Resource(
            name='energy',
            use=0.5, # W/h
            produce=0.1, # W/h
            storage_current=0, # W
            storage_max=10, # W
            deficiency_current=0, # W
            decificiency_max=10 # W
        )
        resources = {
            'food': food,
            'water': water,
            'energy': energy,
        }
        
        super().__init__(
            name=name,
            pos=pos,
            resources=resources,
            settlement=None,
            transportations=transportations
            )


def generate_agent(count=1):
    result = list()
    i = 0
    while i < count:
        result.append(Agent(
            pos=[0, 0]
        ))
    return result


if __name__ == "__main__":
    from transportation import Vehicle


    a_1 = Human(
        name='person_1',
        pos=[0.3, 0.4],
        vehicles=[Vehicle()]
    )
    a_2 = Human(
        name='person_2',
        pos=[0, 0],
        vehicles=[]
    )
    #print(a_1.distance(a_2))
    #print(a_2.transportations[0])