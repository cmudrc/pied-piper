from piperabm.society import Agent
from piperabm.matter import Matter, Container, Containers


food = Container(
    matter=Matter(name='food', amount=20),
    max=100
)
water = Container(
    matter=Matter(name='water', amount=30),
    max=100
)
energy = Container(
    matter=Matter(name='energy', amount=40),
    max=100
)
resources = Containers(food, water, energy)

agent = Agent(
    name='John',
    resources=resources,
    balance=100
)


if __name__ == '__main__':
    agent.print