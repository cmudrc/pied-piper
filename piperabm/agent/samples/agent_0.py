from piperabm.agent import Agent
from piperabm.resources import Resources, Resource


resources = Resources()
food = Resource(name="food", amount=20, max=100)
water = Resource(name="water", amount=30, max=100)
energy = Resource(name="energy", amount=40, max=100)

agent = Agent(
    name="John",
    resources=resources,
    balance=100
)


if __name__ == "__main__":
    print(agent)