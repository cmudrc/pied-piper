from piperabm.transporation import Transportation
from piperabm.unit import Unit


transportation = Transportation(
    name='foot',
    speed=Unit(5, 'km/hour').to_SI(),
    fuel_rate={
        'food': Unit(2, 'kg/day').to_SI(),
        'water': Unit(1, 'kg/day').to_SI(),
        'energy': Unit(0, 'kg/day').to_SI(),
    }
)


if __name__ == "__main__":
    print(transportation)
