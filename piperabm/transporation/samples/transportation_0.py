from piperabm.transporation import Transportation
from piperabm.resources import Resources, Resource
from piperabm.tools.unit import Unit


food = Resource(
    name="food",
    amount=Unit(2, "kg/day").to_SI(),
)
water = Resource(
    name="water",
    amount=Unit(1, "kg/day").to_SI(),
)
energy = Resource(
    name="energy",
    amount=Unit(0, "kg/day").to_SI(),
)
fuels_rate = Resources(food, water, energy)

transportation = Transportation(
    name="walk",
    speed=Unit(5, "km/hour").to_SI(),
    fuels_rate=fuels_rate
)


if __name__ == "__main__":
    transportation.print
