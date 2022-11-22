import  numpy as np
import matplotlib.pyplot as plt

from piperabm.degradation import DegradationProperty, degradation_kwargs
from piperabm.graphics.plt.path import track_to_plt


class Track(DegradationProperty):

    def __init__(self):
        super().__init__(
            **degradation_kwargs
        )

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