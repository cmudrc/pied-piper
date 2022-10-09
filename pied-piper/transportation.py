import numpy as np
from datetime import timedelta

from tools import Use, Storage
from tools import Unit


class Transportation():
    def __init__(
            self,
            name=None,
            speed=0,
            fuel_rate=None,
            storage_max=None
    ):
        self.name = name
        self.speed = speed  # km/h
        self.fuel_rate = fuel_rate  # resource used for the transport
        self.storage_max = storage_max

    def displacement(self, t, t_0, direction):
        i = direction[0]
        j = direction[1]
        ''' normalizing i and j '''
        L = np.power((np.power(i, 2) + np.power(j, 2)), 0.5)
        i = i/L
        j = j/L

        displacement_total = (t - t_0) * self.speed
        displacement_x = displacement_total * i
        displacement_y = displacement_total * j
        return [displacement_x, displacement_y]

    def how_long(self, pos, pos_destination):
        """
        How long does it take to reach the destination? (in hours)
        """

        x_0 = pos[0]
        y_0 = pos[1]
        x_1 = pos_destination[0]
        y_1 = pos_destination[1]
        delta_i = x_0 - x_1
        delta_j = y_0 - y_1
        L = np.power((np.power(delta_i, 2) + np.power(delta_j, 2)), 0.5)  # km
        t = L / self.speed.to('km/h').val  # hour
        return timedelta(hours=t)

    def how_much_fuel(self, pos, pos_destination):
        """
        How much fuel is needed for reaching the destination? (in hours)
        """

        t = self.how_long(pos, pos_destination)  # hours
        result = {}
        for fuel_name in self.fuel_rate:
            use = self.fuel_rate[fuel_name]
            rate = use.rate.to('kg/hour').val
            #print(rate)
            result[fuel_name] = (t.seconds / 3600) * rate  # kg
        return result

    def __str__(self):
        return str(self.name)


class Foot(Transportation):
    def __init__(
        self,
        speed=Unit(5, 'km/h'),
        fuel_rate=Unit(1, 'kg/h'),
        storage_max=Unit(20, 'kg')
    ):
        super().__init__(
            name='foot',
            speed=speed,
            fuel_rate={'food': Use(rate=fuel_rate), },
            storage_max=storage_max
        )


class Vehicle(Transportation):
    def __init__(
        self,
        speed=Unit(100, 'km/h'),
        fuel_rate=Unit(1, 'kg/h'),
        storage_max=Unit(200, 'kg')
    ):
        super().__init__(
            name='vehicle',
            speed=speed,  # km/h
            fuel_rate={'energy': Use(rate=fuel_rate), },
            storage_max=storage_max
        )


if __name__ == "__main__":
    transportation = Foot()
    #print('transportation.name:', transportation.name)
    delta_t = transportation.how_long([0, 0], [1, 0])  # km
    delta_m = transportation.how_much_fuel([0, 0], [1, 0])  # km
    #print('delta_t:', delta_t)
    print('delta_m:', delta_m)
