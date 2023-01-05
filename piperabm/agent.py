from piperabm.unit import Date
from piperabm.transportation import Foot


class Agent:
    """
    Representes an agent.
    """

    def __init__(
        self,
        name=None,
        pos=[0, 0],
        active=True,
        asset=None,
        settlement=None,
        transportations=[Foot()],
    ):
        """
        Args:
            birthday: datetime object
            resources: a list containing all resources that the agent use, produce, or store
            settlement: the name the settlement that agent resides
            transportations: a list of possible transportation methods
        """
        self.name = name
        self.pos = pos
        self.active = active
        self.transportations = transportations
        self.asset = asset
        self.settlement = settlement

    def solve(self):
        """
        Phase I in update sequence
        """
        if self.asset is not None:
            self.asset.solve()

    def prepare(self, delta_t):
        """
        Prepare agent for the next step
        """
        if self.asset is not None:
            self.asset.refill(delta_t)

    def finalize(self):
        """
        Finalize the step
        """
        if self.asset is not None:
            self.asset.finalize()
            if not self.asset.is_alive():
                self.active = False

    def decide(self):
        pass

    def to_dict(self) -> dict:
        dictionary = {
            'name': self.name,
            'pos': self.pos,
            'active': self.active,
            'asset': None
        }
        if self.asset is not None:
            dictionary['asset'] = self.asset.to_dict()
        return dictionary

'''
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
'''

def generate_agent(count=1):
    result = list()
    i = 0
    while i < count:
        result.append(Agent(
            pos=[0, 0]
        ))
    return result
'''


def from_dict(self, dictionary: dict):
    d = dictionary
    self.x_lim = d['center']
    self.y_lim = d['radius']
    self.asset = Asset().from_dict(d['asset'])
    settlements_list = d['settlements']
    self.settlements = []
    for settlement_dict in settlements_list:
        s = Settlement()
        s.from_dict(settlement_dict)
        self.settlements.append(s)
'''

if __name__ == "__main__":
    from piperabm.asset import Resource


    resources = [
        Resource
    ]
    a = Agent(
        asset=None
    )

    '''
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
    '''
    #print(a_1.distance(a_2))
    #print(a_2.transportations[0])