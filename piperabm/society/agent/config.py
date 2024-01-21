from piperabm.transportation import Transportation
#from piperabm.resources import Resources, Resource
from piperabm.matter import Matter, Matters, Container, Containers
from piperabm.tools.unit import Unit


""" resource """
RESOURCES_VITAL = ['food', 'water']
RESOURCES_NONVITAL = ['energy']
RESOURCES_ALL = RESOURCES_VITAL + RESOURCES_NONVITAL

food_default = Container(
    matter=Matter(name='food', amount=30),
    max=100,
    min=0
)
water_default = Container(
    matter=Matter(name='water', amount=40),
    max=100,
    min=0
)
energy_default = Container(
    matter=Matter(name='energy', amount=50),
    max=100,
    min=0
)
RESOURCES_DEFAULT = Containers(food_default, water_default, energy_default)

""" idle fuel rate """
food_rate_human_idle = Matter(name='food', amount=Unit(2, 'kg/day').to_SI())
water_rate_human_idle = Matter(name='water', amount=Unit(4, 'kg/day').to_SI())
energy_rate_human_idle = Matter(name='energy', amount=Unit(0, 'kg/day').to_SI())
FUELS_RATE_HUMAN_IDLE = Matters(food_rate_human_idle, water_rate_human_idle, energy_rate_human_idle)

""" trasportation """
food_rate_walk = Matter(name='food', amount=Unit(2, 'kg/day').to_SI())
water_rate_walk = Matter(name='water', amount=Unit(1, 'kg/day').to_SI())
energy_rate_walk = Matter(name='energy', amount=Unit(0, 'kg/day').to_SI())
fuels_rate_walk = Matters(food_rate_walk, water_rate_walk, energy_rate_walk)

WALK = Transportation(
    name='walk',
    speed=Unit(5, 'km/hour').to_SI(),
    fuels_rate=fuels_rate_walk
)