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
    index=1,
    name='Robert',
    origin_node=1,
    transportation=None,
    queue=None,
    resource=resource,
    idle_fuel_rate=None,
    balance=200,
    wealth_factor=1
)


if __name__ == "__main__":
    print(agent)