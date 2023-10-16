from piperabm.agent import Agent
from piperabm.resources import Resource
from piperabm.unit import Date


resource = Resource()
resource.create('food', amount=20, max=100)
resource.create('water', amount=30, max=100)
resource.create('energy', amount=40, max=100)

agent = Agent(
    name='John',
    origin=0,
    start_date=Date(2020, 1, 2),
    resource=resource,
    balance=100,
)


if __name__ == "__main__":
    print(agent)