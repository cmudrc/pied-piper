from piperabm.transporation import Transportation
from piperabm.unit import Unit


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


if __name__ == "__main__":
    transportation = Walk()
    #print(transportation)

    length = 1000
    delta_t = transportation.how_long(length)
    delta_f = transportation.how_much_fuel(length)
    print('delta_t:', delta_t)
    print('delta_f:', delta_f)