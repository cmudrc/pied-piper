import numpy as np

from tools import dt
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
        """
        Read the desired info from other elements
        """
        self.start_pos = find_element(self.start_point, all_settlements).pos
        self.end_pos = find_element(self.end_point, all_settlements).pos

    def travel_duration(self):
        """
        Total duration of the action
        """
        vector = self.total_displacement_vector()
        vector_size = np.sqrt(np.sum(vector**2))
        delta_t_SI = vector_size / self.transportation.speed
        return dt(seconds=delta_t_SI)

    def when_reach(self):
        """
        Calculate the date in which the destination will be reached
        """
        delta_t = self.travel_duration()
        return self.start_date + delta_t

    def pos(self, date):
        """
        Calculate the position on the requested date
        """
        result = None
        action_progress = self.action_progress(date)
        if action_progress < 0:
            result = self.start_pos
        elif action_progress >= 0 and action_progress <= 1:
            current_displacement_vector = action_progress * self.total_displacement_vector()
            result = self.start_pos + current_displacement_vector
        elif action_progress > 1:
            result = self.end_pos
        return result

    def action_progress(self, date):
        """
        Calculate the action_progress on the requested date

        Returns:
            result: float in range 0 < ... < 1
        """
        result = None
        end_date = self.when_reach()
        if date < self.start_date:
            result = 0
        elif date >= self.start_date and date <= end_date:
            result = (date - self.start_date).seconds / (end_date - self.start_date).seconds
        else:
            result = 1
        return result

    def total_displacement_vector(self):
        """
        Total displacement vector between starting point and ending point
        """
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
        pos=[1000, 0],
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
    print(start_date + dt(seconds=360))
    print(a.pos(start_date + dt(seconds=360)))
    #print(a.when_reach())