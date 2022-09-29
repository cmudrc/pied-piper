import numpy as np
from datetime import timedelta
from resource import Resource


class Transportation():
    def __init__(
            self,
            name=None,
            speed=0,
            fuel=None):
        self.name = name
        self.speed = speed  # km/h
        self.fuel = fuel  # resource used for the transport

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
        '''
        How long does it take to reach the destination in hours

        '''
        x_0 = pos[0]
        y_0 = pos[1]
        x_1 = pos_destination[0]
        y_1 = pos_destination[1]
        delta_i = x_0 - x_1
        delta_j = y_0 - y_1
        L = np.power((np.power(delta_i, 2) + np.power(delta_j, 2)), 0.5)  # km
        t = L / self.speed  # hour
        return timedelta(hours=t)


    def how_much_fuel(self, pos, pos_destination):
        t = self.how_long(pos, pos_destination)
        t.hours * self.fuel.use

    def __str__(self):
        return str(self.name)


class Foot(Transportation):
    def __init__(self):
        super().__init__(
            name='foot',
            speed=5,  # km/h
            fuel=Resource(
                name='food',
                use=1  # per hour
            )
        )


class Sedan(Transportation):
    def __init__(self):
        super().__init__(
            name='sedan',
            speed=100,  # km/h
            fuel=Resource(
                name='energy',
                use=5  # per hour
            )
        )


class Truck(Transportation):
    def __init__(self):
        super().__init__(
            name='truck',
            speed=50,  # km/h
            fuel=Resource(
                name='energy',
                use=5  # per hour
            )
        )


if __name__ == "__main__":
    transportation = Foot()
    print('transportation.name:', transportation.name)
    delta_t = transportation.how_long([0, 0], [1, 0])
    print('delta_t:', delta_t)
