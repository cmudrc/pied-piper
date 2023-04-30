from piperabm.society import Agent
from piperabm.resource import Resource


resource = Resource(
    current_resource={
        'food': 20,
        'water': 30,
        'energy': 40
    },
    max_resource={
        'food': 100,
        'water': 100,
        'energy': 100
    }
)
agent = Agent(
    name='John',
    origin=0,
    resource=resource,
    balance=100,
)


if __name__ == "__main__":
    print(agent)