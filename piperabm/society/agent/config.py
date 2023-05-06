from piperabm.resource import ResourceDelta
from piperabm.unit import Unit


HUMAN_IDLE_FUEL_RATE = ResourceDelta(
    {
        'food': Unit(2, 'kg/day').to_SI(),
        'water': Unit(4, 'kg/day').to_SI(),
        'energy': 0
    }
)

DEFAULT_RESOURCE = ResourceDelta()
DEFAULT_RESOURCE.create_zeros(['food', 'water', 'energy']) # zeros

VITAL_RESOURCES = ['food', 'water']