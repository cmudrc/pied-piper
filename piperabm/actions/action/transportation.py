from piperabm.resource import DeltaResource
from piperabm.unit import Unit, DT


class Transportation:
    def __init__(
            self,
            name: str = None,
            speed: float = None,
            fuel_rate=None,
            storage_max=None
    ):
        self.name = name
        self.speed = speed # None means Infinity
        if fuel_rate is None:
            fuel_rate ={
                'food': 0,
                'water': 0,
                'energy': 0,
            }
        if isinstance(fuel_rate, dict):
            self.fuel_rate = DeltaResource(batch=fuel_rate)
        elif isinstance(fuel_rate, DeltaResource):
            self.fuel_rate = fuel_rate  # resource used for the transport
        self.storage_max = storage_max

    def how_long(self, length):
        """
        Calculate how long does it take to move by length amount.
        """
        speed = self.speed
        if speed is None:
            d_time = 0
        else:
            d_time = length / self.speed
        return DT(seconds=d_time)

    def how_much_fuel(self, length):
        """
        Calculate the amount of required fuel
        """
        t = self.how_long(length)
        return self.fuel_rate * t.total_seconds()

    def __str__(self):
        return str(self.name)


class Walk(Transportation):
    def __init__(self):
        super().__init__(
            name='foot',
            speed=Unit(5, 'km/hour').to_SI(),
            fuel_rate={
                'food': Unit(2, 'kg/day').to_SI(),
                'water': Unit(1, 'kg/day').to_SI(),
                'energy': Unit(0, 'kg/day').to_SI(),
            },
            storage_max=Unit(20, 'kg').to_SI()
        )


class Vehicle(Transportation):
    def __init__(self):
        super().__init__(
            name='vehicle',
            speed=Unit(100, 'km/hour').to_SI(),
            fuel_rate={
                'food': Unit(0, 'kg/day').to_SI(),
                'water': Unit(0, 'kg/day').to_SI(),
                'energy': Unit(1, 'kg/day').to_SI(),
            },
            storage_max=Unit(200, 'kg').to_SI()
        )


if __name__ == "__main__":
    transportation = Walk()
    #print('transportation.name:', transportation.name)
    length = 1000
    delta_t = transportation.how_long(length)
    delta_f = transportation.how_much_fuel(length)
    print('delta_t:', delta_t)
    print('delta_f:', delta_f)
