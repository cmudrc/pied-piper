from piperabm.resource import Resource
from piperabm.unit import Unit


HUMAN_IDLE_FUEL_RATE = Resource(
    {
        'food': Unit(2, 'kg/day').to_SI(),
        'water': Unit(4, 'kg/day').to_SI(),
        'energy': 0
    }
)

DEFAULT_RESOURCE = Resource(['food', 'water', 'energy']) # zeros

VITAL_RESOURCES = ['food', 'water']