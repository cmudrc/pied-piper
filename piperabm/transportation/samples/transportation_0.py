"""
Represent walking
"""

from piperabm.transportation import Transportation
from piperabm.matter_new import Matter
from piperabm.tools.unit import Unit


fuels_rate = Matter(
    {
        'food': Unit(2, 'kg/day').to_SI(),
        'water': Unit(1, 'kg/day').to_SI(),
        'energy': Unit(0, 'kg/day').to_SI(),
    }
)
transportation = Transportation(
    name='walk',
    speed=Unit(5, 'km/hour').to_SI(),
    fuels_rate=fuels_rate,
    wear=1
)


if __name__ == '__main__':
    print(transportation)
