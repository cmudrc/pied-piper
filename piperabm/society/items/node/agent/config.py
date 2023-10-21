from piperabm.transporation import Transportation
from piperabm.resources import Resources, Resource
from piperabm.tools.unit import Unit


""" resource """
RESOURCES_VITAL = ["food", "water"]
RESOURCES_NONVITAL = ["energy"]
RESOURCES_ALL = RESOURCES_VITAL + RESOURCES_NONVITAL

food_default = Resource(name="food", amount=0)
water_default = Resource(name="water", amount=0)
energy_default = Resource(name="energy", amount=0)
RESOURCES_DEFAULT = Resources(food_default, water_default, energy_default)

""" idle fuel rate """
food_human_idle = Resource(name="food", amount=Unit(2, "kg/day").to_SI())
water_human_idle = Resource(name="water", amount=Unit(4, "kg/day").to_SI())
energy_human_idle = Resource(name="energy", amount=Unit(0, "kg/day").to_SI())
FUELS_RATE_HUMAN_IDLE = Resources(food_human_idle, water_human_idle, energy_human_idle)

""" trasportation """
food_walk = Resource(name="food", amount=Unit(2, "kg/day").to_SI())
water_walk = Resource(name="water", amount=Unit(1, "kg/day").to_SI())
energy_walk = Resource(name="energy", amount=Unit(0, "kg/day").to_SI())
fuels_rate_walk = Resources(food_walk, water_walk, energy_walk)

WALK = Transportation(
    name="walk",
    speed=Unit(5, "km/hour").to_SI(),
    fuels_rate=fuels_rate_walk
)