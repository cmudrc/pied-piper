from piperabm.agent import Agent
from piperabm.resources import Resource
from piperabm.unit import Date


resource = Resource()
resource.create('food', amount=70, max=100)
resource.create('water', amount=80, max=100)
resource.create('energy', amount=90, max=100)

agent = Agent(
    name='Peter',
    origin=1,
    start_date=Date(2020, 1, 4),
    resource=resource,
    balance=200,
)


if __name__ == "__main__":
    print(agent)