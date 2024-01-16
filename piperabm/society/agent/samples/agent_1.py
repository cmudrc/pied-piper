from piperabm.society import Agent
from piperabm.resources import Resources, Resource


food = Resource(name='food', amount=70, max=100)
water = Resource(name='water', amount=80, max=100)
energy = Resource(name='energy', amount=90, max=100)
resources = Resources(food, water, energy)

agent = Agent(
    name='Peter',
    resources=resources,
    balance=200,
    income=200 / (24*3600*30)
)


if __name__ == '__main__':
   agent.print