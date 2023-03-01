import numpy as np

from piperabm.unit import DT
from piperabm.tools import euclidean_distance


class Track:
    
    def __init__(self, start_index, start_pos, end_index, end_pos, adjusted_length):
        self.start_index = start_index
        self.start_pos = start_pos
        self.end_index = end_index
        self.end_pos = end_pos
        self.adjusted_length = adjusted_length

    def refine_delta_time(self, delta_time):
        if isinstance(delta_time, (int, float)):
            delta_time = delta_time
        elif isinstance(delta_time, DT):
            delta_time = delta_time.total_seconds()
        else: raise ValueError
        return delta_time

    def duration(self, transportation):
        duration = transportation.how_long(self.adjusted_length)
        return duration.total_seconds()
    
    def fuel(self, transportation):
        return transportation.how_much_fuel(self.adjusted_length)

    def progress(self, delta_time, transportation):
        delta_time = self.refine_delta_time(delta_time)
        progress = delta_time / self.duration(transportation)
        if progress < 0:
            progress = 0
        elif progress > 1:
            progress = 1
        return progress

    def pos(self, delta_time, transportation):
        delta_time = self.refine_delta_time(delta_time)
        progress = self.progress(delta_time, transportation)
        current_length = progress * euclidean_distance(*self.start_pos, *self.end_pos)
        pos_0 = np.array(self.start_pos)
        delta_x = self.end_pos[0] - self.start_pos[0]
        delta_y = self.end_pos[1] - self.start_pos[1]
        if delta_x == 0:
            if delta_y > 0:
                theta = np.pi / 2
            else:
                theta = 3 * np.pi / 2
        else:
            m = delta_y / delta_x
            theta = np.arctan(m)
        displacement = current_length * np.array([np.cos(theta), np.sin(theta)])
        return list(pos_0 + displacement)
 
    def __str__(self):
        txt = '"track" from '
        txt += str(self.start_pos)
        txt += ' to '
        txt += str(self.end_pos)
        return txt


if __name__ == "__main__":
    from piperabm.transportation import Foot

    t = Track(
        start_index=0, 
        start_pos=[-100, -100], 
        end_index=1, 
        end_pos=[100, 100], 
        adjusted_length=400
    )
    pos = t.pos(delta_time=250, transportation=Foot())
    print(pos)