import  numpy as np
import matplotlib.pyplot as plt

from piperabm.degradation import DegradationProperty, degradation_kwargs, Eternal
from piperabm.graphics.plt.path import track_to_plt


class Track(DegradationProperty):

    def __init__(self, name_start, name_end, *elements):
        super().__init__(
            **degradation_kwargs
        )
        self.name_start = name_start
        self.name_end = name_end
        self.length = None
        self.difficulty = 1

    def probability_of_working(self, start_date, end_date):
        default_length = 1  # meter
        t1 = start_date
        t2 = end_date
        if isinstance(self.distribution, Eternal):
            t0 = t1
        else:
            t0 = self.initiation_date

        Q = self.distribution.probability(
            time_start=(t1-t0).total_seconds(),
            time_end=(t2-t0).total_seconds()
        )
        Q = Q * (self.length / default_length)
        P = 1 - Q
        return P

    def xylim(self):
        delta_x = np.abs(self.pos_start[0] - self.pos_end[0])
        delta_y = np.abs(self.pos_start[1] - self.pos_end[1])
        center_x = (self.pos_start[0] + self.pos_end[0]) / 2
        center_y = (self.pos_start[1] + self.pos_end[1]) / 2
        xlim = [center_x - delta_x,
                center_x + delta_x]
        ylim = [center_y - delta_y,
                center_y + delta_y]
        return xlim, ylim

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')
        xlim, ylim = self.xylim()
        plt.xlim(xlim)
        plt.ylim(ylim)
        self.to_plt(ax)
        plt.show()

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        track_to_plt(self.to_dict(), ax)