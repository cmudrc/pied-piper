from piperabm.society.agent import Agent
from piperabm.resource import Resource


resource = Resource()
resource.create('food', amount=20, max=100)
resource.create('water', amount=30, max=100)
resource.create('energy', amount=40, max=100)

agent = Agent(
    name='John',
    origin=0,
    resource=resource,
    balance=100,
)


if __name__ == "__main__":
    print(agent)