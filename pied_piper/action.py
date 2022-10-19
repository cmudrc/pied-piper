import numpy as np

from tools import find_element


class Action:

    def __init__(
        self,
        start_date,
        start_point,
        end_point,
        transportation
    ):
        self.start_date = start_date
        self.start_point = start_point
        self.start_pos = None
        self.end_point = end_point
        self.end_pos = None
        self.transportation = transportation

    def update(self, all_settlements):
        self.start_pos = find_element(self.start_point, all_settlements).pos
        self.end_pos = find_element(self.end_point, all_settlements).pos

    def travel_duration(self):
        pass

    def when_reach(self):
        pass
    
    def pos(self, date):
        delta_t = (self.start_date - date).seconds
        print(delta_t)
        displacement_vector = self.direction_vector() * delta_t
        return self.start_pos + displacement_vector

    def total_displacement_vector(self):
        return np.array(self.end_pos) - np.array(self.start_pos)

    def direction_vector(self):
        """
        Normalize the total_displacement_vector
        """
        vector = self.total_displacement_vector()
        return vector / np.sqrt(np.sum(vector**2))


if __name__ == "__main__":
    from tools import date, dt
    from transportation import Foot
    from settlement import Settlement

    s_1 = Settlement(
        name='settlement_1',
        pos=[0, 0],
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )

    s_2 = Settlement(
        name='settlement_2',
        pos=[1, 0.2],
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 0.5
        }
    )

    settlements = [s_1, s_2]

    start_date = date(2020, 1, 1)
    a = Action(
        start_date=start_date,
        start_point='settlement_1',
        end_point='settlement_2',
        transportation=Foot()
    )
    a.update(settlements)
    #print(a.total_displacement_vector())
    #print(a.direction_vector())
    print(start_date + dt(seconds=1000))
    print(a.pos(start_date + dt(seconds=1000)))