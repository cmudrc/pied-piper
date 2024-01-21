from piperabm.transportation import Transportation
from piperabm.matter import Matter, Matters
from piperabm.tools.unit import Unit


food = Matter(
    name='food',
    amount=Unit(2, 'kg/day').to_SI(),
)
water = Matter(
    name='water',
    amount=Unit(1, 'kg/day').to_SI(),
)
energy = Matter(
    name='energy',
    amount=Unit(0, 'kg/day').to_SI(),
)
fuels_rate = Matters(food, water, energy)

transportation = Transportation(
    name='walk',
    speed=Unit(5, 'km/hour').to_SI(),
    fuels_rate=fuels_rate
)


if __name__ == '__main__':
    transportation.print
