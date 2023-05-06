from piperabm.transporation import Transportation
from piperabm.unit import Unit


class Vehicle(Transportation):

    def __init__(self):
        super().__init__(
            name='vehicle',
            speed=Unit(100, 'km/hour').to_SI(),
            fuel_rate={
                'food': Unit(0, 'kg/day').to_SI(),
                'water': Unit(0, 'kg/day').to_SI(),
                'energy': Unit(1, 'kg/day').to_SI(),
            }
        )


if __name__ == "__main__":
    transportation = Vehicle()
    print(transportation)