from piperabm.transporation import Transportation
from piperabm.resource import ResourceDelta
from piperabm.unit import Unit


''' Resource '''
ALL_RESOURCES = ['food', 'water', 'energy']

VITAL_RESOURCES = ['food', 'water']

DEFAULT_RESOURCE = ResourceDelta()
DEFAULT_RESOURCE.create_zeros(ALL_RESOURCES)

''' Idle fuel rate '''
HUMAN_IDLE_FUEL_RATE = ResourceDelta(
    {
        'food': Unit(2, 'kg/day').to_SI(),
        'water': Unit(4, 'kg/day').to_SI(),
        'energy': 0
    }
)

''' Trasportation '''
class Walk(Transportation):

    def __init__(self):
        super().__init__(
            name='foot',
            speed=Unit(5, 'km/hour').to_SI(),
            fuel_rate={
                'food': Unit(2, 'kg/day').to_SI(),
                'water': Unit(1, 'kg/day').to_SI(),
                'energy': Unit(0, 'kg/day').to_SI(),
            }
        )