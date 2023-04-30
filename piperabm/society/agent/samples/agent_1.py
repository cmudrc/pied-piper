from piperabm.society import Agent
from piperabm.resource import Resource


resource = Resource(
    current_resource={
        'food': 70,
        'water': 80,
        'energy': 90
    },
    max_resource={
        'food': 100,
        'water': 100,
        'energy': 100
    }
)
agent = Agent(
    name='Robert',
    origin=1,
    resource=resource,
    balance=200,
)


if __name__ == "__main__":
    print(agent)