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
    balance=100,
    income=100 / (24*60*60*30)  # monthly
)


if __name__ == '__main__':
    agent.print