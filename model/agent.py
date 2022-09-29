from core.entity import Entity
        

class Agent(Entity):
    def __init__(self, name, pos, transportations):
        super().__init__(
            name=name,
            pos=pos
        )
        self.transportations = transportations
        self.actions = []

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
    a_1 = Agent(
        name='person_1',
        pos=[0.3, 0.4]
    )
    a_2 = Agent(
        name='person_2',
        pos=[0, 0]
    )
    print(a_1.distance(a_2))