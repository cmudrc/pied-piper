from piperabm.society import Agent
from piperabm.resources import Resources, Resource


food = Resource(name="food", amount=20, max=100)
water = Resource(name="water", amount=30, max=100)
energy = Resource(name="energy", amount=40, max=100)
resources = Resources(food, water, energy)

agent = Agent(
    name="John",
    resources=resources,
    balance=100,
    income=100 / (24*3600*30)
)


if __name__ == "__main__":
    agent.print