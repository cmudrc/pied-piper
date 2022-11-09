import numpy as np

from piperabm.asset import Use, Storage
from piperabm.unit import Unit, DT


class Transportation():
    def __init__(
            self,
            name=None,
            speed=0,
            fuel_rate=None,
            storage_max=None
    ):
        self.name = name
        self.speed = speed
        self.fuel_rate = fuel_rate  # resource used for the transport
        self.storage_max = storage_max

    def how_long(self, length):
        """
        Calculate how long does it take to move by length amount.
        """
        d_time = length / self.speed
        return DT(seconds=d_time)

    def how_much_fuel(self, length):
        """
        How much fuel is needed for reaching the destination?
        """
        t = self.how_long(length)
        result = {}
        for fuel_name in self.fuel_rate:
            use = self.fuel_rate[fuel_name]
            #print(use.rate)
            result[fuel_name] = (t.seconds) * use.rate
        return result

    def __str__(self):
        return str(self.name)


class Foot(Transportation):
    def __init__(
        self,
        speed=Unit(5, 'km/hour').to_SI(),
        fuel_rate=Unit(1, 'kg/hour').to_SI(),
        storage_max=Unit(20, 'kg').to_SI()
    ):
        super().__init__(
            name='foot',
            speed=speed,
            fuel_rate={'food': Use(rate=fuel_rate),},
            storage_max=storage_max
        )


class Vehicle(Transportation):
    def __init__(
        self,
        speed=Unit(100, 'km/hour').to_SI(),
        fuel_rate=Unit(1, 'kg/hour').to_SI(),
        storage_max=Unit(200, 'kg').to_SI()
    ):
        super().__init__(
            name='vehicle',
            speed=speed,
            fuel_rate={'energy': Use(rate=fuel_rate), },
            storage_max=storage_max
        )


if __name__ == "__main__":
    transportation = Foot()
    #print('transportation.name:', transportation.name)
    length = 1000
    delta_t = transportation.how_long(length)
    delta_m = transportation.how_much_fuel(length)
    print('delta_t:', delta_t)
    print('delta_m:', delta_m)
