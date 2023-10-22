from piperabm.society import Agent
from piperabm.resources import Resources, Resource


resources = Resources()
food = Resource(name="food", amount=70, max=100)
water = Resource(name="water", amount=80, max=100)
energy = Resource(name="energy", amount=90, max=100)

agent = Agent(
    name="Peter",
    resources=resources,
    balance=200
)


if __name__ == "__main__":
   agent.print