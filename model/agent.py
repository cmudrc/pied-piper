from core.entity import Entity
from transportation import Foot
        

class Agent(Entity):
    def __init__(self, name, pos, vehicles=[]):
        super().__init__(
            name=name,
            pos=pos
        )
        
        self.vehicles = vehicles
        self.transportation_calc()

    def transportation_calc(self):
        self.transportations = []
        for vehicle in self.vehicles:
            self.transportations.append(vehicle)
        self.transportations.append(Foot()) # everyone at least walks

    def decide(self):
        pass


def generate_agent(count=1):
    result = list()
    i = 0
    while i < count:
        result.append(Agent(
            pos=[0, 0]
        ))
    return result


if __name__ == "__main__":
    from transportation import Truck


    a_1 = Agent(
        name='person_1',
        pos=[0.3, 0.4],
        vehicles=[Truck()]
    )
    a_2 = Agent(
        name='person_2',
        pos=[0, 0],
        vehicles=[]
    )
    #print(a_1.distance(a_2))
    #print(a_2.transportations[0])