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
    index=0,
    name='John',
    origin_node=0,
    transportation=None,
    queue=None,
    resource=resource,
    idle_fuel_rate=None,
    balance=100,
    wealth_factor=1
)


if __name__ == "__main__":
    print(agent)